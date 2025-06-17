# gdrive_module.py

from googleapiclient.discovery import build

def get_my_drive_files(creds, start, end):
    service = build('drive', 'v3', credentials=creds)
    query = (f"modifiedTime >= '{start}T00:00:00' and modifiedTime <= '{end}T23:59:59' "
             "and (owners me or lastModifyingUser me)")
    results = service.files().list(q=query, fields="files(id,name,webViewLink)").execute()
    return [(f["name"], f["webViewLink"]) for f in results.get("files", [])]
