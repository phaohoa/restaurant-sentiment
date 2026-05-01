from datasets import load_dataset
import pandas as pd

def load_data():
    dataset = load_dataset(
        "pqthinh232/vietnamese-restaurant-review-sentiment-dataset"
    )
    train = dataset["train"]

    df = pd.DataFrame(train)
    return df

def main():
    print("Loading dataset...")

    df = load_data()

    print("\n=== dataset size ===")
    print("rows:", len(df))

    print("\n=== columns ===")
    print(df.columns)

    print("\n=== first sample ===")
    print(df.iloc[0])

    

    print("\n=== top 5 ===")
    print(df.head())

    print("\n=== label count ===")
    print(df["label"].value_counts())


if __name__ == "__main__":
    main()