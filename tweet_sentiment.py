import sys
import json


def calc_sentiment():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    scores = {} #Make empty dictionary

    for line in sent_file:
        term,score=line.split("\t")
        scores[term] = int(score) #COnverting score to integer

    #print scores.items() #display contents of scores

    data = []
    sentiment = 0.0
    with open(sys.argv[2]) as f:
        for line in f:
            data.append(json.loads(line))

    for index,item in enumerate(data):
        sentiment = 0.0
        tweet_dict =  data[index]
        if 'text' in tweet_dict:
            tweet_txt = tweet_dict['text']
            #tweet_txt =  data[index]['text']
            tweet_list = tweet_txt.split()
            for word in tweet_list:
                if word in scores:
                    sentiment = sentiment + scores[word]
        print sentiment


if __name__ == '__main__':
    main()
