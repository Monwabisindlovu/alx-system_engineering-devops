#!/usr/bin/python3
"""
Recursively query the Reddit API for all hot articles in a given subreddit

Args:
    subreddit (str): The name of the subreddit
    hot_list (list, optional): The list of hot articles to append to
    after (str, optional): The after parameter for pagination

Returns:
    list: The list of hot articles
"""
if hot_list is None:
    hot_list = []

url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
headers = {
    'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/fraol21)',
}
params = {
    'limit': 25,
}
if after:
    params['after'] = after

response = requests.get(url, headers=headers, params=params)
data = response.json()

for child in data['data']['children']:
    hot_list.append(child['data']['title'])

after = data['data']['after']
if after:
    recurse(subreddit, hot_list, after)
else:
    return hot_list
