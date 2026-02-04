from inventory.collector import collect_repo_metadata

def test_collector_keys():
    sample = {
        "name": "example",
        "archived": False,
        "visibility": "public",
        "default_branch": "main"
    }

    result = collect_repo_metadata(sample)

    assert "name" in result
    assert "visibility" in result
