#!/usr/bin/python3
"""0. Gather data from an API"""
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

def todo_list(employee, todos):
    """Displays todo list progress of given employee"""
    name = employee.get('name')
    total_tasks = len(todos)
    done_check = [task for task in todos if task.get('completed')]
    done_count = len(done_check)

    print(f"Employee {name} is done with tasks({done_count}/{total_tasks}):")
    for task in done_check:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <id>")
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

    todo_list(employee, todos)
