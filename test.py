from github import Github
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '976ffeca822450a37a6b')
g = Github(token)
repo = g.get_repo("vultorio67/alpha67_plugin")
#issues = repo.get_issues(state="open")
pprint(issues.get_page(0))