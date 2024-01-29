#!/usr/bin/python3
"""
Module to export data to CSV.
"""

import csv
import requests

"""Get the user ID from the command line argument"""
user_id = sys.argv[1]

""" Get the user information from the API"""
user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
user_response = requests.get(user_url)
user_data = user_response.json()
user_name = user_data.get("username")

"""Get the tasks information from the API"""
tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
tasks_response = requests.get(tasks_url)
tasks_data = tasks_response.json()

"""Create a CSV file with the user ID as the name"""
file_name = "{}.csv".format(user_id)
with open(file_name, "w", newline="") as csv_file:
    """Create a CSV writer object"""
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    """Loop through the tasks data and write each row"""
    for task in tasks_data:
        task_id = task.get("id")
        task_title = task.get("title")
        task_completed = task.get("completed")
        csv_writer.writerow([user_id, user_name, task_completed, task_title])
