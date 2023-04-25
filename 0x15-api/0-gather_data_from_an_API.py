#!/usr/bin/python3
import requests

# Function to get employee TODO list progress
def get_employee_todo_progress(employee_id):
    # API endpoint URL
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Send GET request to the API
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        employee_name = todos[0]['name'].split()[0]
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo['completed'])
        print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')
        for todo in todos:
            if todo['completed']:
                print(f'\t{todo["title"]}')
    else:
        print(f'Error getting employee TODO list progress. Response status code: {response.status_code}')


if __name__ == '__main__':
    # This accept employee ID as input
    employee_id = int(input('Enter employee ID: '))

    # this calls the function with the provided employee ID
    get_employee_todo_progress(employee_id)

