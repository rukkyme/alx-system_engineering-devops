#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a given subreddit."""

import requests
def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != requests.codes.ok:
        print("None")
        return
    results = response.json().get("data")
    for child in results.get("children"):
        print(child.get("data").get("title"))


