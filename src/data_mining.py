import twitter
import json

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = '6phMdNK4VfoHSOWqeakRxblOv'
CONSUMER_SECRET = '4E1TUPU21lv4ip9fqmwZLcUfQzjW4s0XMTx8OdwbH6qvrHHf1e'
OAUTH_TOKEN = '3230882224-NC1MwvGSSK7RGwCMCBuNABNWyE7ZPRB0pnYRkZ0'
OAUTH_TOKEN_SECRET = 'JYiGXlOWch8vEIyExdKHqjA23hgHof4E4TXyokRwFywFx'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print json.dumps(world_trends,indent=1)
print 
print json.dumps(us_trends,indent=1)