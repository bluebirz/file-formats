import json

target_jsonl = "../outputs/sample_jsonl.json"
people = [
    {
        "id": 1,
        "first_name": "Kenneth",
        "last_name": "Farrell",
        "occupation": "Product manager",
    },
    {
        "id": 2,
        "first_name": "Kimberly",
        "last_name": "Hood",
        "occupation": "Social worker",
    },
]
with open(target_jsonl, "w") as file:
    for p in people:
        file.writelines(json.dumps(p) + "\n")
