# fit
# transform

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

VECTORIZER_PATH = "artifacts/vectorizer.pkl"

# create TfidfVectorizer
# fit on texts
# save vectorizer.pkl
# return vectorizer
def fit_vectorizer(texts):
    #1. Create the TfidfVectorizer
    # vectorizer = TfidfVectorizer()
    vectorizer = TfidfVectorizer(
                    ngram_range=(1, 2), #(Gom cụm từ)
                    min_df=5, #(Lọc từ quá hiếm)
                    max_df=0.8, #Lọc từ quá phổ biến
                    max_features=20000 #(Giới hạn số lượng từ)
                )

    #2. Fit on texts
    vectorizer.fit(texts)

    #3. Save vectorizer.pkl
    joblib.dump(vectorizer, VECTORIZER_PATH)

    return vectorizer

def transform_text(vectorizer, texts):
    X = vectorizer.transform(texts)
    return X

def main():
    texts = [
        "quán ngon",
        "quán dở",
        "đồ ăn xuất sắc"
    ]

    vectorizer = fit_vectorizer(texts)
    X = transform_text(vectorizer, texts)

    print(type(X))
    print(X.shape)

if __name__ == "__main__":
    main()