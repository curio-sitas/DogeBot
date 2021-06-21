#!/usr/bin/python3

import tweepy
import requests
import json
import time

from keys import keys # Get these on the Twitter Developer Portal

bot_user = "@DogeBot11"

# Authenticate to Twitter
def getAuth(keys):
    auth = tweepy.OAuthHandler(keys['API_ID'],keys['API_SECRET'] )
    auth.set_access_token(keys['TOKEN_ID'],keys['TOKEN_SECRET'] )

    # Create API object
    return tweepy.API(auth)

def main():
    
    # Create api object
    api = getAuth(keys)
    tweet = api.user_timeline(count = 1)[0]
    api.destroy_status(tweet.id)   
    api.update_status(status=f"@ApolloNano\n!coinflip\n😇")

    
if __name__ == "__main__":
    main()