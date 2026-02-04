import json
from inventory.schema import json

def test_schema_loads():
    with open("inventory/schema.json") as f:
        schema = json.load(f)

    assert schema["type"] == "object"
