#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a given subreddit."""

import requests

def top_ten(subreddit):
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get("data")
    for post in data.get("children"):
        print(post.get("data").get("title"))

