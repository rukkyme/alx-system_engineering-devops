#!/usr/bin/python3
import requests
import sys
import json

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    usr = requests.get(url + 'users/{}'.format(user_id)).json()
    username = usr.get("username")
    to_do = requests.get(url + 'todos', params={'userId': user_id}).json()

    completed = []
    for title in to_do:
        if title.get('completed') is True:
            task_data = {
                "task": title.get("title"),
                "completed": title.get("completed"),
                "username": username
            }
            completed.append(task_data)

    user_data = {
        user_id: completed
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(user_data, jsonfile)

