#!/usr/bin/python3
"""Python script that exports all tasks of employees to JSON format
    -   run by ./script <user_id>
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get('{}users'.format(url)).json()
    todo = requests.get('{}todos'.format(url)).json()
    final_data = {}
    for num in range(len(users)):
        values = []
        username = users[num].get('username')
        user_id = num + 1
        for items in todo:
            data = {}
            if items['userId'] == user_id:
                data['username'] = username
                data['task'] = items['title']
                data['completed'] = items['completed']
                values.append(data)
            else:
                continue
        final_data["{}".format(user_id)] = values

    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        json.dump(final_data, file)
