"""Teste les utilitaires d'interface."""

import pytest

from synesthesia.Tools import Ui


# ==================================================
# region Affichages
# ==================================================
##################################################
@pytest.mark.parametrize("printer, message", [
		pytest.param(Ui.print_error, "Message d'erreur", id="error"),
		pytest.param(Ui.print_warning, "Message d'avertissement", id="warning"),
		pytest.param(Ui.print_success, "Message de succès", id="success")])
def test_print_message(capsys, printer, message):
	"""Vérifie que chaque fonction affiche le message demandé."""
	printer(message)
	captured = capsys.readouterr()
	assert message in captured.out
	assert captured.out.endswith("\n")
	assert captured.err == ""


##################################################
@pytest.mark.parametrize("seconds, expected", [
		pytest.param(0, "00:00:00", id="zero-duration"),
		pytest.param(59, "00:00:59", id="seconds"),
		pytest.param(60, "00:01:00", id="minute-boundary"),
		pytest.param(3666, "01:01:06", id="hours-minutes-seconds")])
def test_format_time(seconds, expected):
	"""Vérifie le format heures, minutes et secondes de la durée."""
	assert Ui.format_time(seconds) == expected

# ==================================================
# endregion Affichages
# ==================================================
