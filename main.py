# main.py

from config import *
from jira_module import get_my_issues
from github_module import get_my_prs
from gdrive_module import get_my_drive_files

def main():
    print("=== Jira Issues ===")
    for title, link in get_my_issues(JIRA_URL, JIRA_AUTH, PERIOD_START, PERIOD_END):
        print(f"- {title} → {link}")

    print("\n=== GitHub PRs ===")
    for title, link in get_my_prs(GH_TOKEN, PERIOD_START, PERIOD_END):
        print(f"- {title} → {link}")

    print("\n=== Google Drive Files ===")
    if GOOGLE_CREDS:
        for name, link in get_my_drive_files(GOOGLE_CREDS, PERIOD_START, PERIOD_END):
            print(f"- {name} → {link}")
    else:
        print("Google Drive 인증 정보가 없습니다.")

if __name__ == "__main__":
    main()
