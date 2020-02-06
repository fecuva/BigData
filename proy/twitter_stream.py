import tweepy

TWITTER_APP_KEY = 'RNbWRckUdr1mzMYe2ir2S44aP'
TWITTER_APP_SECRET = 'FVB0RX0nGo1VMRAMF603g7jOKuZdKfCLo0SjXWv2T15wHvLMRy'
TWITTER_KEY = '1220749681900191744-JDImKJjEF4NadKsiKekx82zDI9FyQW'
TWITTER_SECRET = 'bQaUWESSjNkqhO3d2Sc4pLPmNDYLr5DiRIIS5ko5Sg4yv'

auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["trump", "clinton", "hillary clinton", "donald trump"])