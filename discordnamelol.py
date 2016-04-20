import requests
import time

email = raw_input('Email:')
password = raw_input('Password:')
avatar = 'c8b136b112473ba615bc1a416f1abdd1'
names = [
    'this','is just','a simple',
    'test to see','if I can','do this'
]
headers = { "authorization": 'your_auth_session_token_here' }
url = 'https://discordapp.com/api/users/@me'
post = {
    'avatar': avatar,
    'email': email,
    'password': password, #kek resets session. will fix later idc.
    'username': names[0],
}

while 1 < 2:
    for name in names:
        post['username'] = 'wewe'
        meme = requests.patch(url, headers=headers, data=post)
        print(meme.text)
        time.sleep(120)