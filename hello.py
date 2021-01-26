#!/usr/bin/env python3

import os
import sys
import cgi
import cgitb
import json
import secret
from http import cookies
from templates import login_page,secret_page


'''
for q1-q3:
print('Content - Type: application/json')
print()
print(json.dumps(dict(os.environ),indent=2))
print()
print(os.environ["QUERY_STRING"])
print(os.environ["HTTP_USER_AGENT"])
print()'''

input_username = ""
input_password = ""
posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    # below we are parsing the input data
    temp_list = posted.splitlines()[0].split("&")
    input_username = temp_list[0].split("=")[1]
    input_password = temp_list[1].split("=")[1]
    print('Content-Type: text/html')
    if (input_username == secret.username) and (input_password == secret.password):
        # store the cookies
        print("Set-Cookie: username={}".format(input_username))
        print("Set-Cookie: password={}".format(input_password))

    print()

cookie_username = ""
cookie_password = ""
C = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])

# read the info in the cookie
if (C.get("username")):
    cookie_username = C.get("username").value

if (C.get("password")):
    cookie_password = C.get("password").value

if (cookie_username == secret.username and cookie_password == secret.password):
    # if it has the correct cookie already
    print(secret_page(cookie_username, cookie_password))

elif (secret.username == input_username and input_password == secret.password):
    print(secret_page(input_username,input_password))

else:
    print(login_page())