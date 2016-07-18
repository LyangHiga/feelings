# -*- coding: utf-8 -*-

from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
import time
import requests
import sys
import io
import tweepy

consumer_key = 'W06P4EaZCgmVpoQVQpEdOEcp2'
consumer_secret = 'AOuhpjysQN0LOhgXMZfgQLwAt4cMOKKTTsfOXxxyKJ02tBwi6E'
access_token = '750928470444765184-c7PQTxqqimhxSEZ0a6CJuXS1NDmFaRM'
access_secret = '9RvZU1GanhHiSEMNdN1Az32B49nbzZY7QojVJ8OXrgijC'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
diretorio = "./arquivos/"

class MyListener(StreamListener):
    def __init__(self, fname, time_limit, tweets_limit):
        self.start_time = time.time()
        self.limit = time_limit
        self.n = 0
        self.limit_n = tweets_limit
        if fname == ".txt":
            fname = "#.txt"
        self.f = io.open(diretorio+fname, mode='a',encoding="utf8")
        super(MyListener, self).__init__()

    def on_data(self, data):
        if ((time.time() - self.start_time) < self.limit) and (self.n < self.limit_n):        
            try:
                #with open('teste.txt', 'a') as f:
                all_data = json.loads(data)
                
                text = all_data["text"].replace("\n","").replace("|","/")
                date = all_data["created_at"]
                #geo = all_data["geo"]
                
                self.f.write(("|".join([text,date])+"\n"))
                self.n += 1
            except BaseException as e:
                print("Error on_data: %s" % str(e))
            return True        	
        return False
 
    def on_error(self, status):
        print(status)
        return True
        
    def on_status(self, status):
        if ((time.time() - self.start_time) < self.limit) and (self.n < self.limit_n):
            return True
        return False
