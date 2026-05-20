# 1 load vectorizer.pkl
# 2 load sentiment_model.pkl
# 3 receive input text
# 4 clean text
# 5 transform text to vector
# 6 predict sentiment
# 7 convert label -> sentiment meaning
# 8 print result

# text → clean → vectorize → predict

import joblib

from preprocessing.clean import clean_text
from vectorize import transform_text

MODEL_PATH = "model/sentiment_model.pkl"
VECTORIZER_PATH = "model/vectorizer.pkl"

def predict():
    # 1. load vectorizer.pkl (saved with joblib)
    vectorizer = joblib.load(VECTORIZER_PATH)

    # 2. load vectorizer.pkl (saved with joblib)        
    model = joblib.load(MODEL_PATH)

    # 3. receive input text
    input_text = "Đồ ăn rất ngon nhưng giá lại quá đắt :)"

    # 4 clean text
    text = clean_text(input_text)

    # 5. transform text to vector
    text_vector = transform_text(vectorizer, [text])

    # 6. predict sentiment
    prediction = model.predict(text_vector)[0]  

    # 7. convert label -> sentiment meaning
    label_mapping = {
        0: "Negative",
        1: "Neutral",
        2: "Positive"
    }

    sentiment = label_mapping.get(prediction, "Unknown")

    # 8. print result
    print(f"Original Text: {input_text}")
    print(f"Predicted Sentiment: {sentiment}")

def main():
    predict()

if __name__ == "__main__":
    main()