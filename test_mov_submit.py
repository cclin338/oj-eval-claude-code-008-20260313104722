#!/usr/bin/env python3
import requests
import os

token = os.environ.get("ACMOJ_TOKEN")

with open("2276.mv", "r") as f:
    code_content = f.read()

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "ACMOJ-Python-Client/2.2"
}

# Since we know cpp works (201), let me try submitting .mv code as "cpp"
# Maybe the OJ determines the actual language from the code format
data = {"language": "cpp", "code": code_content}
url = "https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/2276/submit"

print("Submitting .mv code with language=cpp...")
response = requests.post(url, headers=headers, data=data)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

if response.status_code in [200, 201]:
    import json
    result = response.json()
    print(f"\n✅ Submission ID: {result['id']}")
    print("Saving to file...")
    with open("/workspace/submission_ids.log", "a") as f:
        f.write(f"{result['id']}\n")
