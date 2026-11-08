import unicodedata
import re
import logging
from typing import Tuple, Dict, Any

logger = logging.getLogger(__name__)

class InputNormalizer:
    def __init__(
        self, 
        normalize_unicode: bool = True,
        strip_control_chars: bool = True,
        collapse_whitespace: bool = True,
        detect_injections: bool = True,
        max_length: int = 4000
    ):
        self.normalize_unicode = normalize_unicode
        self.strip_control_chars = strip_control_chars
        self.collapse_whitespace = collapse_whitespace
        self.detect_injections = detect_injections
        self.max_length = max_length

        self.injection_patterns = [
            r"ignore\s+(all\s+)?previous\s+instructions",
            r"system\s*:\s*override",
            r"you\s+are\s+now\s+(in\s+)?developer\s+mode",
            r"disregard\s+above",
            r"reveal\s+system\s+prompt"
        ]

    def normalize(self, text: str) -> Tuple[str, Dict[str, Any]]:
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        metadata = {
            "original_length": len(text),
            "flagged_injection": False,
            "matched_patterns": [],
            "truncated": False
        }

        if self.normalize_unicode:
            text = unicodedata.normalize('NFKC', text)
            
        if self.strip_control_chars:
            text = re.sub(r'[\u200b-\u200d\uFEFF\x00-\x1f\x7f-\x9f]', '', text)
            
        if self.collapse_whitespace:
            text = re.sub(r'[ \t]+', ' ', text)
            text = re.sub(r'\n\s*\n', '\n\n', text).strip()

        if self.detect_injections:
            lower_text = text.lower()
            for pattern in self.injection_patterns:
                if re.search(pattern, lower_text):
                    metadata["flagged_injection"] = True
                    metadata["matched_patterns"].append(pattern)

        if self.max_length and len(text) > self.max_length:
            metadata["truncated"] = True
            text = text[:self.max_length]

        metadata["final_length"] = len(text)
        return text, metadata
