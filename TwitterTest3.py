from tweepy import OAuthHandler, Stream, API, StreamListener
import config
import sys
import json
import pprint
import sqlite3
import time


class MyStreamListener(StreamListener):
    def __init__(self):
        self.con = sqlite3.connect('sqltest.db')
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS twittertesttable4 (data TEXT, geo TEXT, lat REAL , lon REAL )')






    def on_status(self, status):
        print unicode(status.text).encode('utf-8')

    def on_data(self, raw_data):
        data = json.loads(raw_data)

        while (self.cur.lastrowid < 1000):
            print self.cur.lastrowid
            with self.con:
                cur = self.con.cursor()
                if data['coordinates'] is None:
                    self.cur.execute("INSERT INTO twittertesttable4(data, geo) VALUES (?, ?)", (raw_data, 'False',))

                elif data['coordinates'] is not None:
                    lat, lon = data['coordinates']['coordinates']
                    self.cur.execute("INSERT INTO twittertesttable4(data, geo, lat, lon) VALUES (?, ?, ?, ?)", (raw_data, 'True', lat, lon, ))

                else:
                    raise "oh-no"

        return False

        #self.con.commit()
        return
    def keep_alive(self):
        print "keep alive"
        return
    def on_exception(self, exception):
        print exception
        return
    def on_limit(self, track):
        print track
        return
    def on_error(self, status_code):
        print status_code
        return
    def on_timeout(self):
        return








if __name__ == "__main__":

    data = None
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = API(auth)

    myStreamListener = MyStreamListener()
    myStream = Stream(auth = api.auth, listener = myStreamListener)


    myStream.filter(locations=[-74.0369,40.6848,-73.8638,40.9104])
