import pickle
import nltk
import sys

Classifier = pickle.load(open("classifier.p", "rb"))
word_features = pickle.load(open("word_features.p", "rb"))

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
	print classify(sys.argv[1])