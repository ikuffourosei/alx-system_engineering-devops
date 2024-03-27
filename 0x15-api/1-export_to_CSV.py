#!/usr/bin/python3
"""Python script to export data in the CSV format.
-   run by ./script <user_id>
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(f"{url}users", params={"id": argv[1]}).json()
    todo = requests.get(f"{url}todos", params={"userId": argv[1]}).json()
    filename = '{}'.format(argv[1]) + '.csv'
    with open('{}'.format(filename), 'w', newline='') as file:
        writer = csv.writer(file)
        for data in todo:
            writer.writerow(["{}".format(argv[1]),
                             "{}".format(user[0].get('name')),
                             "{}".format(data['completed']),
                             "{}".format(data['title'])])
