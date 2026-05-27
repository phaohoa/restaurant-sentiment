✓ Phase 1–8: foundation + preprocessing
✓ Phase 9: prepare_data
✓ Phase 10: vectorize refactor

Done
✓ Phase 11 — Train Baseline Model (Level A) ✅
Model: scikit-learn LogisticRegression

Mục tiêu: train được model đầu tiên predict được sentiment save model.pkl
Flow: X→Logistic Regression→y^​

Done
✓ Phase 12 — Realtime Prediction (predict.py)

Done
Phase 13 — Refactor & Project Structure

Done
Phase 14 — Improve Model Quality

Done
Phase 15 — Better Vectorization
    ngram_range=(1,2): cho phép model học cả từ đơn và cụm 2 từ
    ex: ngon
        rất ngon
        không ngon
        quá đắt
    min_df: giảm noise, giảm overfitting
    max_features: giảm kích thước feature space, tăng tốc train, giảm noise
    Đo kết quả sau mỗi thay đổi: tham số mới tốt hơn, hay chỉ là cảm giác tốt hơn

Done
Phase 16 — Error Analysis
    Model sai ở đâu?
    Tại sao sai?
    Sai theo pattern nào?

Done
Phase 17 — Better Models
    Logistic Regression:    0.8607
    Linear SVM:             0.8508
    Naive Bayes:            0.8179
Phase 20 — Deep Learning NLP