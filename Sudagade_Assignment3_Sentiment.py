import tweepy # Tweepy is an easy to use Python library used to access the Twitter API
import time # This module provides various time related functions for us to use
from textblob import TextBlob # This is a python library that is used to process textual data

# Below are the access key that I have received after creating a developer account in Twitter. This is unique for each project. So please do not copy it anywhere else
consumer_key = '1iFbECQLQajiHKyqP9wamZ22S' 
consumer_secret = 'X8pHLGIA4prbSoIj3uaKPMCHKkMwfHjrxdpnMB69rl0KchdAoB'
access_token = '76062506-SvmcBckTm7DAIFmYCwqatLKSl1qFRk2DG9laOnJFb'
access_token_secret = 'Qax7GHEPaMpxV4CgdUzHGViJYiQE4Y9QeWk1UiBIG4NkR'

# Tweepy's OAuthHandler and set_access_token functions are used to tell Tweepy use the above mentioned keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token = (access_token, access_token_secret)

# The API function will then use auth to authenticate our access to Twitter's API, the rest of the properties are used to make our code wait and notify us if we have reached the API's access limit
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# As requested, I am setting the query keyword as BLOCKCHAIN
query = 'BLOCKCHAIN'
# This code will retrieve the 10,000 most recent tweets from the API
max_tweets = 10000

# Cursor function is used to tell Tweepy to search the api for 10,000 latest Blockchain related tweets from the API 
tweets = tweepy.Cursor(api.search, q=query).items(max_tweets)
# Below variables are used in case the access limit is reached
count = 0
start = 0
errorCount = 0
waitQuery = 100
waitTime = 2.0
justincase = 1
secondcount = 0



for tweet in tweets:
  # Below is a filter that will retrieved all the English, non-tweeted Tweets from the API
  if (tweet.lang == "en") and (not tweet.retweeted) and ('RT @' not in tweet.text):
    # This section is for the case where the code has reached the access limit of the API, it will now sleep untill we are allowed access to the API again
    try:
      tweet = next(tweets)
      count += 1
      if (count%waitQuery == 0):
        time.sleep(waexcitTime)
    except tweepy.TweepError:
      print ("sleeping...")
      time.sleep(60*justincase)
      tweet = next(tweets)
    # Here Textblob will analyze the tweet's text and give out to values Sensitivity and polarity
    try:
      analysis = TextBlob(tweet.text)
      if(analysis.sentiment.polarity > 0):
        print(tweet.text)
        print("This tweet is negative\n")
      elif(analysis.sentiment.polarity == 0):
        print(tweet.text)
        print("This tweet is neutral\n")
      else:
        print(tweet.text)
        print("This tweet is positive")
    # Most tweets contain Emojis. Chances are that this code will not be able to read it. So I am adding this exception to the UNICODE ERROR
    except UnicodeEncodeError:
      print ("Unicode Encode Error")

# Please run this code in the Terminal for best results.