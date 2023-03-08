import json
import pandas as pd

target_json = "outputs/sample_json.json"
print(">> using `json`")
with open(target_json, "r") as file:
    people = json.load(file)
print(people)
print(">> using `pandas`")
people = pd.read_json(target_json)
print(people)
