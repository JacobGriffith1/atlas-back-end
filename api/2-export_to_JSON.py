#!/usr/bin/python3
"""2. Export to JSON"""
import json
import requests
import sys


def fetch_data(id):
    """Fetches data on an employee and their todos from the API"""
    base_url = f"https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{id}"
    todos_url = f"{base_url}/todos?userId={id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        return None, None

    return user_response.json(), todos_response.json()
# data is now JSON-formatted; ready to be used.


def export_to_json(id, employee, todos):
    """Export todo list to a JSON file"""
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee.get('username')
        })

    filename = f"{id}.json"
    with open(filename, 'w') as file:
        json.dump({str(id): tasks}, file, indent=2)
        # indent option will pretty print the code
    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <id>")
        sys.exit(1)
    try:
        id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    employee, todos = fetch_data(id)
    if not employee:
        print(f"User {id} not found")
        sys.exit(1)

    export_to_json(id, employee, todos)
