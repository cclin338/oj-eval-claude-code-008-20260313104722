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

# Try different language names
for lang in ["mov", "MOV", "Mov", ".mv", "movlang"]:
    data = {"language": lang, "code": code}
    url = "https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/2276/submit"
    
    print(f"\nTrying language: {lang}")
    response = requests.post(url, headers=headers, data=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code == 200:
        break
