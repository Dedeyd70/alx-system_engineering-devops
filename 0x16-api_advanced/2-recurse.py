#!/usr/bin/python3
"""
Getting the titles of the hot posts for a given subreddit
"""
import requests

URL = 'https://www.reddit.com/r/{}/hot.json'
USER_AGENT = 'Mozilla/5.0 (Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'


def recurse(subreddit, titles=[], **kwargs):
    """
    Querying reddit for all hot posts of a subreddit
    """
    params = {
        'after': kwargs.setdefault('after'),
        'count': kwargs.setdefault('count', 0),
        'limit': kwargs.setdefault('limit', 100)
    }
    d = requests.get(
        URL.format(subreddit),
        headers={'User-Agent': USER_AGENT},
        params=params,
        allow_redirects=False,
        timeout=30,
    )
    if d.status_code == 200:
        results = d.json()['data']
        titles.extend(post['data']['title'] for post in results['children'])
        if results['after'] is not None:
            kwargs['after'] = results['after']
            kwargs['count'] += kwargs['limit']
            return recurse(subreddit, titles, **kwargs)
        return titles
    return None
