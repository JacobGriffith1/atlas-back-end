#!/usr/bin/python3
"""0. Gather data from an API"""
import json
import sys
import urllib.request

base_url = "https://jsonplaceholder.typicode.com/"

# Write a Python script that, using this REST API,
if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print("Please enter an employee ID.")
    
    else:
        employee_id = int(sys.argv[1])