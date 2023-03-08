import json
import pandas as pd

target_jsonl = "outputs/sample_jsonl.json"
print(">> using `json`")
with open(target_jsonl, "r") as file:
    people = [json.loads(line) for line in file.readlines()]
print(people)
print(">> using `pandas`")
people = pd.read_json(target_jsonl, lines=True)
print(people)
