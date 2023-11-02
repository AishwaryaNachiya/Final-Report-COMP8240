import os
import random

# Define the paths to the IMDb dataset files
dataset_dir = 'corpus/imdb'  # Replace with the actual path
output_dir = 'corpus/imdb'  # Replace with the desired output path
train_ratio = 0.7  # Percentage of data for training
dev_ratio = 0.15  # Percentage of data for development
test_ratio = 0.15  # Percentage of data for testing

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize lists for positive and negative reviews
positive_reviews = []
negative_reviews = []

# Load positive reviews from 'pos' directory
pos_dir = os.path.join(dataset_dir, 'pos')
for filename in os.listdir(pos_dir):
    with open(os.path.join(pos_dir, filename), 'r', encoding='utf-8') as file:
        review = file.read()
        positive_reviews.append(review)

# Load negative reviews from 'neg' directory
neg_dir = os.path.join(dataset_dir, 'neg')
for filename in os.listdir(neg_dir):
    with open(os.path.join(neg_dir, filename), 'r', encoding='utf-8') as file:
        review = file.read()
        negative_reviews.append(review)

# Shuffle the reviews
random.shuffle(positive_reviews)
random.shuffle(negative_reviews)

# Split the reviews into train, dev, and test sets
total_reviews = len(positive_reviews) + len(negative_reviews)
train_split = int(train_ratio * total_reviews)
dev_split = int(dev_ratio * total_reviews)

train_reviews = positive_reviews[:train_split] + negative_reviews[:train_split]
dev_reviews = positive_reviews[train_split:train_split + dev_split] + negative_reviews[train_split:train_split + dev_split]
test_reviews = positive_reviews[train_split + dev_split:] + negative_reviews[train_split + dev_split:]

# Create train, dev, and test files
with open(os.path.join(output_dir, 'imdb.train.txt.ss'), 'w', encoding='utf-8') as file:
    for review in train_reviews:
        file.write(review + '\n0\n')  # Label 0 for negative reviews

with open(os.path.join(output_dir, 'imdb.dev.txt.ss'), 'w', encoding='utf-8') as file:
    for review in dev_reviews:
        file.write(review + '\n0\n')  # Label 0 for negative reviews

with open(os.path.join(output_dir, 'imdb.test.txt.ss'), 'w', encoding='utf-8') as file:
    for review in test_reviews:
        file.write(review + '\n0\n')  # Label 0 for negative reviews
