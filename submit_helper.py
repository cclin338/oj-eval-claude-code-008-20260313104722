#!/usr/bin/env python3
import requests
import os
import sys
import time

if len(sys.argv) < 2:
    print("Usage: python3 submit_helper.py <problem_id>")
    sys.exit(1)

problem_id = sys.argv[1]
token = os.environ.get("ACMOJ_TOKEN")

with open(f"{problem_id}.mv", "r") as f:
    code_content = f.read()

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "ACMOJ-Python-Client/2.2"
}

data = {"language": "cpp", "code": code_content}
url = f"https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/{problem_id}/submit"

print(f"Submitting {problem_id}.mv...")
response = requests.post(url, headers=headers, data=data)
print(f"Status: {response.status_code}")

if response.status_code in [200, 201]:
    result = response.json()
    sub_id = result['id']
    print(f"✅ Submission ID: {sub_id}")
    
    # Wait and check status
    print("Waiting 5 seconds before checking status...")
    time.sleep(5)
    
    status_url = f"https://acm.sjtu.edu.cn/OnlineJudge/api/v1/submission/{sub_id}"
    status_resp = requests.get(status_url, headers=headers)
    if status_resp.status_code == 200:
        status_data = status_resp.json()
        print(f"Status: {status_data.get('status')}")
        print(f"Score: {status_data.get('score')}")
        if 'details' in status_data:
            print(f"Result: {status_data['details'].get('result')}")
        print(f"\nFull response: {status_resp.text}")
    else:
        print(f"Status check failed: {status_resp.text}")
else:
    print(f"Submission failed: {response.text}")
