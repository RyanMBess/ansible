import requests
import json

url = "https://10.10.20.60/smc-configuration/rest/v1/tenants/301/tags/"

payload = [
  {
    "name": "Ryan111111",
    "location": "OUTSIDE",
    "description": "A sample of a threat feed",
    "ranges": [
      "149.202.170.60",
      "23.129.64.101",
      "37.187.129.166",
      "91.146.121.3"
    ],
    "hostBaselines": False,
    "suppressExcludedServices": True,
    "inverseSuppression": False,
    "hostTrap": False,
    "sendToCta": False,
    "parentId": 0
  }
]
headers = {
  'Cookie': 'XSRF-TOKEN=ab64b033-a12b-4316-9e44-4a3c007d767c',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, verify=False, headers=headers, data=json.dumps(payload))

print(response.text)