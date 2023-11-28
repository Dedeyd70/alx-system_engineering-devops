#!/usr/bin/python3
"""Script that exports all employees TODO tasks to a json file"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            usr.get("id"): [{
                "task": tk.get("title"),
                "completed": tk.get("completed"),
                "username": usr.get("username")
            } for tk in requests.get(url + "todos",
                                    params={"userId": usr.get("id")}).json()]
            for usr in users}, jsonfile, indent=2)
