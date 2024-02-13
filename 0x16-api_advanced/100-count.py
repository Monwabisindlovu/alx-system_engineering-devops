#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

Args:
    subreddit (str): The name of the subreddit to search.
    word_list (list): A list of keywords to count.

Returns:
    None
"""
if subreddit is None or not isinstance(subreddit, str) or len(subreddit) == 0:
    return

if word_list is None or not isinstance(word_list, list) or len(word_list) == 0:
    return

url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
headers = {'User-Agent': 'MyUserAgent/1.0'}
params = {'limit': 100}

response = requests.get(url, headers=headers, params=params)
data = response.json()

children = data['data']['children']
after = data['data'].get('after')
word_counts = {}

for word in word_list:
    word_counts[word.lower()] = 0

for child in children:
    post = child['data']
    title = post['title'].lower()
    for word in word_list:
        count = title.count(word.lower())
        word_counts[word.lower()] += count

sorted_word_counts = sorted
