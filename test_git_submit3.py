#!/usr/bin/env python3
import requests
import os

token = os.environ.get("ACMOJ_TOKEN")
git_url = "https://github.com/cclin338/oj-eval-claude-code-008-20260313104722"

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "ACMOJ-Python-Client/2.2"
}

data = {"language": "git", "code": git_url}
url = "https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/2276/submit"

print("Trying git submission with file at root...")
response = requests.post(url, headers=headers, data=data)
print("Status:", response.status_code)
print("Response:", response.text)
if response.status_code == 200:
    print("Success!")
    import json  
    result = response.json()
    print("JSON:", json.dumps(result, indent=2))
    if 'id' in result:
        print(f"\n✅ Submission ID: {result['id']}")
        print("Use this command to check status:")
        print(f"python3 submit_acmoj/acmoj_client.py --token $ACMOJ_TOKEN status --submission-id {result['id']}")
