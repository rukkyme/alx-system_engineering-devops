#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyBot/0.0.1'}
    
    # Make a GET request to the subreddit's about endpoint
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']
        return data['subscribers']
    else:
        return 0

