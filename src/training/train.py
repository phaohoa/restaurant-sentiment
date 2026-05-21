# 1 load cleaned csv
# 2 extract X_raw / y
# 3 split train / test
# 4 fit vectorizer on X_train_raw
# 5 transform X_train
# 6 transform X_test
# 7 train Logistic Regression
# 8 evaluate
# 9 save model

import pandas as pd
from sklearn.model_selection import train_test_split
from src.vectorize import fit_vectorizer, transform_text
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

CSV_PATH = "data/cleaned_reviews.csv"
MODEL_PATH = "artifacts/sentiment_model.pkl"

def train():
    # 1. load cleaned csv
    df = pd.read_csv(CSV_PATH) 

    # 2. extract X_raw / y
    X_raw = df['cleaned_review']
    y = df['label']

    # 3. split train / test
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        X_raw, y, test_size=0.2, random_state=42
    )

    # 4 fit vectorizer on X_train_raw
    vectorizer = fit_vectorizer(X_train_raw)

    # 5. transform X_train
    X_train = transform_text(vectorizer, X_train_raw)

    # 6. transform X_test
    X_test = transform_text(vectorizer, X_test_raw)

    # 7. train Logistic Regression
    model = LogisticRegression(class_weight='balanced')
    model.fit(X_train, y_train)

    # 8 evaluate
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # 9. save model
    joblib.dump(model, MODEL_PATH)

def main():
    train()

if __name__ == "__main__":
    main()