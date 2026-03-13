#!/usr/bin/env python3
import requests
import json
import os

token = os.environ.get("ACMOJ_TOKEN")
with open("code/2276.mv", "r") as f:
    code = f.read()

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "User-Agent": "ACMOJ-Python-Client/2.2"
}

data = {"language": "mov", "code": code}
url = "https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/2276/submit"

print("Sending request to:", url)
print("Headers:", headers)
print("Data keys:", data.keys())
print("Code length:", len(code))

response = requests.post(url, headers=headers, json=data)
print("Status:", response.status_code)
print("Response:", response.text)
try:
    print("JSON:", response.json())
except:
    pass
