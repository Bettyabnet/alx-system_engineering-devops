#!/usr/bin/python3
""" A function that queries the Reddit API and returns
the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """ Return the number of subscribers.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/121.0.0.0 Safari/537.36'
    headers = {'User-Agent': User_Agent}

    r = requests.get(url, headers=headers)
    
    if r.status_code == 200:
        data = r.json()
        subscribers = data.get('data').get('subscribers')
        return subscribers
    else:
        return 0
