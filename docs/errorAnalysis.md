# Error Analysis

## Error Type 1
Positive vs Neutral ambiguity

Examples:
- đồ ăn ngon vừa miệng
- đúng vị nhà làm

Cause:
Boundary between Positive and Neutral is fuzzy.

---

## Error Type 2
Mixed sentiment

Examples:
- ngon nhưng đắt
- phục vụ tốt nhưng chậm

Cause:
TF-IDF cannot model sentiment trade-offs well.

---

## Error Type 3
Short reviews

Examples:
- sẽ đặt lại
- xin sdt quán

Cause:
Not enough context.

---

## Error Type 4
Long reviews

Cause:
Many conflicting opinions in one review.