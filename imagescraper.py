import tweepy
import cheong_key
import time
import json
import wget

# rohhse account authorization
auth = tweepy.OAuthHandler(cheong_key.consumer_key, cheong_key.consumer_secret)
auth.set_access_token(cheong_key.access_token, cheong_key.access_token_secret)
api = tweepy.API(auth)
half_day = 43200

media_file = set()
while 1:
    try:
        # go through timeline
        timeline = api.home_timeline()
        for tweet in timeline:
            text = tweet.text
            media = tweet.entities.get('media',[])
            if (len(media) > 0):
                media_file.add(media[0]['media_url'])
        for f in media_file:
            wget.download(f)
        time.sleep(half_day)
    except Exception as e:
        print(str(e))
        time.sleep(half_day)
