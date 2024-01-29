#!/usr/bin/python3
"""
Module to gather data from an API.
"""

import requests
from sys import argv

def get_employee_data(employee_id):
    """
    Function to get employee data from the specified API endpoint.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data

def display_todo_progress(employee_id, user_data, todos_data):
    """
    Function to display TODO list progress.
    """
    employee_name = user_data.get("name")
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = todos_data

    print(f"Employee {employee_name} is done with tasks"
          f"({len(completed_tasks)}/{len(total_tasks)}):")

    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    user_data, todos_data = get_employee_data(employee_id)
    display_todo_progress(employee_id, user_data, todos_data)

