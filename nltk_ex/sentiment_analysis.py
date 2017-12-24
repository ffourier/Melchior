#!/usr/local/bin/python3.6

import nltk
import random
import pickle

testing_set_f = open("testing_set.pickle", "rb")
testing_set = pickle.load(testing_set_f)
testing_set_f.close()

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Classifier accuracy percent: ", (nltk.classify.accuracy(classifier, testing_set)) * 100)

classifier.show_most_informative_features(15)

