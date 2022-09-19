import subprocess
import json
from github import Github
from my_token import token
import time

g = Github(token)

repo_name = "Adafruit_CircuitPython_Display_Text"

full_name = "adafruit/{}".format(repo_name)
#full_name = "foamyguy/{}".format(repo_name)

print(full_name)

repo = g.get_repo(full_name)

repo_topics = repo.get_topics()
print("topics: {}".format(repo_topics))

#time.sleep(5)

if "hacktoberfest" in repo_topics:
    repo_topics.remove("hacktoberfest")
    repo.replace_topics(repo_topics)
    print("removed hacktoberfest")