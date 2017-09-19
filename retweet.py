from twython import Twython

app_key = "2UbDfKCaAz8oRNwWbygDVVtNe"
app_secret = "MvWUHfAUHa1v6pOnabXJ4KpBvp4BG8xane4Ktjj3hG7qeyCUjx"
oauth_token = "898316520794841090-Gt7sN0L9SWSkVnwaKr4lMOJxDIoNgDT"
oauth_token_secret = "GZIK6KaVsitTHiyr7T7MZZMG8YWZd2O9DZuyJMp1Zxuqp"

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

#ReTweeting by ID of the Tweet
twitter.retweet(id = "909911952327032832")
