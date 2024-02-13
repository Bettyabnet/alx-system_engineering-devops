#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses
the title of all hot articles, and prints a sorted
count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    if not word_list:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
     headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
     params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params)
