import tweepy

from textblob import TextBlob 

wiki = TextBlob("Vivek is always angry beacuse he can't manage his time")

# print(wiki.tags) #Parts of speech

# print(wiki.words) #Tokenize

print(wiki.sentiment)

consumer_key = 'o5CbrDAJkpCLBhHTsu3YkSsvN'
consumer_secret = '2irncRv189vQTBMF3qAO5vwO4LpEHT29rH8r3nagzzvNt9IEEQ'

access_token = '2996486912-b7NCHNfnISl5fsXVO0OLH4Dl7NyfnXCtxwTgsUh'
access_token_secret = '	9KJksG6vLknQs80MimZvHVoiAuYkeGaXrtUxL8Sulxkeg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("")



