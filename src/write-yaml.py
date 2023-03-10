import yaml

target_yaml = "outputs/sample_yaml.yaml"
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
with open(target_yaml, "w") as file:
    yaml.dump(people, file)
