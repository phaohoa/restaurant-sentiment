Full Flows

dataset → preprocessing → vectorization → training → evaluation → inference

| ML Stage      | File                                             |
| ------------- | ------------------------------------------------ |
| dataset       | `src/data/load_data.py`                          |
| preprocessing | `src/preprocessing/prepare_data.py` + `clean.py` |
| vectorization | `src/vectorize.py`                               |
| training      | `src/training/train.py`                          |
| evaluation    | `src/training/train.py`                          |
| inference     | `src/inference/predict.py`                       |

dataset 
    load HuggingFace dataset
Preprocessing
    raw text
    → cleaned text
    OUTPUT: cleaned_reviews.csv
Vectorization
    text→TFIDF vectors
    OUTPUT: artifacts/vectorizer.pkl
Training
    train LogisticRegression
    OUTPUT: artifacts/sentiment_model.pkl
Evaluation
    accuracy
    classification_report
Inference
    predict sentiment for new text

execution order
===============================================
python -m src.preprocessing.prepare_data    ===
python -m src.training.train                ===
python -m src.inference.predict             ===
===============================================
===============================================
internally
Train phase
    vectorize.py
Preprocessing phase
    clean.py