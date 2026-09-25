"""
Génère les diagrammes de classes synthétiques de la documentation.

La structure des classes et leurs relations sont extraites avec :mod:`pyreverse`.
Les cartouches sont volontairement limités aux noms des classes afin de conserver une vue lisible de l'architecture.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent.parent
MODULE_PATH = ROOT_PATH / "synesthesia"
GRAPH_PATH = ROOT_PATH / "docs" / "_static" / "graph"

NODE_PATTERN = re.compile(r'^"(?P<identifier>[^"]+)" \[')
EDGE_PATTERN = re.compile(r'^"(?P<source>[^"]+)" -> "(?P<target>[^"]+)" (?P<attributes>\[.*\]);$')


# ==================================================
# region Configuration
# ==================================================
##################################################
@dataclass(frozen=True)
class Diagram:
	"""
	Décrit un diagramme de classes à produire.

	:param name: Nom interne du graphe Graphviz.
	:param filename: Nom du fichier DOT produit.
	:param fill_color: Couleur de fond des classes.
	:param edge_rank_cycle: Nombre de niveaux utilisés pour étager les relations.
	:param contains: Prédicat indiquant si une classe appartient au diagramme.
	"""

	name: str
	"""Nom interne du graphe Graphviz."""
	filename: str
	"""Nom du fichier DOT produit."""
	fill_color: str
	"""Couleur de fond des classes."""
	edge_rank_cycle: int
	"""Nombre de niveaux utilisés pour étager les relations."""
	contains: Callable[[str], bool]
	"""Prédicat indiquant si une classe appartient au diagramme."""


# Exemple de Diagrams possibles
# DIAGRAMS = (Diagram(name="classes_synesthesia", filename="classes_synesthesia.dot", fill_color="#e6e6ac",
# 					edge_rank_cycle=1, contains=lambda identifier: ".Settings.Groups." not in identifier and ".Settings.Types." not in identifier),
# 			Diagram(name="classes_groups", filename="classes_groups.dot", fill_color="#e6ace6",
# 					edge_rank_cycle=4, contains=lambda identifier: ".Settings.Groups." in identifier),
# 			Diagram(name="classes_types", filename="classes_types.dot", fill_color="#acace6",
# 					edge_rank_cycle=4, contains=lambda identifier: ".Settings.Types." in identifier),)
DIAGRAMS = (Diagram(name="classes_synesthesia", filename="classes_synesthesia.dot", fill_color="#e6e6ac", edge_rank_cycle=1, contains=lambda identifier: True),)

EXCLUDED_CLASSES = {"synesthesia.Tools.Monitoring.Monitoring", }


# Relations structurelles non détectées ou mal qualifiées par pyreverse.
# MANUAL_EDGES = ( )

# ==================================================
# endregion Configuration
# ==================================================

# ==================================================
# region Extraction
# ==================================================
##################################################
def _run_pyreverse(output_directory: Path) -> Path:
	"""
	Exécute pyreverse et retourne le chemin du diagramme DOT brut.

	:param output_directory: Répertoire temporaire de sortie.
	:return: Chemin du diagramme brut.
	:raises RuntimeError: Si pyreverse est absent ou si sa génération échoue.
	"""
	pyreverse = shutil.which("pyreverse")
	if pyreverse is None:
		raise RuntimeError("La commande 'pyreverse' est introuvable. Installez pylint pour générer les diagrammes.")

	command = [pyreverse, "--only-classnames", "--project", "synesthesia", "--output", "dot",
			   "--output-directory", str(output_directory), "--ignore", "_tests", str(MODULE_PATH)]
	result = subprocess.run(command, cwd=ROOT_PATH, check=False, capture_output=True, text=True)
	if result.returncode != 0:
		details = result.stderr.strip() or result.stdout.strip() or "erreur inconnue"
		raise RuntimeError(f"La génération pyreverse a échoué : {details}")

	output_path = output_directory / "classes_synesthesia.dot"
	if not output_path.is_file(): raise RuntimeError(f"pyreverse n'a pas produit le fichier attendu : {output_path}")
	return output_path


##################################################
def _is_architectural_class(identifier: str) -> bool:
	"""
	Indique si une classe doit apparaître dans les diagrammes d'architecture.

	:param identifier: Nom pleinement qualifié de la classe.
	:return: ``True`` pour une classe publique utile à la vue architecturale.
	"""
	class_name = identifier.rsplit(".", maxsplit=1)[-1]
	return "._tests." not in identifier and not class_name.startswith("_") and identifier not in EXCLUDED_CLASSES


##################################################
def _read_graph(raw_graph_path: Path) -> tuple[set[str], list[tuple[str, str, str]]]:
	"""
	Extrait les classes et relations du graphe produit par pyreverse.

	:param raw_graph_path: Chemin du fichier DOT brut.
	:return: Identifiants de classes et relations ``(source, cible, attributs)``.
	"""
	nodes: set[str] = set()
	edges: list[tuple[str, str, str]] = []
	for line in raw_graph_path.read_text(encoding="utf-8").splitlines():
		if edge_match := EDGE_PATTERN.match(line): edges.append((edge_match["source"], edge_match["target"], edge_match["attributes"]))
		elif node_match := NODE_PATTERN.match(line): nodes.add(node_match["identifier"])
	return nodes, edges


# ==================================================
# endregion Extraction
# ==================================================

# ==================================================
# region Génération
# ==================================================
##################################################
def _normalize_edge_attributes(attributes: str, min_length: int) -> str:
	"""
	Uniformise les attributs d'une relation produite par pyreverse.

	La longueur de rang est alternée pour répartir les nombreuses classes sœurs sur	plusieurs niveaux et éviter un diagramme excessivement horizontal.

	:param attributes: Liste d'attributs Graphviz entre crochets.
	:param min_length: Longueur minimale de la relation, en rangs Graphviz.
	:return: Liste d'attributs normalisée.
	"""
	normalized = attributes.replace('fontcolor="green"', 'fontcolor="#006400"').replace(', style="solid"', "")
	return f'{normalized[:-1]}, minlen="{min_length}"]'


##################################################
def _render_diagram(diagram: Diagram, nodes: set[str], edges: list[tuple[str, str, str]]) -> str:
	"""
	Construit le contenu DOT d'un diagramme synthétique.

	:param diagram: Configuration du diagramme.
	:param nodes: Classes détectées par pyreverse.
	:param edges: Relations détectées par pyreverse.
	:return: Contenu DOT terminé par un saut de ligne.
	"""
	diagram_nodes = {identifier for identifier in nodes if _is_architectural_class(identifier) and diagram.contains(identifier)}
	diagram_edges = sorted((source, target, attributes) for source, target, attributes in edges if source in diagram_nodes and target in diagram_nodes)

	lines = [f'digraph "{diagram.name}" {{',
			 'graph [bgcolor="transparent", nodesep="0.35", pad="0.2", rankdir="BT", ranksep="0.7"];',
			 f'node [color="#4a4a4a", fillcolor="{diagram.fill_color}", fontcolor="black", fontname="Helvetica", '
			 f'fontsize="10", shape="box", style="filled,rounded"];',
			 'edge [color="#666666", fontcolor="#006400", fontname="Helvetica", fontsize="9"];',
			 ""]
	for identifier in sorted(diagram_nodes, key=lambda item: (item.rsplit(".", maxsplit=1)[-1].casefold(), item.casefold())):
		class_name = identifier.rsplit(".", maxsplit=1)[-1]
		lines.append(f'"{identifier}" [label="{class_name}"];')

	if diagram_edges:
		lines.append("")
		for index, (source, target, attributes) in enumerate(diagram_edges):
			min_length = index % diagram.edge_rank_cycle + 1
			lines.append(f'"{source}" -> "{target}" {_normalize_edge_attributes(attributes, min_length)};')

	connected_nodes = {identifier for source, target, _ in diagram_edges for identifier in (source, target)}
	isolated_nodes = sorted(diagram_nodes - connected_nodes, key=str.casefold)
	if len(isolated_nodes) > 1:
		lines.extend(("", "// Contraintes invisibles limitant la largeur des classes isolées."))
		chain_count = max(1, (len(isolated_nodes) + 6) // 7)
		chain_length = (len(isolated_nodes) + chain_count - 1) // chain_count
		for index in range(len(isolated_nodes) - 1):
			if (index + 1) % chain_length != 0:
				lines.append(f'"{isolated_nodes[index]}" -> "{isolated_nodes[index + 1]}" [style="invis"];')

	lines.append("}")
	return "\n".join(lines) + "\n"


##################################################
def generate_class_diagrams() -> None:
	"""Génère les trois diagrammes de classes utilisés par Sphinx."""
	GRAPH_PATH.mkdir(parents=True, exist_ok=True)
	with tempfile.TemporaryDirectory(prefix="synesthesia-pyreverse-") as temporary_directory:
		raw_graph_path = _run_pyreverse(Path(temporary_directory))
		nodes, edges = _read_graph(raw_graph_path)

	# manual_relations = {frozenset((source, target)) for source, target, _ in MANUAL_EDGES}
	# edges = [edge for edge in edges if frozenset(edge[:2]) not in manual_relations]
	# edges.extend(MANUAL_EDGES)

	for diagram in DIAGRAMS:
		output_path = GRAPH_PATH / diagram.filename
		with output_path.open("w", encoding="utf-8", newline="\n") as output_file: output_file.write(_render_diagram(diagram, nodes, edges))


# ==================================================
# endregion Génération
# ==================================================

##################################################
if __name__ == "__main__":
	generate_class_diagrams()
	print(f"Diagrammes de classes générés dans : {GRAPH_PATH}")
