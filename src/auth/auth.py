from requests_oauthlib import OAuth1
from src.auth import secret


def get_auth():
    return OAuth1(
        secret.consumer_key,
        secret.consumer_secret,
        secret.access_token,
        secret.access_secret
    )
