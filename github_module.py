# github_module.py

import requests

def get_my_prs(token, start, end):
    headers = {"Authorization": f"token {token}"}
    query = f"author:USERNAME type:pr created:{start}..{end}"
    url = "https://api.github.com/search/issues"
    res = requests.get(url, headers=headers, params={"q": query})
    items = res.json().get("items", [])
    return [(pr["title"], pr["html_url"]) for pr in items]
