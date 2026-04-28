from datasets import load_dataset
import pandas as pd

dataset = load_dataset(
    "pqthinh232/vietnamese-restaurant-review-sentiment-dataset"
)

df = pd.DataFrame(dataset["train"])

for label in [0, 1, 2]:
    print(f"\n===== LABEL {label} =====")
    samples = df[df["label"] == label]["review"].head(3)

    for i, text in enumerate(samples, 1):
        print(f"\n{i}. {text[:300]}...")