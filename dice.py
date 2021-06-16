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
    timeline = tweepy.Cursor(api.user_timeline).items()
    api.destroy_status(timeline[-1].id)      
    api.update_status(status=f"@ApolloNano\n!dice\n😇")

    
if __name__ == "__main__":
    main()