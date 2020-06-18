#reference: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/

import os
import tweepy as tw
import pandas as pd

consumer_key='Aui0x7f6MGnsXEjdSMOeBVoqa'
consumer_secret='i3uUUhag9IA9xYXXGRrOJefw6pqcB1eaVnfzb4ZFOKn9F9gfb6'
access_token='757232698117283840-uO9a5o37b9zGlPadTaa60uD4Bk4b836'
access_token_secret='fVsGIIjJLhAgMJoGLfcIRN99k7v6udG3vfpfWBc84nuOE'


search_words = "#seguridad"
date_since = "2018-01-01"


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="es",
              since=date_since,
                           ).items(10)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)

# retweets
print('----retweets-----')
new_search = search_words + " -filter:retweets"
new_search
tweets = tw.Cursor(api.search,
                       q=new_search,
                       lang="es",
                       since=date_since,
                   ).items(10)

[print(tweet.text) for tweet in tweets]

tweets = tw.Cursor(api.search,
                           q=new_search,
                           lang="es",
                           since=date_since,
                          ).items(10)

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
print(users_locs)

