import json

target_json = "sample_json.json"
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
with open(target_json, "w") as file:
    file.write(json.dumps(people, indent=2))
