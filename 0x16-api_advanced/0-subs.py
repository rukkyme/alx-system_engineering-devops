#!/usr/bin/python3
"""
    This script returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The total number of subscribers for the given subreddit.
    """
import requests


def number_of_subscribers(subreddit: str) -> int:
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers)

    if response.ok:
        data = response.json()["data"]
        return data["subscribers"]
    else:
        response.raise_for_status()


