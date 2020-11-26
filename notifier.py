import requests

url = "https://www.fast2sms.com/dev/bulk"

my_data = {
    "authorization":"cgHJxPNUFSetwpvf1mQjAZsiKy5zTGu62o0qR9lEarLh7XODdkO5mLgXQWFr2DPVRjA7K1MJqZ86SiHC",
    "sender_id":"FSTSMS",
    #Enter your message here(To add amazon product detail in future)
    "message":"",
    "language":"english",
    "route":"p",
    #Enter the mobile numebr here
    "numbers":""
}

headers = {"cache-control":"no-cache"}

response = requests.request("GET",url, headers=headers, params=my_data)
print(response.text)