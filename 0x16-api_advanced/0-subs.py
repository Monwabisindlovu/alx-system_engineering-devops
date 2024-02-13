#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API to get the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)
    
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0

