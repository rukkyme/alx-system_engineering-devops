#!/usr/bin/python3
"""This module exports tasks from all employees in JSON format.

This module provides a function to export all tasks from all employees in JSON
format. The function retrieves task data from the JSONPlaceholder API for all
users and exports it in a JSON format that includes information about each task,
including the user ID, username, task title, and completion status.

Usage:
    Call the export_todo_all_employees() function to export all tasks from all
    employees to a JSON file.

"""
import json
import requeists

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    all_user_data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        user_data = [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]
        all_user_data[user_id] = user_data

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_user_data, jsonfile)
