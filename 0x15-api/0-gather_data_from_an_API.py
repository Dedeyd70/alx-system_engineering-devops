#!/usr/bin/python3
"""
Returns  to-do list info of a given employee ID
"""

import requests
import sys


if __name__ == "__main__":
    _url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(_url + "users/{}".format(sys.argv[1])).json()

    todos = requests.get(_url + "todos", params={"userId": sys.argv[1]}).json()

    complete = [d.get("title") for d in todos if d.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(complete), len(todos)))
    [print("\t {}".format(t)) for t in complete]
