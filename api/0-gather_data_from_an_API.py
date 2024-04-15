#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch employee's user data
    user_url = f'{base_url}users/{employee_id}'
    user_response = requests.get(user_url)
    
    if user_response.status_code != 200:
        print(f'Error: Unable to fetch data for employee ID {employee_id}')
        return
    
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch employee's TODO list data
    todos_url = f'{base_url}todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        print(f'Error: Unable to fetch TODO list for employee ID {employee_id}')
        return

    todos_data = todos_response.json()
    
    # Calculate the total and completed tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Print the output as specified
    print(f'Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task["title"]}')

if __name__ == '__main__':
    # Ensure that an employee ID is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    # Get the employee ID from the command line arguments
    employee_id = int(sys.argv[1])

    # Call the function to get the employee's TODO list progress
    get_employee_todo_progress(employee_id)
