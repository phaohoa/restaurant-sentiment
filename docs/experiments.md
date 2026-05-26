# Experiment Log

## Baseline

Date: 2026-05-23

Vectorizer:

```python
TfidfVectorizer()

Accuracy: 0.8110
Initial baseline

========================

Date: 2026-05-26

Vectorizer:

```python
TfidfVectorizer(
    ngram_range=(1, 2), #(Gom cụm từ)
    min_df=2, #(Lọc từ quá hiếm)
    max_df=0.8, #Lọc từ quá phổ biến
    max_features=20000, #(Giới hạn số lượng từ)
    sublinear_tf=True
)

Accuracy: 0.8401
Initial baseline