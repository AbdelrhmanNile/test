import os
from github import Github

# Initialize GitHub client
g = Github(os.getenv("GITHUB_TOKEN"))

# Constants
REPO_NAME = "Abdelrhmannile/test"  # Replace with your repository
TODO_ISSUE_NUMBER = 1  # Replace with your TODO list issue number

# Get the repository and TODO issue
repo = g.get_repo(REPO_NAME)
todo_issue = repo.get_issue(number=TODO_ISSUE_NUMBER)

# Get the latest comment
comments = todo_issue.get_comments()
latest_comment = comments[-1].body

# Example parsing logic (customize as needed)
for line in latest_comment.splitlines():
    if line.startswith("#"):  # Simple way to find issue references; adjust as needed
        issue_number = int(line[1:])
        referenced_issue = repo.get_issue(number=issue_number)
        todo_issue.edit(
            body=f"{todo_issue.body}\n- [ ] {referenced_issue.title} #{issue_number}"
        )

print("TODO list updated with referenced issues.")
