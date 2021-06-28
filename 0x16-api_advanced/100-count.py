#!/usr/bin/python3
"""
    Recursive function to querie Reddit API
"""
import re
import requests
headers = {'user-agent': 'ubuntu:hbtn:v1.0\
 (by /u/Tristan_001)'}


def count_words(subreddit, word_list, after='', occurs={}):
    """
    Recursive function to querie Reddit API
    """
    url = 'https://api.reddit.com/r/' + subreddit + '?limit=100&after=' + after
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
    except:
        return
    if (str(response.status_code) == '404'):
        return
    dataLength = len(data['data']['children'])
    if (dataLength is 0):
        return
    for i in range(0, dataLength):
        try:
            get_title = data['data']['children'][i]['data']['title']
            for ww in word_list:
                try:
                    occurs[ww]
                except KeyError:
                    occurs[ww] = 0
                finally:
                    occurs[ww] += re.subn(r'(?i)(?<!\S)\b{}\b(?!\S)'.format(ww),
                                         '', get_title)[1]
        except:
            pass
    afterVal = data['data']['after']
    if (afterVal is not None):
        return count_words(subreddit, word_list, afterVal, occurs)
    else:
        for key in sorted(occurs, key=lambda k: (-occurs[k], k)):
            if (occurs[key] > 0):
                print("{}: {}".format(key, occurs[key]))
        return
