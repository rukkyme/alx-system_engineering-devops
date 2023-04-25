#!/usr/bin/python3
"""This expo:rts to-do list information of all employees to JSON format."""
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
