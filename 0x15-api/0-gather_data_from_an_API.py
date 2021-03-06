#!/usr/bin/python3
"""returns information about employee TODO list progress"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [task.get("title") for task in todos if
                 task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todos)))
    [print("\t {}".format(compl)) for compl in completed]
