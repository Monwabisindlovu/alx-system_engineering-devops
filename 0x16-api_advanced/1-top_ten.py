#!/usr/bin/python3

"""
prints the titles offirst 10 hot posts listed for a given subreddit
"""
import requests

def submit_comment(subreddit, post_id, comment_text):
    """Submit a comment to a given post on a given subreddit."""
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    username = 'your_username'
    password = 'your_password'

    # Get the access token
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {'grant_type': 'password', 'username': username, 'password': password}
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    access_token = response.json()['access_token']

    # Submit the comment
    headers = {'Authorization': f'bearer {access_token}', 'User-Agent': 'my-app/0.0.1'}
    data = {'api_type': 'json', 'text': comment_text, 'thing_id': post_id}
    response = requests.post('https://oauth.reddit.com/api/comment', headers=headers, data=data)

    # Check the response
    if response.status_code == 200:
        print('Comment submitted successfully')
    else:
        print('Error submitting comment:', response.json()['message'])


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    head = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    param = {
        "limit": 10
    }
    response = requests.get(url, headers=head, params=param,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    for c in results.get("children"):
        post_id = c.get("data").get("id")
        post_title = c.get("data").get("title")
        print(post_title)
        submit_comment(subreddit, post_id, f"This is a test comment on {post_title}")
