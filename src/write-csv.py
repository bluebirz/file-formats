import csv

target_csv = "outputs/sample_csv.csv"
header = ["id", "first_name", "last_name", "occupation"]
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
with open(target_csv, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for p in people:
        writer.writerow(p)
