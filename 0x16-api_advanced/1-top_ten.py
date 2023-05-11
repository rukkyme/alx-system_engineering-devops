#!/usr/bin/python3

"""
This function query Reddit API and print the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Query Reddit API and print the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None

    Prints:
        title of the first 10 hot posts, or 'None' if subreddit invalid.

    Raises:
        None
    """
    # Set custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'rukkyme/0.1'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the subreddit is invalid, print None
    if response.status_code == 404:
        print(None)
        return

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts[:10]:
            print(post['data']['title'])
    else:
        print("Error: {}".format(response.status_code))
