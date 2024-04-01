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

comment_id = os.getenv("COMMENT_ID")

if comment_id:
    comment = todo_issue.get_comment(int(comment_id))
    comment.delete()
    for line in comment.body.splitlines():
        if line.startswith(
            "#"
        ):  # Simple way to find issue references; adjust as needed
            issue_number = int(line[1:])
            referenced_issue = repo.get_issue(number=issue_number)
            todo_issue.edit(
                body=f"{todo_issue.body}\n- [ ] {referenced_issue.title} #{issue_number}"
            )

    # Delete the comment
    comment.delete()

print("TODO list updated successfully.")
