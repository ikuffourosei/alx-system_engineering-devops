#!/usr/bin/python3
""" a Python script that using this REST API, for a given employee ID
returns information about his/her TO-DO list progress.
-   run script using `python3 argv[1] number`
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{argv[1]}").json()
    todo = requests.get(f"{url}/todos", params={'userId': argv[1]}).json()
    comp = [t['title'] for t in todo if t['completed'] is True]
    print(f"Employee {user['name']} is done with tasks\
({len(comp)}/{len(todo)}):")
    for items in comp:
        print(f"\t {items}")
