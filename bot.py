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


def getDogeCoinPrice():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd"


    response = requests.request("GET", url)

    data = response.json()
    return data["dogecoin"]["usd"]






def getMentions_Respond_Follow(api, last_mention_id):
    new_id = last_mention_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=last_mention_id).items():
        new_id = max(tweet.id, last_mention_id) # update the last mention in order to not track the whole list
        if tweet.in_reply_to_status_id !=None: # Check wether we had already responded to the tweet
            continue
        if bot_user in tweet.text: # Check if it is really a mention tweet
            if tweet.favorited == False:
                tweet.favorite()
                if tweet.user.following == False: # Respond to user and follow
                    api.create_friendship(tweet.user.id)
                    api.update_status(
                        status=f"Hi @{tweet.user.screen_name} 😇 !\nThe dogecoin price is {getDogeCoinPrice()} $ 🐕 !",
                        in_reply_to_status_id=tweet.id)
            

                print("Had one interaction !")
    return new_id

def main():
    last_mention = 1000
    # Create api object
    api = getAuth(keys)
    while True:
        # Do the fucking stuff
        last_mention = getMentions_Respond_Follow(api,last_mention)
        time.sleep(20)
if __name__ == "__main__":
    main()