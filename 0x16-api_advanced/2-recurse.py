#!/usr/bin/python3
"""
Recursive function to get a list of all hot posts on a given subreddit.
"""

import requests


def get_all_hot_posts(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit.

    Parameters:
        subreddit (str): The subreddit to query.
        hot_list (list): The list to append post titles to.
        after (str): The post ID to start at.
        count (int): The number of posts to include in the results.

    Returns:
        A list of post titles.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for post in results.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return get_all_hot_posts(subreddit, hot_list, after, count)

    return hot_list

