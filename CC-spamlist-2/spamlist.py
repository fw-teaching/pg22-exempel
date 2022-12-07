
with open('emails.txt') as f:
    secret_marketing_data = f.read()

emails_list = secret_marketing_data.split(";") # Omvandla strängen till list, splitta vid varje semikolon
fixed_emails_list = [] # Skapa tom lista för de korrekta och fixade email-adresserna

for email in emails_list: # Loopa igenom hela marketing_data-listan
  email = email.lower().strip() # Ändra vaje till små bokstäver och ta bort onödiga mellanslag och radbryt

  if "@arcada.fi" in email: # Finns @arcada.fi i den email vi just nu kollar?
    fixed_emails_list.append(email) # Lägg till vår fixade lista

fixed_emails_list.sort() # Sortera i alfabetisk ordning
fixed_emails = ", ".join(fixed_emails_list) # Joina ihop till en ny kommaseparerad teckensträng

print(fixed_emails)

with open('refined_emails.txt', 'w') as f:
    f.write(fixed_emails)

# Skriv ut fixed_emails i filen refined.txt