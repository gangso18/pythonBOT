# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "Zzx7WmxkI2uSWjSKtmXTkX6kv"
CONSUMER_SECRET = "CiYIH3ECxEnNAn7NuvRZbOeq1bgvphDbQSCdV7mx5Xec2jVZpa"

OAUTH_TOKEN = "983222173-Ynj5DVoDxmfU2lOp8U3sJoQ5GWXPXos13FpkY44M"
OAUTH_TOKEN_SECRET = "UYFsEKI9qlFGXFg2T9WuZkPiItDwow6uqUyxn5VRuouJB"

def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key_b = credentials.get(b'oauth_token')
    resource_owner_key_a = str(resource_owner_key_b)
    resource_owner_key = resource_owner_key_a[3:-2]
    resource_owner_secret_b = credentials.get(b'oauth_token_secret')
    resource_owner_secret=str(resource_owner_secret_b)[3:-2]


    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
 
    print ('Please go here and authorize: ' + authorize_url)

    verifier = input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token_a = credentials.get(b'oauth_token')
    token = str(token_a)[3:-2]
    secret_b = credentials.get(b'oauth_token_secret')
    secret = str(secret_b)[3:-2]
    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print ("OAUTH_TOKEN: " + token)
        print ("OAUTH_TOKEN_SECRET: " + secret)
        print 
    else:
        oauth = get_oauth()
        #r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi", auth=oauth)
        r =requests.get(url="https://api.twitter.com/1.1/trends/place.json?id=1&count=10",auth = oauth)
        #r = requests.get(url="https://api.twitter.com/1.1/trends/available.json", auth=oauth)        
        #print (ascii(r.json()))

        #x=(r.json())

        for x in range(0,10):
            print (r.json()[0]['trends'][x]["name"])
