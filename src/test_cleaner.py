from preprocessing.clean import clean_text
sample = "Quán ngon vl 😍, giá 120k/2 người!!!"

result = clean_text(sample)

print("INPUT :", sample)
print("OUTPUT:", result)