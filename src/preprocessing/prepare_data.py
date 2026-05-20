from src.data.load_data import load_data
from src.preprocessing.clean import clean_text

OUTPUT_PATH = "data/cleaned_reviews.csv"

def prepare_data():
    df = load_data()
    # Create cleaned text column for training
    # pandas apply
    df["cleaned_review"] = df["review"].apply(clean_text)

    return df

def main():
    print("Phase 9 — Prepare Dataset.")
    df = prepare_data()
    df.to_csv(OUTPUT_PATH, index=False)

if __name__ == "__main__":
    main()