import json

INPUT_FILE = 'input.json'


def task(filename) -> float:
    with open(filename) as file:
        json_data = json.load(file)

    composition = [item['weight'] * item['score'] for item in json_data]
    amount = round(sum(composition), 3)
    return amount


print(task(INPUT_FILE))
