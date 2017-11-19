import json

json_data = open('전국금연구역표준데이터.json', encoding='utf-8').read()

data = json.loads(json_data)
print(data)
