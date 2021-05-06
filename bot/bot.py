
# config is the file that contains the actual keys
from config import *
import tweepy
import time

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweetlist = ['Test tweet one!', 'Test tweet two!', 'Test tweet three!']

for line in tweetlist:
    api.update_status(line)
    print(line)
    print('...')
    time.sleep(15)  # Sleep for 15 seconds

print("All done!")
