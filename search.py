#Import TwythonError now too!
from twython import Twython, TwythonError

app_key = "2UbDfKCaAz8oRNwWbygDVVtNe"
app_secret = "MvWUHfAUHa1v6pOnabXJ4KpBvp4BG8xane4Ktjj3hG7qeyCUjx"
oauth_token = "898316520794841090-Gt7sN0L9SWSkVnwaKr4lMOJxDIoNgDT"
oauth_token_secret = "GZIK6KaVsitTHiyr7T7MZZMG8YWZd2O9DZuyJMp1Zxuqp"

#Let's gather a list of words we DON'T want to RT
naughty_words = [" -RT", "football", "Nazi", "fuck",
"White House", "Trump", "sexy", "kill", "horrible", "worst", "shit", "fuck"]
#And a list of words we WOULD like to RT
good_words = ["cute", "kitten", "meow", "love", "funny"]
#OR is Twitter's search operator to search for this OR that
#So let's join everything in good_words with an OR!
filter = " OR ".join(good_words)

# The - is Twitter's search operator for negative keywords
# So we want to prefix every negative keyword with a -
blacklist = " -".join(naughty_words)

#And finally our list of keywords that we want to search for
#This will search for any words in good_words minus any naughty_words
keywords = filter + blacklist

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

#Setting Twitter's search results as a variable
search_results = twitter.search(q="cats", count=5)
try:
    for tweet in search_results["statuses"]:
        twitter.retweet(id = tweet["id_str"])
except TwythonError as e:
    print = "e"
