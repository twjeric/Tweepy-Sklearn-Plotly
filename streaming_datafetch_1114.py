import tweepy
import json
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import time
import csv

# oauth_keys = [["consumer_key_1", "consumer_secret_1", "access_token_1", "access_token_secret_1"], ["consumer_key_2", "consumer_secret_2", "access_token_2", "access_token_secret_2"]]
consumer_key = "F9PpBKyNfIYig6XIB7tjO0M9N"
consumer_secret = "H611qoOW1H31o9c8SFkpYc9UDrs3x3O4lEnO12x18X9TzRHhJ2"
access_token = "930674351585800192-fVjixlsfV7PvqBpRVVsV1oK5YaD2Ahb"
access_token_secret = "q4oMDCzX4oXqQWJo1tQERrFh4PWZWPf100pdubGd9iguf"

def process_status(sta):
	print sta.user
	print sta.text



if __name__ == "__main__":
    #pdb.set_trace()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api1 = tweepy.API(auth)
    tweetsDict = {}
    counter = 0
    status_count = 0
    statuses = tweepy.Cursor(api1.search, q="valentine", geocode="34.0201613,-118.6919255,20mi").items()
    with open('valentine.csv', 'a') as csvFile:
        fieldnames = ['user_id', 'created_at', 'hashtags', 'retweet_count', 'favorite_count', 'user_name',
                      'user_friends_count', 'user_followers_count', 'user_location', 'user_tweet_count', 'place', 'geo',
                      'tweets']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        while(True):
            try:
                counter+=1
                for status in statuses:
                    if('RT @' not in status.text and 'alentine' not in status.user.name):
                        tweetsDict[status.id_str] = {}
                        thisTweet = tweetsDict[status.id_str]
                        thisTweet["user_id"] = status.user.id_str
                        thisTweet["created_at"] = str(status.created_at)
                        thisTweet["hashtags"] = []
                        for hashtag in status.entities["hashtags"]:
                            thisTweet["hashtags"].append(hashtag["text"])
                        thisTweet["retweet_count"] = status.retweet_count
                        thisTweet["favorite_count"] = status.favorite_count
                        thisTweet["user_name"] = status.user.name
                        thisTweet["user_friends_count"] = status.user.friends_count
                        thisTweet["user_followers_count"] = status.user.followers_count
                        thisTweet["user_location"] = status.user.location
                        thisTweet["user_tweet_count"] = status.user.statuses_count
                        thisTweet["place"] = str(status.place)
                        thisTweet["geo"] = str(status.geo)
                        thisTweet["tweets"] = status.text.encode('utf-8')
                        # with open('cs145data_filtered_motherday.json', 'w') as outFile:
                        #     json.dump(tweetsDict, outFile, sort_keys=True)
                        try:
                            writer.writerow(thisTweet)
                        except UnicodeEncodeError:
                            pass
                csvFile.flush()
                statuses = statuses.next()
                print counter
                    # Insert into db
            except tweepy.TweepError:
                print "status_count %d" %status_count
                time.sleep(60 * 15)
                status_count+=1
            except StopIteration:
                pass
        print counter
	#for status in tweepy.Cursor(api1.user_timeline, id=userid, q="christmas").items(200):
		#f.write(str(status._json['user']))

		# f.write(status.text.encode('utf-8'))
		# status.id_str
		# status.created_at
		# status.entities.hashtags
		# status.user.id_str
		# status.user.name
		# status.place
		# status.geo



	#pdb.set_trace()
