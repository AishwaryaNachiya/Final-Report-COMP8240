import pandas as pd
import torch
import os
from transformers import BertTokenizer

# Load and preprocess the data
data_path = 'imdb.train.txt.ss'
print("Loading data...")
data = pd.read_csv(data_path, sep="\t", header=None)
data = data.dropna(subset=[0, 2])  # Drop rows where text or label is missing
print("Data loaded successfully!")

# Convert labels to tensors
print("Converting labels to tensors...")
label_data = torch.tensor(data[2].values, dtype=torch.long)
print("Labels converted!")

# Tokenize the text data
print("Starting tokenization...")
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
text_data = list(data[0].values)
text_data_tokenized = tokenizer(text_data, padding=True, truncation=True, return_tensors="pt", max_length=256)
print("Tokenization completed!")

# Ensure the directory exists before saving
output_dir = 'corpus/imdb/'
os.makedirs(output_dir, exist_ok=True)

# Save as .pt file
output_path = os.path.join(output_dir, 'train_both.pt')
print(f"Saving data to {output_path}...")
torch.save({
    'input_ids': text_data_tokenized['input_ids'],
    'attention_mask': text_data_tokenized['attention_mask'],
    'labels': label_data
}, output_path)
print("Data saved successfully!")

