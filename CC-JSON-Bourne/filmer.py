import json

with open('filmer.json') as filen:
    filmer = json.loads(filen.read())

for film in filmer:
    # Ternary expression:
    verdict = "Den är bra." if film['stars'] > 2 else "Den suger."

    print(f"{film['title']} får {film['stars']} stjärnor {film['stars'] * '*'} {verdict}")

if input("Lägg till ny film? (y/n) ") == "y":
    ny_title = input("Filmens titel: ")
    ny_stars = input("Hur många stjärnor? ")

    filmer.append({
        "title": ny_title,
        "stars": int(ny_stars)
    })

with open('filmer.json', 'w') as filen: # w = write
    filmer_json = json.dumps(filmer, indent=2)
    filen.write(filmer_json)