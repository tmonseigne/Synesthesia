"""Configure les fixtures et les hooks Pytest communs à la suite de tests."""

import json
import os
import platform

import cpuinfo
import psutil
import pytest
from pytest_metadata.plugin import metadata_key

from synesthesia.Tools import Monitoring, Ui

os.environ["QT_QPA_PLATFORM"] = "offscreen"
os.environ["QT_OPENGL"] = "software"
os.environ["NAPARI_GUI_BACKEND"] = "none"
os.environ["VISPY_USE_APP"] = "mock"

all_tests_monitoring = Monitoring()


# ==================================================
# region Hooks pytest
# ==================================================
##################################################
def _is_qt_test(item) -> bool:
	"""Indique si le test utilise Qt ou Napari."""
	if item is None: return False
	fixture_names = set(getattr(item, "fixturenames", []))
	keywords = set(item.keywords)
	nodeid = str(getattr(item, "nodeid", "")).lower()
	return bool({"qtbot"} & fixture_names or {"qt"} & keywords or "qt" in nodeid or "gui" in nodeid)


##################################################
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
	except Exception: cores = threads = os.cpu_count()

	try:  # En cas de problème notamment sur mac
		freq = f"Unknown frequency"
		if hasattr(psutil, "cpu_freq"):
			cpu_info = psutil.cpu_freq(percpu=False)
			if cpu_info and getattr(cpu_info, "current", None): freq = f"{cpu_info.current / 1000:.2f} GHz"
		res += f" ({freq} - {cores} Cores ({threads} Logical))"
	except RuntimeError: res += "(No CPU Infos)"
	return res


##################################################
def add_to_json(path, datas_name, datas):
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


##################################################
# Fonction pour configurer les métadonnées du rapport
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

	## Ajout de la carte graphique si disponible
	try:
		from pynvml import nvmlInit, nvmlShutdown, nvmlDeviceGetHandleByIndex, nvmlDeviceGetName, nvmlDeviceGetMemoryInfo, nvmlDeviceGetCount

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
	except Exception as e:
		metadata["GPU"] = f"Error detecting GPU: {str(e)}"


##################################################
@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
	"""
	Initialise les mesures au démarrage de la session Pytest.

	:param session: Session Pytest.
	"""
	global all_tests_monitoring
	all_tests_monitoring.start(0.1)


##################################################
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
	"""
	Finalise et enregistre les mesures de la session Pytest.

	:param session: Session Pytest.
	:param exitstatus: Code de sortie de la session Pytest.
	"""
	global all_tests_monitoring
	all_tests_monitoring.stop()
	for ext in ["html", "json", "txt"]:
		try: all_tests_monitoring.save(f"reports/monitoring.{ext}")
		except Exception as e: Ui.print_error(f"Unable to save monitoring in format {ext} : {e}")
	add_to_json("reports/test_report.json", "metadata", session.config.stash[metadata_key])


##################################################
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
	"""Capture les informations sur chaque test."""
	global all_tests_monitoring
	all_tests_monitoring.add_test_info(item.nodeid)
	return None


##################################################
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
	"""À l'initialisation de chaque test."""
	global all_tests_monitoring
	if _is_qt_test(item) and all_tests_monitoring.is_running: all_tests_monitoring.pause()


##################################################
@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item, nextitem):
	"""Au nettoyage de chaque test."""
	global all_tests_monitoring
	if _is_qt_test(item) and not _is_qt_test(nextitem): all_tests_monitoring.resume()
# ==================================================
# endregion Hooks pytest
# ==================================================
