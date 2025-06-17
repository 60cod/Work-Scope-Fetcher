# jira_module.py

from jira import JIRA

def get_my_issues(jira_url, auth, start, end):
    jira = JIRA(jira_url, basic_auth=auth)
    jql = f'assignee=currentuser() AND updated>="{start}" AND updated<="{end}"'
    issues = jira.search_issues(jql, fields="summary,key")
    return [(i.fields.summary, f"{jira_url}/browse/{i.key}") for i in issues]
