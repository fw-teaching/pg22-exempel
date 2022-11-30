# Funktion för att läsa filer
def read_file(file_name):
    with open(file_name) as f:
        return f.read()

# Funktion för att skriva filer
def write_file(file_name, text_to_write):
    with open(file_name, 'w') as f: # Öppna för att skriva över ('w')
        f.write(text_to_write)

##########################

write_file('nyare-fil.txt', 'skriven med vår nya funktion.')

# Läs fil genom att anopa funktionen
innehall = read_file('min-fil.txt')
print(innehall)

# Nu kan vi läsa andra filer med samma funktion!
print(read_file('nyare-fil.txt'))
