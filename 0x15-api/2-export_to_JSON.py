#!/usr/bin/python3
"""
Module to export data to JSON.
"""

import json
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

def export_to_json(employee_id, user_data, todos_data):
    """
    Function to export data to JSON format.
    """
    employee_name = user_data.get("username")
    file_name = f"{employee_id}.json"

    json_data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name
            }
            for task in todos_data
        ]
    }

    with open(file_name, 'w') as json_file:
        json.dump(json_data, json_file)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    user_data, todos_data = get_employee_data(employee_id)
    export_to_json(employee_id, user_data, todos_data)

