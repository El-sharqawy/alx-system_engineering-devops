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

    filePath = f"{employeeID}.csv"

    with open(filePath, "w") as file:
        for task in todoJson:
            file.write(
                f"\"{employeeID}\",\"{jsonName}\",\"{task['completed']}\",\"{task['title']}\""
                + "\n"
            )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(0)

    employeeID = int(sys.argv[1])
    if not isinstance(employeeID, int):
        raise TypeError("Employee ID should be an integer.")

    FetchData(employeeID)
