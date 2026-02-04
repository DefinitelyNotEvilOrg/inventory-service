def collect_repo_metadata(repo):
    return {
        "name": repo.get("name"),
        "archived": repo.get("archived"),
        "visibility": repo.get("visibility"),
        "default_branch": repo.get("default_branch"),
    }
