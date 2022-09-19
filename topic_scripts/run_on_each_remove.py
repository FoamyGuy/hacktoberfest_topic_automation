import subprocess
import json
from github import Github
from my_token import token
import time

g = Github(token)

result = subprocess.check_output(['gh', 'repo', 'view', '--json', 'name'])
result_obj = json.loads(result)

repo_name = result_obj["name"]

full_name = "adafruit/{}".format(repo_name)

print(full_name)

repo = g.get_repo(full_name)

repo_topics = repo.get_topics()
print("topics: {}".format(repo_topics))

time.sleep(5)

if "hacktoberfest" in repo_topics:
    repo_topics.remove("hacktoberfest")
    repo.replace_topics(repo_topics)
    print("removed hacktoberfest")