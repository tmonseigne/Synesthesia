"""Fournit les utilitaires d'interface."""

from __future__ import annotations

from colorama import Fore, Style


# ==================================================
# region Affichages
# ==================================================
def print_error(msg: str):
	"""
	Affiche un message avec une couleur rouge.

	:param msg: Message à afficher.
	"""
	print(Fore.RED + Style.BRIGHT + msg + Fore.RESET + Style.RESET_ALL)


# --------------------------------------------------
def print_warning(msg: str):
	"""
	Affiche un message avec une couleur jaune.

	:param msg: Message à afficher.
	"""
	print(Fore.YELLOW + Style.BRIGHT + msg + Fore.RESET + Style.RESET_ALL)


# --------------------------------------------------
def print_success(msg: str):
	"""
	Affiche un message avec une couleur verte.

	:param msg: Message à afficher.
	"""
	print(Fore.GREEN + Style.BRIGHT + msg + Fore.RESET + Style.RESET_ALL)


# --------------------------------------------------
def format_time(seconds: float) -> str:
	"""
	Formate une durée en heures, minutes et secondes.

	Les fractions de seconde sont tronquées ; le nombre d’heures peut dépasser 23.

	:param seconds: Durée en secondes.
	:return: Durée au format ``HH:MM:SS``.
	"""
	hours = int(seconds // 3600)
	minutes = int((seconds % 3600) // 60)
	seconds = int(seconds % 60)
	return f"{hours:02}:{minutes:02}:{seconds:02}"
# ==================================================
# endregion Affichages
# ==================================================
