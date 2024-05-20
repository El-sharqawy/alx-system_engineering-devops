#!/usr/bin/python3
"""
a Python script to gather data from an API
"""

import requests
import sys


def FetchData(employeeID):
    """Fetch Data fhttps://jsonplaceholder.typicode.com/rom API"""
    url = "https://jsonplaceholder.typicode.com/"

    todoList = requests.get(f"{url}users/{employeeID}/todos")
    name = requests.get(f"{url}users/{employeeID}")

    jsonName = name.json()["name"]
    todoJson = todoList.json()

    tasksDone = 0

    for task in todoJson:
        if task["completed"]:
            tasksDone += 1

    print(f"Employee {jsonName} is done "
          f"with tasks({tasksDone}/{len(todoJson)}):")
    for task in todoJson:
        if task["completed"]:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(0)

    employeeID = int(sys.argv[1])
    if not isinstance(employeeID, int):
        raise TypeError("Employee ID should be an integer.")

    FetchData(employeeID)
