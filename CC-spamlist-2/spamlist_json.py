import json

with open('emails.json') as f:
    marketing_data_json = f.read()

emails_list = json.loads(marketing_data_json) # konvertera JSON till python-objekt
fixed_emails_list = [] # Skapa tom lista för de korrekta och fixade email-adresserna

for email in emails_list: # Loopa igenom hela marketing_data-listan
  email = email.lower().strip() # Ändra vaje till små bokstäver och ta bort onödiga mellanslag och radbryt

  if "@arcada.fi" in email: # Finns @arcada.fi i den email vi just nu kollar?
    fixed_emails_list.append(email) # Lägg till vår fixade lista

fixed_emails_list.sort() # Sortera i alfabetisk ordning
fixed_emails_json = json.dumps(fixed_emails_list, indent=2) # Konvertera till JSON så att det går att spara i en fil

with open('refined_emails.json', 'w') as f:
    f.write(fixed_emails_json)
