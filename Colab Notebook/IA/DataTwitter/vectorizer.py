import pickle
import re
import os
from vectorizer import vect  # archivo vectorizer.py 
clf = pickle.load(open(os.path.join('/content/twitterclassifier/pkl_objects', 'classifier.pkl'), 'rb'))