import random
import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
from nltk.tokenize import word_tokenize

nltk.download('movie_reviews')
nltk.download('punkt')

def extract_features(words):
    return dict([(word, True) for word in words])

# Load movie reviews from the NLTK corpus
fileids_pos = movie_reviews.fileids('pos')
fileids_neg = movie_reviews.fileids('neg')

features_pos = [(extract_features(word_tokenize(movie_reviews.raw(fileids=[f]))), 'Positive') for f in fileids_pos]
features_neg = [(extract_features(word_tokenize(movie_reviews.raw(fileids=[f]))), 'Negative') for f in fileids_neg]

# Combine the positive and negative features
threshold = 0.8
num_pos = int(threshold * len(features_pos))
num_neg = int(threshold * len(features_neg))

# Create training and testing datasets
features_train = features_pos[:num_pos] + features_neg[:num_neg]
features_test = features_pos[num_pos:] + features_neg[num_neg:]

# Shuffle the datasets
random.shuffle(features_train)
random.shuffle(features_test)

print(f"Number of training datapoints: {len(features_train)}")
print(f"Number of test datapoints: {len(features_test)}")


# Train a Naive Bayes classifier
classifier = NaiveBayesClassifier.train(features_train)
print('\nAccuracy of the classifier:', nltk_accuracy(classifier, features_test))

# Output the most informative features
print('\nTop 10 most informative words:')
for item in classifier.most_informative_features()[:10]:
    print(item[0])

# Test input sentences
input_sentences = [
    "The movie was amazing and I loved it!",
    "The movie was dull and boring.",
    "It was a fantastic performance!",
    "I did not like the movie, but it was okay."
]

print("\nMovie review predictions:")
for sentence in input_sentences:
    words = word_tokenize(sentence)
    features = extract_features(words)
    print(f"Sentiment: {classifier.classify(features)} - Sentence: {sentence}")


# Test input sentences
input_sentences = [
    "The movie was amazing and I loved it!",
    "The movie was dull and boring.",
    "It was a fantastic performance!",
    "I did not like the movie, but it was okay."
]

print("\nMovie review predictions:")
for sentence in input_sentences:
    words = word_tokenize(sentence)
    features = extract_features(words)
    print(f"Sentiment: {classifier.classify(features)} - Sentence: {sentence}")

