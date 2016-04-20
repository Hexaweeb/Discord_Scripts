import requests
import time

auth_token = raw_input('Authorization:')
headers = { 'authorization': auth_token }
servers = [
    '149698866541887488','106995902362689536','164183604128120832'
]

def go():
    while 1 < 2:
        for server in servers:
            url = 'https://discordapp.com/api/channels/' + server + '/typing'
            type = requests.post(url, headers=headers)
    time.sleep(0.5)
 
go()