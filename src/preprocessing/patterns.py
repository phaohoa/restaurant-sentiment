import re

#slang normalization
SLANG_MAP = {
    "vl": "rất",
    "vcl": "rất",
    "vc": "rất",
    "ko": "không",
    "k": "không",
    "kg": "không",
    "ok": "ổn",
    "oke": "ổn",
    "nv": "nhân_viên",
}

# 120k / 200k / 99k...
PRICE_PATTERN = re.compile(r"\b\d+\s*k\b", re.IGNORECASE)

# 2 người / 4 người
QUANTITY_PATTERN = re.compile(r"\b\d+\s*người\b", re.IGNORECASE)

# punctuation
PUNCT_PATTERN = re.compile(r"[^\w\s]", re.UNICODE)

# multiple spaces
MULTI_SPACE_PATTERN = re.compile(r"\s+")