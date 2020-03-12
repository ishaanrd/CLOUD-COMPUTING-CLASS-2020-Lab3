import json
import os
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import re
from collections import Counter
from nltk.corpus import stopwords
import string


# Collect tweets

# class MyListener(StreamListener):
#
#     def on_data(self, data):
#         try:
#             with open('PeopleOpinion.json', 'a') as f:
#                 f.write(data)
#                 return True
#         except BaseException as e:
#             print("Error on_data: %s" % str(e))
#         return True
#
#     def on_error(self, status):
#         print(status)
#         return True
#
#
# consumer_key = os.environ['CONSUMER-KEY']
# consumer_secret = os.environ['CONSUMER-SECRET']
# access_token = os.environ['ACCESS-TOKEN']
# access_secret = os.environ['ACCESS-SECRET']
#
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
#
# twitter_stream = Stream(auth, MyListener())
# twitter_stream.filter(track=['Coronavirus'])

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

#
# with open('PeopleOpinion.json', 'r') as f:
#     for line in f:
#         tweet = json.loads(line)
#         tokens = preprocess(tweet['text']) # test
#         print(tokens)


punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT', '…']

fname = 'PeopleOpinion.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        terms_only = [terms_stop for terms_stop in preprocess(tweet['text'])
                      if terms_stop not in stop and
                      not terms_stop.startswith(('#', '@'))]
        count_all.update(terms_only)
    for word, index in count_all.most_common(10):
        print ('%s : %s' % (word, index))

    sorted_x, sorted_y = zip(*count_all.most_common(15))
    print(sorted_x, sorted_y)

