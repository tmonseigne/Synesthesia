"""Fournit les utilitaires d'interface."""

from __future__ import annotations

from colorama import Fore, Style


# ==================================================
# region Affichages
# ==================================================
##################################################
def print_error(msg: str):
	"""
	Affiche un message avec une couleur rouge.

	:param msg: Message à afficher.
	"""
	print(Fore.RED + Style.BRIGHT + msg + Fore.RESET + Style.RESET_ALL)


##################################################
def print_warning(msg: str):
	"""
	Affiche un message avec une couleur jaune.

	:param msg: Message à afficher.
	"""
	print(Fore.YELLOW + Style.BRIGHT + msg + Fore.RESET + Style.RESET_ALL)


##################################################
def print_success(msg: str):
	"""
	Affiche un message avec une couleur verte.

	:param msg: Message à afficher.
	"""
	print(Fore.GREEN + Style.BRIGHT + msg + Fore.RESET + Style.RESET_ALL)


##################################################
def format_time(seconds):
	"""
	Fonction pour formater le temps en secondes en HH:MM:SS.

	:param seconds: Temps en secondes.
	:return: Chaîne de caractère représentant le temps au format HH:MM:SS.
	"""
	hours = int(seconds // 3600)
	minutes = int((seconds % 3600) // 60)
	seconds = int(seconds % 60)
	return f"{hours:02}:{minutes:02}:{seconds:02}"
# ==================================================
# endregion Affichages
# ==================================================
