import requests

Url='https://www.google.com'

Get_content= requests.get(Url)

if Get_content.status_code == 200:
    print(Get_content.text)
else:
    print("لا يعمل")
