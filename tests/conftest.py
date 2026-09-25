"""Configure les fixtures et les hooks Pytest communs à la suite de tests."""

from __future__ import annotations

import json
import os
import platform
from pathlib import Path
from typing import Any

import cpuinfo
import psutil
import pytest
from pytest_metadata.plugin import metadata_key

from synesthesia.Tools import Ui
from tests.Monitoring import Monitoring

os.environ["QT_QPA_PLATFORM"] = "offscreen"
os.environ["QT_OPENGL"] = "software"
os.environ["NAPARI_GUI_BACKEND"] = "none"
os.environ["VISPY_USE_APP"] = "mock"

all_tests_monitoring = Monitoring()


# ==================================================
# region Hooks pytest
# ==================================================
def _is_qt_test(item: pytest.Item | None) -> bool:
	"""
	Détecte un test Qt à partir de ses fixtures, marqueurs ou identifiant.

	:param item: Test Pytest à examiner, ou ``None``.
	:return: ``True`` si une fixture ``qtbot``, un marqueur ``qt`` ou un identifiant contenant ``qt`` ou ``gui`` est détecté.
	"""
	if item is None: return False
	fixture_names = set(getattr(item, "fixturenames", []))
	keywords = set(item.keywords)
	nodeid = str(getattr(item, "nodeid", "")).lower()
	return bool({"qtbot"} & fixture_names or {"qt"} & keywords or "qt" in nodeid or "gui" in nodeid)


# --------------------------------------------------
def cpu_infos() -> str:
	"""
	Collecte les informations relatives au processeur.

	:return: Informations disponibles sur le processeur.
	"""
	info = cpuinfo.get_cpu_info()
	res = info.get("brand_raw") or info.get("processor", "Unknown Processor")

	try:  # Cœurs / threads (tolérant aux erreurs) En cas de problème notamment sur mac
		cores = psutil.cpu_count(logical=False) or os.cpu_count()
		threads = psutil.cpu_count(logical=True) or os.cpu_count()
	# Le repli doit couvrir les erreurs de collecte propres aux plateformes.
	except Exception: cores = threads = os.cpu_count()  # noqa: BLE001

	try:  # En cas de problème notamment sur mac
		freq = "Unknown frequency"
		if hasattr(psutil, "cpu_freq"):
			cpu_info = psutil.cpu_freq(percpu=False)
			if cpu_info and getattr(cpu_info, "current", None): freq = f"{cpu_info.current / 1000:.2f} GHz"
		res += f" ({freq} - {cores} Cores ({threads} Logical))"
	except RuntimeError: res += "(No CPU Infos)"
	return res


# --------------------------------------------------
def add_to_json(path: str | Path, datas_name: str, datas: Any):
	"""
	Ajoute des données à un fichier JSON.

	:param path: Chemin du fichier JSON.
	:param datas_name: Clé des données à ajouter.
	:param datas: Données à ajouter.
	"""
	try:
		with open(path) as f: data = json.load(f)
		data[datas_name] = datas
		with open(path, "w") as f: json.dump(data, f, indent=4)
	except FileNotFoundError: Ui.print_warning("Json File not found.")


# --------------------------------------------------
# Fonction pour configurer les métadonnées du rapport
# --------------------------------------------------
@pytest.hookimpl
def pytest_metadata(metadata):
	"""
	Complète les métadonnées du rapport Pytest.

	:param metadata: Métadonnées du rapport Pytest.
	"""
	metadata["System"] = platform.system()
	metadata["Platform"] = platform.platform()
	metadata["CPU"] = cpu_infos()
	metadata["RAM"] = f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB"

	# Ajout de la carte graphique si disponible
	try:
		from pynvml import nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex, nvmlDeviceGetMemoryInfo, nvmlDeviceGetName, nvmlInit, nvmlShutdown

		nvmlInit()
		count = nvmlDeviceGetCount()
		if count > 0:
			handle = nvmlDeviceGetHandleByIndex(0)  # Premier GPU
			name_raw = nvmlDeviceGetName(handle)
			name = name_raw.decode("utf-8") if isinstance(name_raw, bytes) else name_raw
			memory = nvmlDeviceGetMemoryInfo(handle).total // (1024 * 1024)  # Taille en Mo
			metadata["GPU"] = f"{name} (Memory: {memory} MB)"
		else:
			metadata["GPU"] = "No GPU found"
		nvmlShutdown()
	# La collecte GPU facultative ne doit pas interrompre les tests.
	except Exception as e:  # noqa: BLE001
		metadata["GPU"] = f"Error detecting GPU: {e!s}"


# --------------------------------------------------
@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
	"""
	Initialise les mesures au démarrage de la session Pytest.

	:param session: Session Pytest.
	"""
	all_tests_monitoring.start(0.1)


# --------------------------------------------------
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
	"""
	Finalise et enregistre les mesures de la session Pytest.

	:param session: Session Pytest.
	:param exitstatus: Code de sortie de la session Pytest.
	"""
	all_tests_monitoring.stop()
	for ext in ["html", "json", "txt"]:
		try: all_tests_monitoring.save(f"reports/monitoring.{ext}")
		# Continuer les autres formats si une sortie de rapport échoue.
		except Exception as e: Ui.print_error(f"Unable to save monitoring in format {ext} : {e}")  # noqa: BLE001
	add_to_json("reports/test_report.json", "metadata", session.config.stash[metadata_key])


# --------------------------------------------------
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
	"""
	Enregistre l’identifiant du test avant son exécution.

	:param item: Test Pytest courant.
	:param nextitem: Test Pytest suivant, ou ``None`` ; non utilisé par ce hook.
	"""
	all_tests_monitoring.add_test_info(item.nodeid)
	return None


# --------------------------------------------------
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
	"""
	Suspend les mesures avant l’exécution d’un test Qt.

	:param item: Test Pytest courant.
	"""
	if _is_qt_test(item) and all_tests_monitoring.is_running: all_tests_monitoring.pause()


# --------------------------------------------------
@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item, nextitem):
	"""
	Reprend les mesures après le dernier test Qt consécutif.

	:param item: Test Pytest courant.
	:param nextitem: Test Pytest suivant, ou ``None``.
	"""
	if _is_qt_test(item) and not _is_qt_test(nextitem): all_tests_monitoring.resume()
# ==================================================
# endregion Hooks pytest
# ==================================================
