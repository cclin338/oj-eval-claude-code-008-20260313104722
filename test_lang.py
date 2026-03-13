#!/usr/bin/env python3
import requests
import os

token = os.environ.get("ACMOJ_TOKEN")

# Simple test code
code_content = "print('hello')"

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "ACMOJ-Python-Client/2.2"
}

# Try known language to see if submission works at all
for lang in ["python3", "cpp", "c", "java", "python"]:
    data = {"language": lang, "code": code_content}
    url = "https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/2276/submit"
    
    print(f"\nTrying language: {lang}")
    response = requests.post(url, headers=headers, data=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}")
    if response.status_code == 200:
        print("✅ This language works!")
        break
