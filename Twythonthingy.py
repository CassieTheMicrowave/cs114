# Importing the module
from twython import Twython

#Setting these as variables will make them easier for future edits
app_key = "2UbDfKCaAz8oRNwWbygDVVtNe"
app_secret = "MvWUHfAUHa1v6pOnabXJ4KpBvp4BG8xane4Ktjj3hG7qeyCUjx"
oauth_token = "898316520794841090-Gt7sN0L9SWSkVnwaKr4lMOJxDIoNgDT"
oauth_token_secret = "GZIK6KaVsitTHiyr7T7MZZMG8YWZd2O9DZuyJMp1Zxuqp"

#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break

#The obligatory first status update to test
twitter.update_status(status="\U0001f604")
