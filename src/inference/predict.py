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
from src.preprocessing.clean import clean_text
from src.vectorize import transform_text

# Định nghĩa đường dẫn
MODEL_PATH = "artifacts/sentiment_model.pkl"
VECTORIZER_PATH = "artifacts/vectorizer.pkl"

# 1 & 2. Load model và vectorizer một lần duy nhất ở ngoài (Global)
# Giúp tiết kiệm tài nguyên khi chạy thực tế hoặc làm API sau này
try:
    print("Loading models...")
    vectorizer = joblib.load(VECTORIZER_PATH)
    model = joblib.load(MODEL_PATH)
    print("Models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")

def predict_sentiment(input_text: str):
    """
    Hàm nhận vào text thô và trả về kết quả dự đoán sentiment
    """
    # 4. Clean text
    cleaned_text = clean_text(input_text)

    # 5. Transform text to vector (Bọc trong list [cleaned_text] vì model nhận ma trận)
    text_vector = transform_text(vectorizer, [cleaned_text])

    # 6. Predict sentiment label
    prediction = model.predict(text_vector)[0]  

    # 7. Convert label -> sentiment meaning (ĐÃ SỬA KHỚP VỚI TẬP TRAIN)
    label_mapping = {
        0: "Negative",
        1: "Positive",
        2: "Neutral"
    }

    return label_mapping.get(prediction, "Unknown")

def main():
    # 3. Nhận input text
    test_sentences = [
        "Đồ ăn rất ngon",
        "Phục vụ quá tệ, đồ ăn nguội ngắt",
        "Cũng bình thường, không có gì đặc sắc"
    ]
    
    # Chạy dự đoán
    print("\n--- Test Results ---")
    for text in test_sentences:
        result = predict_sentiment(text)
         # 8. Print result
        print("-" * 30)
        print(f"Original Text:  {text}")
        print(f"Predicted Sign: {result}")
        print("-" * 30) 

if __name__ == "__main__":
    main()