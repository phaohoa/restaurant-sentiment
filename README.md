# Restaurant Sentiment Analysis Project

## 🎯 Mục tiêu
Xây dựng hệ thống phân tích cảm xúc (Sentiment Analysis) cho review nhà hàng.

Input:
> "đồ ăn ngon nhưng phục vụ chậm"

Output:
> Negative (68%)

---

# 🧭 Tổng quan pipeline

Raw Text
↓
Cleaning
↓
Vectorization (TF-IDF)
↓
Model (Logistic Regression)
↓
Prediction
↓
Dashboard


---

# 📌 Tiến độ hiện tại
[✓] Setup môi trường
[✓] Load dataset
[✓] Hiểu dataset
[ ] Clean text
[ ] Feature Engineering
[ ] Train model
[ ] Evaluation
[ ] Deploy app


👉 Progress: ~30%

---

# 📂 Cấu trúc project
restaurant-sentiment/
│
├── data/
├── src/
│ ├── load_data.py
│ ├── clean.py
│ ├── train.py
│ └── predict.py
│
├── model/
├── app/
└── README.md


---

# 🧱 Các bước cần làm

## 1. Load Data ✅

- Dùng Hugging Face dataset
- Convert sang pandas DataFrame

---

## 2. Understand Data ✅

Dataset gồm:

- review_id
- review (text)
- label (sentiment)

Mapping:
0 = Negative
1 = Positive
2 = Neutral


---

## 3. Data Cleaning ⏳

Mục tiêu:
- Làm sạch text

Cần làm:

- lowercase
- remove emoji
- remove punctuation
- remove number
- remove extra spaces

Ví dụ:

Before:
quán ngon vl 😍

After:
quán ngon


---

## 4. Feature Engineering ⏳

Biến text thành số bằng TF-IDF.

Ví dụ:
"ngon" → vector số


---

## 5. Train Model ⏳

Sử dụng:

- Logistic Regression hoặc Linear SVM

Quy trình:
X = TF-IDF(text)
y = label

model.fit(X, y)


---

## 6. Evaluation ⏳

Đánh giá model:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

## 7. Prediction ⏳

Input:
text mới

Output:
label + confidence


---

## 8. Deployment ⏳

Dùng Streamlit:

- textbox nhập review
- nút Analyze
- hiển thị kết quả
- biểu đồ sentiment

---

# 🗓️ Kế hoạch học (6 buổi)

## Buổi 1
- Setup + Load data ✅

## Buổi 2
- Clean text

## Buổi 3
- TF-IDF

## Buổi 4
- Train model

## Buổi 5
- Evaluate

## Buổi 6
- Build app

---

# 🧠 Ghi nhớ quan trọng

- AI = data + pattern
- Model không hiểu chữ → chỉ hiểu số
- Dataset quan trọng hơn model

---

# 🚀 Next Step

👉 Làm bước: **Data Cleaning**
