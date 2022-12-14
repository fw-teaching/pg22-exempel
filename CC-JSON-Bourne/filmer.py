import json

with open('filmer.json') as filen:
    filmer = json.loads(filen.read())

for film in filmer:
    print(f"{film['title']} får {film['stars']} stjärnor {film['stars'] * '*'}")

if input("Lägg till ny film? (y/n) ") == "y":
    ny_title = input("Filmens titel: ")
    ny_stars = input("Hur många stjärnor? ")

    filmer.append({
        "title": ny_title,
        "stars": int(ny_stars)
    })

with open('filmer.json', 'w') as filen:
    filmer_json = json.dumps(filmer, indent=2)
    filen.write(filmer_json)