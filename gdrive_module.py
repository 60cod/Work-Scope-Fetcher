# gdrive_module.py

from googleapiclient.discovery import build
from datetime import datetime

def get_my_drive_files(creds, start, end):
    service = build('drive', 'v3', credentials=creds)

    start_iso = f"{start}T00:00:00Z"
    end_iso = f"{end}T23:59:59Z"

    query = f"modifiedTime >= '{start_iso}' and modifiedTime <= '{end_iso}'"

    results = service.files().list(
        q=query,
        fields="files(id,name,webViewLink,driveId,modifiedByMeTime)",
        corpora="allDrives",
        includeItemsFromAllDrives=True,
        supportsAllDrives=True,
        pageSize=1000
    ).execute()

    def is_modified_by_me(file):
        mod_time = file.get("modifiedByMeTime")
        if not mod_time:
            return False
        try:
            mod_dt = datetime.fromisoformat(mod_time.replace("Z", "+00:00"))
            start_dt = datetime.fromisoformat(f"{start}T00:00:00+00:00")
            end_dt = datetime.fromisoformat(f"{end}T23:59:59+00:00")
            return start_dt <= mod_dt <= end_dt
        except Exception:
            return False

    files = results.get("files", [])
    return [
        (f["name"], f["webViewLink"])
        for f in files
        if "driveId" in f and is_modified_by_me(f)
    ]
