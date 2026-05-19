# fit
# transform

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

VECTORIZER_PATH = "model/vectorizer.pkl"

# create TfidfVectorizer
# fit on texts
# save vectorizer.pkl
# return vectorizer
def fit_vectorizer(texts):
    #1. Create the TfidfVectorizer
    vectorizer = TfidfVectorizer()

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