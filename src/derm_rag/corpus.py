from __future__ import annotations

import json
from pathlib import Path

from .models import EvidenceCard


def load_corpus(path: str | Path) -> list[EvidenceCard]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return [EvidenceCard.model_validate(item) for item in payload]
