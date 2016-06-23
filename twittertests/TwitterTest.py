from tweepy import OAuthHandler, Stream, API, StreamListener
import config
import sys
import json
import pprint


class MyStreamListener(StreamListener):
    def __init__(self):
        self.jsonData = []


    def on_status(self, status):
        print unicode(status.text).encode('utf-8')

    def on_data(self, raw_data):

        while len(self.jsonData) < 10:
            print str(len(self.jsonData)) + "@#%$#^%&##*^*^*^*^@##@!@!!@%@%$&#^%*&$^(^&*%^&^*^%@%$!$#~@$!$@!#!#@#!$@^$%&^@$%&" + "\n" * 5
            temp = json.loads(raw_data)
            self.jsonData.append(temp)
            pprint.pprint(self.jsonData)
        return

    def write_file(self, twitter_data):
        pass

if __name__ == "__main__":

    data = None
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = API(auth)

    myStreamListener = MyStreamListener()
    myStream = Stream(auth = api.auth, listener = myStreamListener)


    myStream.filter(locations=[-74.0369,40.6848,-73.8638,40.9104])
