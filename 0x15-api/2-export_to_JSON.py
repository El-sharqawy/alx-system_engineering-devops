#!/usr/bin/python3
"""
a Python script to gather data from an API
"""

import json
import requests
import sys


def FetchData(employeeID):
    """Fetch Data fhttps://jsonplaceholder.typicode.com/rom API"""
    url = "https://jsonplaceholder.typicode.com/"

    todoList = requests.get(f"{url}users/{employeeID}/todos")
    name = requests.get(f"{url}users/{employeeID}")

    jsonName = name.json()["username"]
    todoJson = todoList.json()

    tasks = []
    user = {}

    for task in todoJson:
        tasks.append(
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": jsonName,
            }
        )

    user[employeeID] = tasks
    file = f"{employeeID}.json"

    with open(file, "w") as file:
        json.dump(user, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(0)

    employeeID = int(sys.argv[1])
    if not isinstance(employeeID, int):
        raise TypeError("Employee ID should be an integer.")

    FetchData(employeeID)
