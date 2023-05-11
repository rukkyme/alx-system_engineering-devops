#!/usr/bin/python3

"""
function to query the Reddit API and return the number
of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query Reddit API and returns the number of subreddit subscribers
    If the subreddit is invalid, return 0.

    Args:
        subreddit (str): name of subreddit to query.

    Returns:
        int: The number of subreddit subscribbers, or 0 if invalid.

    Raises:
        None
    """
    # Set custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'rukkyme/0.1'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
