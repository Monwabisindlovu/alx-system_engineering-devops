#!/usr/bin/python3
"""
Extend the Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    response_user = requests.get(url_user)
    response_todos = requests.get(url_todos)

    user_data = response_user.json()
    tasks_data = response_todos.json()

    username = user_data.get('username')

    # Task 1: Export data to individual JSON file
    output_filename = f"{user_id}.json"
    with open(output_filename, 'w') as json_file:
        user_tasks = [{"task": task.get('title'), "completed": task.get('completed'), "username": username} for task in tasks_data]
        json.dump({user_id: user_tasks}, json_file)

    # Task 2: Export data to a single JSON file for all employees
    all_employees_filename = "todo_all_employees.json"
    all_employees_data = {user_id: [{"username": username, "task": task.get('title'), "completed": task.get('completed')} for task in tasks_data]}

    # If the file already exists, load the existing data and update it
    try:
        with open(all_employees_filename, 'r') as all_employees_file:
            existing_data = json.load(all_employees_file)
            existing_data.update(all_employees_data)
    except FileNotFoundError:
        existing_data = all_employees_data

    with open(all_employees_filename, 'w') as all_employees_file:
        json.dump(existing_data, all_employees_file)

