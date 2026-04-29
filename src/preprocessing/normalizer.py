from .patterns import (
    SLANG_MAP,
    PRICE_PATTERN,
    QUANTITY_PATTERN,
    MULTI_SPACE_PATTERN
)

# "Quán NGON"
# "quán ngon"
def normalize_case(text: str) -> str:
    return text.lower()

# "ngon vl"
# ["ngon", "vl"]
# ["ngon", "rất"]
# "ngon rất"
def normalize_slang(text: str) -> str:
    words = text.split()

    normalized_words = [
        SLANG_MAP.get(word, word)
        for word in words
    ]

    return " ".join(normalized_words)

# 120k -> price
def normalize_price(text: str) -> str:
    return PRICE_PATTERN.sub("price", text)

# 2 người -> quantity_people
def normalize_quantity(text: str) -> str:
    return QUANTITY_PATTERN.sub("quantity_people", text)

def normalize_spaces(text: str) -> str:
    text = MULTI_SPACE_PATTERN.sub(" ", text)
    return text.strip()