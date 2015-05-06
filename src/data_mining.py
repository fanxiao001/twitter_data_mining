
import accessOAuth
import tweepy
import mongod
import operator
from collections import Counter
from prettytable import PrettyTable

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

twitter_api = accessOAuth.get_api()
client=mongod.getMongoDBClient()
db=mongod.getDB(client, 'test')

#public_tweets = tweepy.Cursor(twitter_api.search,q="Ebola",count="100").items(100)
#for tweet in public_tweets:
    #mongod.insertDocument(db, 'Ebola',tweet._json )
cursor=db['Ebola'].find()
retweet_count={}
for document in cursor:
    retweet_count[document['text']]=document['retweet_count']
sorted_retweet_count = sorted(retweet_count.items(), key=operator.itemgetter(1))
pt=PrettyTable(field_names=['text','count'])
[pt.add_row(kv) for kv in sorted_retweet_count[len(sorted_retweet_count)-5:len(sorted_retweet_count)]]
pt.align['text'],pt.align['count']='l','r'

#c=Counter(words)
#[pt.add_row(kv) for kv in c.most_common()[:10] ]
print pt
    
    
'''               
WORLD_WOE_ID = 1
US_WOE_ID = 23424977


# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

world_trends_set=set(trend['name'] for trend in world_trends[0]['trends'])
us_trends_set=set(trend['name'] for trend in us_trends[0]['trends'])
common_trends=world_trends_set.intersection(us_trends_set)

q = '#MentionSomeoneImportantForYou' 
count = 100

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

#print json.dumps(search_results,indent=1)

statuses = search_results['statuses']


# Iterate through 5 more batches of results by following the cursor

for _ in range(5):
    print "Length of statuses", len(statuses)
    try:
        next_results = search_results['search_metadata']['next_results']
        
    except KeyError, e: # No more results when next_results doesn't exist
        break
        
    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

# Show one sample search result by slicing the list...
#print json.dumps(statuses[0], indent=1)
status_texts = [ status['text'] 
                 for status in statuses ]

screen_names = [ user_mention['screen_name'] 
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text'] 
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]

# Compute a collection of all words from all tweets
words = [ w 
          for t in status_texts 
              for w in t.split() ]

for label, data in (('Word', words), 
                    ('Screen Name', screen_names), 
                    ('Hashtag', hashtags)):
    pt = PrettyTable(field_names=[label, 'Count']) 
    c = Counter(data)
    [ pt.add_row(kv) for kv in c.most_common()[:10] ]
    pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
    print pt
'''
