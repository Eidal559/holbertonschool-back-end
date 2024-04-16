#!/usr/bin/python3
"""Script to use a REST API to gather information about all tasks
from all employees and export in JSON format."""
import json
import requests
from typing import Dict, List

API_URL = "https://jsonplaceholder.typicode.com"


def fetch_json_data(url: str) -> List[Dict]:
    """Fetch JSON data from the specified URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_all_tasks() -> Dict[int, List[Dict]]:
    """Fetch all tasks for all employees."""
    # Fetch users data
    users = fetch_json_data(f"{API_URL}/users")

    # Dictionary to hold tasks for each user
    user_tasks_dict = {}

    # Process each user
    for user in users:
        # Fetch tasks for the current user
        tasks = fetch_json_data(f"{API_URL}/users/{user['id']}/todos")

        # Create a list to hold tasks for the current user
        tasks_list = []

        # Process each task for the current user
        for task in tasks:
            task_info = {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            tasks_list.append(task_info)

        # Store the list of tasks for the current user in the dictionary
        user_tasks_dict[user["id"]] = tasks_list

    return user_tasks_dict


def export_to_json(data: Dict[int, List[Dict]], filename: str) -> None:
    """Export the given data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def main() -> None:
    """Main function to fetch and export data."""
    # Fetch all tasks data
    all_tasks_data = fetch_all_tasks()

    # Export data to JSON file
    export_to_json(all_tasks_data, "todo_all_employees.json")

    print("Data exported to todo_all_employees.json")


if __name__ == "__main__":
    main()
