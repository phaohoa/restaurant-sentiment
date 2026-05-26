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
    
Phase 16 — Error Analysis
Phase 17 — Interactive CLI App
Phase 18 — REST API
Phase 19 — Frontend Demo
Phase 20 — Deep Learning NLP