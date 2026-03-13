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

print("Code content (first 100 chars):", code_content[:100])
print("Code length:", len(code_content))

# Try with multipart/form-data
files = {"code": ("2276.mv", code_content, "text/plain")}
data = {"language": "mov"}
url = "https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/2276/submit"

print("\nTrying multipart form submission...")
response = requests.post(url, headers=headers, files=files, data=data)
print("Status:", response.status_code)
print("Response:", response.text)
