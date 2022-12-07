import json # Importera JSON-modulen

persons = [
    { 'name': "Linus", "born": 1969, 'is_finnish': True },
    { 'name': "Grace", "born": 1906, 'is_finnish': False  }
]



print(persons)
print(json.dumps(persons))
print(json.dumps(persons, indent=1))

# JSON-formaterad teckensträng
persons_json = '[{"name": "Linus", "born": 1969, "is_finnish": true}, {"name": "Grace", "born": 1906, "is_finnish": false}]'

persons_back_to_python = json.loads(persons_json)
for person in persons_back_to_python:
    print(person)