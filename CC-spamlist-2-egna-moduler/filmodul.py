
# Egen modul med egna funktioner. Importera i med: import filmodul

def read_file(file_name):
    '''Funktion för att läsa filer'''
    with open(file_name) as f:
        return f.read()

def write_file(file_name, text_to_write):
    '''Funktion för att skriva filer'''
    with open(file_name, 'w') as f: 
        f.write(text_to_write)



