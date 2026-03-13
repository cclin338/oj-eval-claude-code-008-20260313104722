#!/usr/bin/env python3
import requests
import os

token = os.environ.get("ACMOJ_TOKEN")
git_url = "https://github.com/cclin338/oj-eval-claude-code-008-20260313104722"

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "ACMOJ-Python-Client/2.2"
}

# Try git submission
data = {"language": "git", "code": git_url}
url = "https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/2276/submit"

print("Trying git submission...")
response = requests.post(url, headers=headers, data=data)
print("Status:", response.status_code)
print("Response:", response.text)
if response.status_code == 200:
    print("JSON:", response.json())
