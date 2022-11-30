# läsa textfil från datorn (samma katalog)
with open('min-fil.txt') as my_file:
    my_file_content = my_file.read()

print(my_file_content)

# Skriva textfil (skapa ny eller skriv över)
with open('ny-fil.txt', 'w') as f: # Öppna för att skriva över ('w')
    f.write('Detta har vi skrivit via Python')

# Lägg till nytt innehåll till befintlig fil
with open('ny-fil.txt', 'a') as f: # Öppna för att lägga till ('a' = append)
    f.write(' och detta har vi lagt till senare') 

