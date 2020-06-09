import tweepy
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", type(auth))

api = tweepy.API(auth)
print("API_CLIENT", type(api))

if __name__ == "__main__":
    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print tweet.text

    user = api.get_user('s2t2')

    print(type(user))
    print(user.id)
    print(user.screen_name)
    print(user.followers_count)
    pprint(user._json)

    tweets = api.user_timeline("s2t2", tweet_mode="extended", count=150)
    print(type(tweets))

    for tweet in tweets:
        print('------------------')
        print(tweet.id, tweet.full_text)

    breakpoint()