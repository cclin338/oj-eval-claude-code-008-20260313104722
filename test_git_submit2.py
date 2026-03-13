#!/usr/bin/env python3
import requests
import os

token = os.environ.get("ACMOJ_TOKEN")

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "ACMOJ-Python-Client/2.2"
}

# Try various git formats
git_urls = [
    "https://github.com/cclin338/oj-eval-claude-code-008-20260313104722/blob/main/code/2276.mv",
    "https://github.com/cclin338/oj-eval-claude-code-008-20260313104722.git",
    "git@github.com:cclin338/oj-eval-claude-code-008-20260313104722.git",
]

for git_url in git_urls:
    data = {"language": "git", "code": git_url}
    url = "https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/2276/submit"
    
    print(f"\nTrying: {git_url}")
    response = requests.post(url, headers=headers, data=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code == 200:
        print("Success!")
        print("JSON:", response.json())
        break
