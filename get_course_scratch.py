"""doctype error - really go away"""
# Import modules from InstructureConn video
import requests
import json

# Import the Canvas class
from canvasapi import Canvas
from vault.dmc_creds import Credentials
API_URL = Credentials.API_URL

API_KEY = Credentials.API_KEY

REQ = "/api/v1/courses/1502155/enrollments?type[]=StudentEnrollment"
payload={}
headers = {
    'Authorization': 'Bearer ' + API_KEY
}

# Initialize a new Canvas object
# canvas = Canvas(API_URL, API_KEY)

# group = canvas.get_course(1502155, include=['user_id'])

# print(group.get_enrollments)


response = requests.request("GET", API_URL+REQ, headers=headers, data=payload)
# print(response.text)

Users = response.json()

for user in Users:
    print(user['user']['login_id'])