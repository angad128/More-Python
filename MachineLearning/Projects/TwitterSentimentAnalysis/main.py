import tweepy
from textblob import TextBlob

consumer_key = 'xzqMUJSahSYadgCtXHsXoBZrf'
consumer_secret = 'yV50oVAZCyOeo17ylCf7AJuqceYbSSQ1wBVPjeQzWPzSnK9coR'


access_token = '938093467304988672-fLe0HIi4AzAZnBCp5zf2vheBskNm2as'
access_token_secrect = 'zwqCfcLc35KHUqWKSbn2WJ8lP9oBWFXuQL2zUym4Kttqm'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secrect)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
