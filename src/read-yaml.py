import yaml

target_yaml = "outputs/sample_yaml.yaml"
with open(target_yaml, "r") as file:
    people = yaml.safe_load(file)
print(people)
