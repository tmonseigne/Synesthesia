"""Met à jour la table des matières des rapports de tests."""

from __future__ import annotations

from pathlib import Path


# --------------------------------------------------
def generate_toctree_rst(dst: str = "tests.rst"):
	"""
	Génère la table des matières des rapports de tests.

	Inclut le rapport de la machine principale et les rapports ``test_report_ci_*.rst`` présents dans ``docs/reports``.

	:param dst: Chemin du fichier de sortie relatif au dossier ``docs``.
	"""

	docs_path = Path("docs")
	reports_path = docs_path / "reports"  # Répertoire contenant les fichiers .rst
	pattern = "test_report_ci_"  # .		Modèle pour les fichiers à inclure

	# Recherche des fichiers correspondants
	files = sorted(f for f in reports_path.glob(f"{pattern}*.rst"))

	# Génération du contenu du fichier .rst
	content = ("Tests\n"
			   "=====\n\n"
			   "Liste des rapports de tests générés :\n\n"
			   ".. toctree::\n"
			   "   :maxdepth: 1\n\n"
			   "   reports/test_report\n")

	for f in files: content += f"   reports/{f.stem}\n"

	# Écriture dans le fichier de sortie
	output_file = docs_path / dst
	output_file.write_text(content, encoding="utf-8")
	print(f"{dst} generated successfully.")


# --------------------------------------------------
if __name__ == "__main__": generate_toctree_rst()
