#!/usr/bin/env python3
import requests
import os

token = os.environ.get("ACMOJ_TOKEN")
with open("code/2276.mv", "r") as f:
    code = f.read()

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "ACMOJ-Python-Client/2.2"
}

# Try with form data
data = {"language": "mov", "code": code}
url = "https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/2276/submit"

print("Trying with form data...")
response = requests.post(url, headers=headers, data=data)
print("Status:", response.status_code)
print("Response:", response.text)
