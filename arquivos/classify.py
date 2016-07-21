import pickle
import nltk
import sys
import os

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

Classifier = pickle.load(open(os.path.join(PROJECT_ROOT, "arquivos/classifier.p"), "rb"))
word_features = pickle.load(open(os.path.join(PROJECT_ROOT, "arquivos/word_features.p"), "rb"))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

# tweet = "some string"
def classify(tweet):
	return Classifier.classify(extract_features(tweet.split()))

if __name__ == "__main__":
	classify(sys.argv[1])