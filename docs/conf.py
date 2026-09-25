"""Configure la génération de la documentation avec Sphinx."""

from __future__ import annotations

# ----- Gestion des fichiers à ajouter ----------------------------------------
import shutil
import sys
from pathlib import Path

# ----- Commandes -------------------------------------------------------------
# python -m pytest;
# python ./docs/tools/pytest_json_to_rst.py ./reports/test_report.json ./docs/reports/test_report.rst;
# cp ./reports/monitoring.html ./docs/reports/monitoring.html;
# python.exe .\docs\tools\generate_api_files.py;
# sphinx-build -b html -D language=fr docs docs/_build/html; sphinx-build -b html -D language=en docs docs/_build/html/en;
# sphinx-build -b gettext docs/ docs/_build/gettext; sphinx-intl update -p docs/_build/gettext -d docs/locale -l en -w 0;


# Ajout du chemin vers le dossier synesthesia
root = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(root), str(root / "synesthesia")]

project = "Synesthesia"
copyright = "2026, Thibaut Monseigne"
author = "Thibaut Monseigne"
language = "fr"

# ----- General configuration -------------------------------------------------

extensions = [
		"sphinx.ext.autodoc",
		"sphinx.ext.autosummary",
		"sphinx.ext.autosectionlabel",
		"sphinx.ext.intersphinx",
		"sphinx.ext.mathjax",
		"sphinx.ext.napoleon",
		"sphinx.ext.todo",
		"sphinx.ext.viewcode",
		"sphinx.ext.graphviz",
		"sphinx_copybutton",
		"sphinxcontrib.bibtex",
		"sphinxcontrib.jquery",
		"sphinx_qt_documentation",
		"sphinx_design",
		]

bibtex_bibfiles = ["references.bib"]
bibtex_reference_style = "author_year"
bibtex_default_style = "unsrtalpha"

autodoc_typehints = "both"
graphviz_output_format = "svg"

intersphinx_mapping = {
		"python":       ("https://docs.python.org/3", None),
		"numpy":        ("https://numpy.org/doc/stable", None),
		"plotly":       ("https://plotly.com/python-api-reference/", None),
		"psutil":       ("https://psutil.readthedocs.io/en/stable/", None),
		"pytest":       ("https://docs.pytest.org/en/latest/", None),
		"pytest-cov":   ("https://pytest-cov.readthedocs.io/en/latest/", None),
		"pytest-qt":    ("https://pytest-qt.readthedocs.io/en/latest/", None),
		"sphinx":       ("https://www.sphinx-doc.org/en/master/", None),
		}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# ----- Options for HTML output -----------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
# html_favicon = "_static/favicon.ico"
html_context = {"allow_html_in_rst": True}  # Autoriser l'inclusion de contenu HTML brut

# ----- Automatisation --------------------------------------------------------

autosummary_generate = False  # .			Évite des arborescences trop profondes et des liens internes vers de nouvelles pages
autodoc_member_order = "bysource"  # .		Évite le tri alphabétique
add_module_names = False  # .				Évite le nom des modules parents au début des objets
toc_object_entries_show_parents = "hide"  # Évite le nom des modules parents au début des objets dans l'arborescence
todo_include_todos = True
python_use_unqualified_type_names = True  # Évite le nom des modules parents au début des objets

suppress_warnings = ["autosectionlabel.*"]

# ----- Multilingue -----------------------------------------------------------
locale_dirs = ["locale/"]
gettext_compact = False


def copy_dir(src: str | Path, dst: str | Path) -> None:
	"""Copie récursivement un dossier source vers un dossier destination."""
	src, dst = Path(src), Path(dst)
	if not src.exists(): return  # .				 Copie les fichiers si le dossier source existe
	dst.mkdir(parents=True, exist_ok=True)  # .		 Crée le dossier de destination s'il n'existe pas
	shutil.copytree(src, dst, dirs_exist_ok=True)  # Copie récursivement les fichiers du dossier source vers le dossier de destination.


copy_dir("reports", "_build/html/reports")
copy_dir("reports", "_build/html/en/reports")

default_language_code = "fr"

languages = [("Français", "fr"), ("English", "en")]


def setup(app):
	"""Ajoute des variables de contexte HTML (Jinja) en fonction de la langue réellement utilisée."""

	def _inject_context(app_, pagename, templatename, context, doctree):
		"""
		Ajoute les informations de langue au contexte du gabarit.

		:param app_: Application Sphinx.
		:param pagename: Nom de la page générée.
		:param templatename: Nom du gabarit.
		:param context: Contexte transmis au gabarit.
		:param doctree: Arbre documentaire de la page.
		"""
		cur = app_.config.language or default_language_code
		context["default_language_code"] = default_language_code
		context["current_language_code"] = cur
		context["languages"] = languages

	app.connect("html-page-context", _inject_context)
