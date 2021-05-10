
# config is the file that contains the actual keys
from config import *
import tweepy
import time
import pandas as pd
import random
import sys

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# GET THE TWEETS THAT HAVE ALREADY BEEN POSTED BEFORE!
# initialize a list to hold all the tweepy Tweets
alltweets = []
# make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.user_timeline(screen_name='ExcitedPinkbike', count=200, tweet_mode="extended")
# save most recent tweets
alltweets.extend(new_tweets)
# save the id of the oldest tweet less one
oldest = alltweets[-1].id - 1

# keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
    print(f"getting tweets before {oldest}")
    # all subsiquent requests use the max_id param to prevent duplicates
    new_tweets = api.user_timeline(screen_name='ExcitedPinkbike', count=200, max_id=oldest)
    # save most recent tweets
    alltweets.extend(new_tweets)
    # update the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

# extract only the tweet text and not all the metadata
posted_tweets = [[tweet.full_text] for tweet in alltweets]

# create empty list and drop the extra junk
posted_tweet_list = []
for row in posted_tweets:
    posted_tweet = row[0]
    posted_tweet_list.append(posted_tweet)

# PICK NEW TWEETS TO POST!
generated = pd.read_csv('C:/Users/custerc/pinkbike_project/data/generated_comments_to_use.csv')
generated = generated.dropna()

counter = 0
todays_tweets = []

# CHECKING AND CHOOSING TWEETS
while counter < 3:
    print(counter)
    potential_tweet = random.choice(generated['Text'])
    potential_tweet = potential_tweet.replace('@', 'To:')
    # check if tweet is already on either list and skip if it is
    if (potential_tweet in todays_tweets) or (potential_tweet in posted_tweet_list):
        pass
    else:
        todays_tweets.append(potential_tweet)
        print("Added " + potential_tweet)
        counter += 1

# An extra check/safety measure
if (len(todays_tweets)) == 3:
    print(todays_tweets)
    print("Confirmed, posting now...")
    pass
else:
    print('Something went wrong....')
    sys.exit()

# POST THE TWEETS!
for line in todays_tweets:
    api.update_status(line)
    print(line)
    print('posting the above...')
    time.sleep(2700)  # Sleep for 45 minutes
