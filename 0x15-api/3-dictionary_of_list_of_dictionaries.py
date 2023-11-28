#!/usr/bin/python3
import json
import requests
import sys


def tasks_done():
    """Script that exports all employees TODO tasks to a json file"""

    id = 1
    all_todos = {}
    while True:
        url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        response = requests.get(url)
        response_json = response.json()

        if len(response_json) == 0:
            break
        employee_username = response_json.get("username")

        url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        todos = requests.get(url)
        todos_json = todos.json()
        task_list = []

        for task in todos_json:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = employee_username
            task_list.append(task_dict)

        all_todos[employee_username] = task_list
        id += 1
    file_name = "todo_all_employees.json"

    with open(file_name, "w") as fd:
        json.dump(all_todos, fd, indent=2)


if __name__ == "__main__":
    tasks_done()
