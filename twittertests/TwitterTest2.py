from tweepy import OAuthHandler, Stream, API, StreamListener
import config
import sys
import json
import pprint
import sqlite3
import time


class MyStreamListener(StreamListener):
    def __init__(self):
        self.jsonData = []
        self.raw_data_chunk = []

        self.con = sqlite3.connect('sqltest.sqlite')
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS twittertesttable ( data TEXT)')






    def on_status(self, status):
        print unicode(status.text).encode('utf-8')

    def on_data(self, raw_data):

        while len(self.raw_data_chunk) < 10:
            self.raw_data_chunk.append(raw_data)
            print self.raw_data_chunk


       # self.cur.execute('BEGIN TRANSACTION')
        for i in self.raw_data_chunk:

            self.cur.execute("INSERT INTO twittertesttable VALUES(?)", (i,))

       # self.cur.execute('COMMIT')
        self.con.commit()
        self.raw_data_chunk = []
        return


 #   def write_file(self, twitter_data):




if __name__ == "__main__":

    data = None
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = API(auth)

    myStreamListener = MyStreamListener()
    myStream = Stream(auth = api.auth, listener = myStreamListener)


    myStream.filter(locations=[-74.0369,40.6848,-73.8638,40.9104])
