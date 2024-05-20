#!/usr/bin/python3
"""
a Python script to gather data from an API
"""

import json
import requests


def FetchData():
    """Fetch Data fhttps://jsonplaceholder.typicode.com/rom API"""
    url = "https://jsonplaceholder.typicode.com/"

    todoList = requests.get(f"{url}todos")
    usersList = requests.get(f"{url}users")

    usersJson = usersList.json()
    todoJson = todoList.json()

    totalToDo = {}

    for user in usersJson:
        userTasks = []
        for task in todoJson:
            if task.get("userId") == user.get("id"):
                taskDict = {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                }
                userTasks.append(taskDict)
        totalToDo[user.get("id")] = userTasks

    filePath = "todo_all_employees.json"
    with open(filePath, "w") as file:
        json.dump(totalToDo, file)


if __name__ == "__main__":
    FetchData()
