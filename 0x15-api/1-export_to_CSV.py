#!/usr/bin/python3
"""export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    employeeName = employee.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, employeeName, task.get("completed"),
             task.get("title")]
         ) for task in todos]
