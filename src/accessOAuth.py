# -*- encoding: utf-8 -*-
'''
Created on 2015年5月5日

@author: xiao
'''

import tweepy

CONSUMER_KEY = '6phMdNK4VfoHSOWqeakRxblOv'
CONSUMER_SECRET = '4E1TUPU21lv4ip9fqmwZLcUfQzjW4s0XMTx8OdwbH6qvrHHf1e'
OAUTH_TOKEN = '3230882224-NC1MwvGSSK7RGwCMCBuNABNWyE7ZPRB0pnYRkZ0'
OAUTH_TOKEN_SECRET = 'JYiGXlOWch8vEIyExdKHqjA23hgHof4E4TXyokRwFywFx'

def get_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    api = tweepy.API(auth) 
    return api

