# WorkScopeFetcher

**WorkScopeFetcher**는 지정된 기간 동안 사용자의 업무 활동 이력을 다음 3가지 출처에서 자동 수집하여 정리된 보고서 파일로 출력하는 Python 기반 도구입니다.

- 📌 Jira: 사용자가 담당자로 지정된 이슈
- 📌 GitHub: 사용자가 생성한 Pull Request
- 📌 Google Drive: 공유 드라이브 내에서 사용자가 수정한 적 있는 파일

---

## 💡 사용 목적

개인 업무 리뷰를 위해 **사용자가 실제 수행한 작업 내역을 자동으로 수집**합니다.

---

## 📁 프로젝트 구조

```
WorkScopeFetcher/
├── main.py                  # 실행 진입점 (출력 파일 생성)
├── config.py                # 인증 정보 및 조회 기간 설정
├── jira_module.py           # Jira 이슈 추출
├── github_module.py         # GitHub PR 추출
├── gdrive_module.py         # Google Drive 파일 추출
├── output/                  # 결과 파일 저장 경로
└── requirements.txt         # 설치해야 할 패키지 목록
```

---

## ⚙️ 환경 설정

### 1. Python 가상환경 생성 (권장)

```bash
python -m venv .venv
source .venv/bin/activate     # Windows는 .venv\Scripts\activate
```

### 2. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. `config.py` 설정

- 토큰 발급하여 입력
  - Jira API Token
  - Github Personal Access Token (권한: repo)
- Google Drive 인증 -> token.pickle 경로 설정

---

## 🔐 Google Drive 인증

### 1. Google Cloud Project 생성

### 2. Drive API 사용 설정

### 3. OAuth 클라이언트 ID 생성

- Google Cloud Console → 사용자 인증 정보 → 데스크톱 앱용 OAuth 2.0 생성
- `credentials.json` 다운로드

### 4. 최초 1회 인증 (token.pickle 생성)

- `credentials.json` 파일이 있는 경로에서 아래 코드 실행
- 생성된 token.pickle 파일을 .googleapi 폴더 하위로 이동

```python
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
creds = flow.run_local_server(port=0)

with open("token.pickle", "wb") as token:
    pickle.dump(creds, token)
```

---

## ▶️ 실행 방법

```bash
python main.py
```

- `/output` 디렉토리에 `output_YYYYMMDD_HHMM.txt` 형식의 결과 파일이 생성됩니다.
- 출력에는 다음이 포함됩니다:
  - 조회 기간
  - Jira 이슈 목록
  - GitHub PR 목록
  - Google Drive 공유 드라이브 내 본인이 수정한 파일 목록

---

## 📌 유의사항

- Jira: 본인이 assignee로 지정된 이슈만 조회됨
- GitHub: private repo 접근을 위해 PAT에 `repo` scope 포함 필요
- Google Drive: 공유 드라이브에서 조회됨 (`driveId` 필터링)

---

## ✅ 향후 개선 아이디어

- 조회 항목 확대
- 조회 기간과 항목을 인자로 입력하여 실행 가능
- 출력 결과를 HTML/CSV 보고서로 저장
- Notion, Google Sheets 등과 연동
- 주간 자동 실행 (cron, Task Scheduler)
