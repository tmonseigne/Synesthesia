"""Fournit les fonctions et les constantes communes aux tests."""

from __future__ import annotations

import os
import re
from pathlib import Path

INPUT_DIR = Path(__file__).parent.resolve() / "input"
REF_DIR = INPUT_DIR / "ref"
OUTPUT_DIR = Path(__file__).parent.resolve() / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)  # Créer le dossier de sorties (la première fois, il n'existe pas)
IS_CI = os.environ.get("CI", "").lower() in {"1", "true", "yes"}
ANSI_ESCAPE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
TS_PATTERN = r"\[\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}\]"  # Regex timestamp : [16-02-2026 10:06:08]
