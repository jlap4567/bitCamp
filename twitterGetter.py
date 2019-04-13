import tweepy

auth = tweepy.OAuthHandler("Enter key", "Enter key secret")
auth.set_access_token("Enter access token", "Enter access token secret")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
