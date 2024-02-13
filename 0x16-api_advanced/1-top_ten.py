#!/usr/bin/python3
"""
Function to print hot posts on a given Reddit subreddit.
"""
import requests

def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])
        for post in data:
            title = post.get("data", {}).get("title")
            print(title)
    else:
        print("No posts found.")

if __name__ == "__main__":
    subreddit = input("Enter the subreddit: ")
    top_ten(subreddit)

