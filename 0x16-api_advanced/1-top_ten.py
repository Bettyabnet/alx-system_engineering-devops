#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a given
subreddit.
"""
import requests

def top_ten(subreddit):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
    r = requests.get('https://www.reddit.com/r/{:}/hot.json?limit=10'.format(
        subreddit), headers=headers, allow_redirects=False)
    if r.status_code < 300:
        json = r.json()
        data_dict = json.get('data')
        hot_list = data_dict.get('children')
        for post in hot_list:
            sub_data_dict = post.get('data')
            print(sub_data_dict.get('title'))
    else:
        print(None)
