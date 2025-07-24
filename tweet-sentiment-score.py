from textblob import TextBlob  
print([TextBlob(tweet).sentiment.polarity for tweet in open("tweets.txt")])
