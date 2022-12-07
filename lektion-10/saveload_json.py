import json

# Läs json-fil
with open('persons.json') as f:
    persons_json = f.read()
    persons = json.loads(persons_json) # Omvandla till Python-objekt

# Nu kan Python använda vårt objekt
for person in persons:
    print(f"{person['name']} föddes {person['born']}")

if input("skapa ny person? (y/n)") == 'y':
    new_name = input("Skriv in en ny person (namn): ")
    new_born = int(input("Personens födelseår: "))
    persons.append({ 'name': new_name, 'born': new_born })

# Skriv json-fil
with open('persons.json', 'w') as f: # Öppna för att skriva över ('w')
    persons_json = json.dumps(persons, indent=2) # Konvertera python-data till json
    f.write(persons_json) # Skriv filen




