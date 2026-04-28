from datasets import load_dataset
import pandas as pd

print("Loading dataset...")

dataset = load_dataset(
    "pqthinh232/vietnamese-restaurant-review-sentiment-dataset"
)

train = dataset["train"]

print("\n=== dataset size ===")
print("train:", len(train))

print("\n=== columns ===")
print(train.column_names)

print("\n=== first sample ===")
print(train[0])

df = pd.DataFrame(train)

print("\n=== top 5 ===")
print(df.head())

print("\n=== label count ===")
print(df["label"].value_counts())