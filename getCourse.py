# Import the Canvas class
from canvasapi import Canvas
import sys
sys.path.append('/home/spooky/canvas-utilities/')

from vault.dmccreds import Credentials
url = Credentials.API_URL

key = Credentials.API_KEY

# Initialize a new Canvas object
canvas = Canvas(url, key)

group = canvas.get_course(1502155, include=['users'])

print(group.get_enrollments)