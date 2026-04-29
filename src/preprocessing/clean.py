from .patterns import PUNCT_PATTERN
from .normalizer import(
    normalize_case,
    normalize_slang,
    normalize_price,
    normalize_quantity,
    normalize_spaces
)

# Input
# Quán ngon vl 😍, giá 120k/2 người!!!
#     ↓
# normalize_case
# quán ngon vl 😍, giá 120k/2 người!!!
#     ↓
# normalize_slang
# quán ngon rất 😍, giá 120k/2 người!!!
#     ↓
# normalize_price
# quán ngon rất 😍, giá price/2 người!!!
#     ↓
# normalize_quantity
# quán ngon rất 😍, giá price/quantity_people!!!
#     ↓
# remove_punctuation
# quán ngon rất giá price quantity_people

def remove_punctuation(text: str) -> str:
    return PUNCT_PATTERN.sub(" ", text)

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    
    text = normalize_case(text)
    text = normalize_slang(text)
    text = normalize_price(text)
    text = normalize_quantity(text)
    text = remove_punctuation(text)
    text = normalize_spaces(text)

    return text