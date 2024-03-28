#!/usr/bin/python3
"""Python script to export data in the JSON format
    -   run by ./script <user_id>
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(f"{url}users/{argv[1]}").json()
    todo = requests.get(f"{url}todos", params={"userId": argv[1]}).json()
    username = user['username']
    val = []
    for items in todo:
        data = {}
        data['task'] = items['title']
        data['completed'] = items['completed']
        data['username'] = username
        val.append(data)

    final_data = {"{}".format(argv[1]): val}
    filename = '{}'.format(argv[1]) + '.json'
    with open('{}'.format(filename), 'w', encoding='utf-8') as file:
        json.dump(final_data, file)
