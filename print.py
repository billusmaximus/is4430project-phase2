import json
import urllib

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
pyresponse =  json.load(response)

results = pyresponse["results"]

for l in range(10):
    print results[l]["text"]
