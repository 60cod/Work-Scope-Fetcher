# config.py

# 기간 설정
PERIOD_START = "2025-01-01"
PERIOD_END = "2025-06-30"

# Jira 설정
JIRA_URL = "https://my-domain.atlassian.net"
JIRA_AUTH = ("ygna@email.com", "jira-api-token")

# GitHub 설정
GITHUB_TOKEN = "my-github-token"
GITHUB_USERNAME = "my-github-username"

# Google Drive 설정
import pickle
try:
    with open(".googleapi/token.pickle", "rb") as token:
        GOOGLE_CREDS = pickle.load(token)  # google-auth credentials 객체 (token.json 등으로 초기화 필요)
except FileNotFoundError:
    GOOGLE_CREDS = None