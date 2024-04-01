name: Sync TODO list with Issues

on:
  issue_comment:
    types: [created]

jobs:
  sync-todo-list:
    if: github.event.issue.number == 1 # Replace 1 with your TODO list issue number
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repo
      uses: actions/checkout@v2

    - name: Set up Python 3.8
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install PyGithub

    - name: Update TODO list
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        COMMENT_ID: ${{ github.event.comment.id }}
      run: python .github/scripts/update_todo_list.py
