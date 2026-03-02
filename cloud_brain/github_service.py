import os

class GitHubService:
    def __init__(self, token=None):
        self.token = token or os.getenv("GITHUB_TOKEN")

    def create_branch(self, branch_name):
        print(f"Creating GitHub branch: {branch_name}")
        return {"status": "success", "branch": branch_name}

    def commit_change(self, branch_name, file_path, content, message):
        print(f"Committing to {branch_name}: {message}")
        return {"status": "success", "commit_sha": "abc12345"}

    def create_pull_request(self, title, body, head, base="main"):
        print(f"Creating PR from {head} to {base}: {title}")
        return {"status": "success", "pr_number": 42}
