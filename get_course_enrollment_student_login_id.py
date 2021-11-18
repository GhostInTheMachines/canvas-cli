"""This script is for outputting a list of student login ids from the given course id.
Course IDs can be obtained by either searching for the course from the Canvas front end,
or running an SIS export for the department or sub account that you would like a student list from"""
# Import modules from InstructureConn video
import requests
import json

# Import the Canvas class
from canvasapi import Canvas
from vault.dmc_creds import Credentials
API_URL = Credentials.API_URL

API_KEY = Credentials.API_KEY
# Input course id here - Future updates will either take this from the command line or user prompt
REQ = "/api/v1/courses/1504696/enrollments?type[]=StudentEnrollment"
payload={}
headers = {
    'Authorization': 'Bearer ' + API_KEY
}

response = requests.request("GET", API_URL+REQ, headers=headers, data=payload)
# print(response.text)

Users = response.json()

for user in Users:
    print(user['user']['login_id'])