# main.py

from config import *
from jira_module import get_my_issues
from github_module import get_my_prs
from gdrive_module import get_my_drive_files

from datetime import datetime
import os

def main():
    # 출력 디렉토리 생성
    os.makedirs("output", exist_ok=True)

    # 파일명에 현재 날짜와 시간 추가
    now_str = datetime.now().strftime("%Y%m%d_%H%M")
    output_path = f"output/output_{now_str}.txt"

    with open(output_path, "w", encoding="utf-8") as out:
        # 조회 기간 출력
        out.write(f"[조회 기간] {PERIOD_START} ~ {PERIOD_END}\n\n")

        # Jira 이슈 출력
        out.write("=== Jira Issues ===\n")
        for title, link in get_my_issues(JIRA_URL, JIRA_AUTH, PERIOD_START, PERIOD_END):
            out.write(f"- {title} → {link}\n")

        # GitHub PR 출력
        out.write("\n=== GitHub PRs ===\n")
        for title, link in get_my_prs(GITHUB_TOKEN, GITHUB_USERNAME, PERIOD_START, PERIOD_END):
            out.write(f"- {title} → {link}\n")

        # Google Drive 파일 출력
        out.write("\n=== Google Drive Files ===\n")
        if GOOGLE_CREDS:
            for name, link in get_my_drive_files(GOOGLE_CREDS, PERIOD_START, PERIOD_END):
                out.write(f"- {name} → {link}\n")
        else:
            out.write("Google Drive 인증 정보가 없습니다.\n")

    print(f"✅ 결과가 저장되었습니다: {output_path}")

if __name__ == "__main__":
    main()
