import requests

url = "http://work-bench.znseed.top/SSO-SERVER/authentication/form"

payload="{\"username\":\"swagger\",\"password\":\"swagger\"}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
token = 'bearer' + ' ' +response.json()['data']['tokenInfo']['token']
print(token)