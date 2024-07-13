#!/usr/bin/python3
"""3. Dictionary of list of dictionaries"""
import json
import requests
import sys


def todo_all():
    """Exports all username and todo data to a JSON file"""
    base_url = f"https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{id}"
    todos_url = f"{base_url}/todos?userId={id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        return None, None

    full_list = {}
    for employee in user_response.json():
        id = employee['id']
        username = employee['username']
        todo = ([task for task in todos_response.json()
                 if task['userId'] == id])
        data = [{
            "username": username,
            "task": task['title'],
            "completed": task['completed']
        } for task in todo]

        full_list[str(id)] = data

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(full_list, file, indent=2)


if __name__ == "__main__":
    todo_all()
