# load cleaned csv
# extract X text
# extract y label
# fit TF-IDF
# return X, y, vectorizer
# save vectorizer.pkl

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

CSV_PATH = "data/cleaned_reviews.csv"
VECTORIZER_PATH = "model/vectorizer.pkl"


def vectorize_data():
    # 1. Load cleaned csv
    df = pd.read_csv(CSV_PATH)

    # 2. Extract X text
    X_raw = df["cleaned_review"]

    #3. Extract y label
    y = df['label']

    #4 Fit TF_IDF
    # Convert cleaned text into TF-IDF features
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(X_raw)

    # 5. Save vectorizer.pkl
    # Use joblib to store the fitted vectorizer object.
    joblib.dump(vectorizer, VECTORIZER_PATH)

    # print(type(X))
    # print(X.shape)

    return X, y, vectorizer

def main():
    vectorize_data()

if __name__ == "__main__":
    main()