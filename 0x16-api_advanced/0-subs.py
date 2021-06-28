#!/usr/bin/python3
"""
Querie Reddit API
"""
import requests
headers = {"User-Agent": "ubuntu:hbtn:v1.0 (by /u/Tristan_001)"}


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
        return request.json().get("data").get("subscribers")

    return 0
