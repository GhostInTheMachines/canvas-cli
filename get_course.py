"""really go away"""
# Import the Canvas class
from canvasapi import Canvas
from vault.dmc_creds import Credentials
API_URL = Credentials.API_URL

API_KEY = Credentials.API_KEY

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

group = canvas.get_course(1502155, include=['users'])

print(group.get_enrollments)
