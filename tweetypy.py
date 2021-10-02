import tweepy
import requests
import json
import time


bearerHeader = {"Authorization": "Bearer "}
auth = tweepy.OAuthHandler("", "")
auth.set_access_token(
    "",
    "",
)

api = tweepy.API(auth)
auth2 = tweepy.AppAuthHandler("", "")
client = tweepy.API(auth2)
tweetIds = []
safeIds = []
paginationTokens = []
for i in range(1081948665458147329):

    try:
        if paginationTokens:
            resp = requests.get(
                f"https://api.twitter.com/2/users/{1081948665458147329}/tweets?max_results={100}&pagination_token={paginationTokens[-1]}",
                headers=bearerHeader,
            )
        else:
            resp = requests.get(
                f"https://api.twitter.com/2/users/{1081948665458147329}/tweets?max_results={100}",
                headers=bearerHeader,
            )
        resp = json.loads(resp.text)
        for tweet in resp["data"]:
            # print(type(tweet["id"]))
            tweetIds.append(tweet["id"])
            for j in safeIds:
                if tweet["id"] == j:
                    print(f"{j} silinmedi")
                    break
            api.destroy_status(id=tweet["id"])
            # print(f"{tweet['id']} silindi")

        paginationTokens.append(resp["meta"]["next_token"])
        # print("bi 100lük sildim")
        time.sleep(2)
    except:
        # print("ters giden bir şeyler var")
        break
