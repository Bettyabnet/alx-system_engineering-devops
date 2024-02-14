#!/usr/bin/python3
""" A function that queries the Reddit API and returns
the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple' +
            'WebKit/537.36 (KHTML, like Gecko)Chrome/121.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
