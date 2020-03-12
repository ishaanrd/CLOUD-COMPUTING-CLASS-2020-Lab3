import json
import re
import nltk
import operator
from collections import Counter
from nltk.corpus import stopwords
import string
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (6,6)
import matplotlib.pyplot as plt

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


with open('ArtificialIntelligenceTweets.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = preprocess(tweet)
        print(tokens)

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT', '…']

fname = 'ArtificialIntelligenceTweets.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        # terms_hash = [terms_stop for terms_stop in preprocess(tweet['text'])
        #               if terms_stop.startswith('#')]
        terms_only = [terms_stop for terms_stop in preprocess(tweet['text'])
                      if terms_stop not in stop and
                      not terms_stop.startswith(('#', '@'))]
        count_all.update(terms_only)
    for word, index in count_all.most_common(10):
        print ('%s : %s' % (word, index))

    sorted_x, sorted_y = zip(*count_all.most_common(15))
    print(sorted_x, sorted_y)

    plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='center')
    plt.xticks(range(len(sorted_x)), sorted_x, rotation=60)
    plt.axis('tight')

plt.show()
plt.savefig('CaseStudy.png')


