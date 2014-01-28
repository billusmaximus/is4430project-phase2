import sys
import json
import re
import operator
from operator import itemgetter

def input_tweets(fn):

    tweets_file = open(fn)

    # Initialise empty array
    tweets = []

    for tweet in tweets_file:
        # Parse input strings as JSON.
        json_tweet = json.loads(tweet)
        tweets.append(json_tweet)

        # Check that there is a text field.
        #if "text" in json_tweet.keys():
        #    text = json_tweet["text"].encode('utf-8')
        #    tweets.append(text)

    return tweets


def extract_htags(tweets):

    htags = []

    for tweet in tweets:

        # Ensure that there is an entities element to extract.
        if "entities" in tweet.keys() and "hashtags" in tweet["entities"]:

            for htag in tweet["entities"]["hashtags"]:
                unicode_tag = htag["text"].encode('utf-8')
                htags.append(unicode_tag)

    return htags

# -------------------------------------------------------------------------------
# judge_sentiments()
# -------------------------------------------------------------------------------
def top_ten(htags):

    frequencies = []

    for htag in htags:

        tup = [htag,htags.count(htag)]
        if tup not in frequencies : frequencies.append(tup)

        #frequencies[htag] = int(htags.count(htag))

    frequencies_sorted = sorted(frequencies, key=itemgetter(1), reverse=True)

    for i in range(0,10):
        print frequencies_sorted[i][0] + " " + str(float(frequencies_sorted[i][1]))

# -------------------------------------------------------------------------------
# main()
# -------------------------------------------------------------------------------
def main():
    # Populate the list of tweets.
    tweets = input_tweets(sys.argv[1])

    # Extract hash tags.
    htags = extract_htags(tweets)

    top_ten(htags)

if __name__ == '__main__':
    main()
