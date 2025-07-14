agenda = {} #creamos un diccionario vacio

def add_contact(name, phone, email):
  agenda[name] = {"phone": phone, "email": email} #agregamos un contacto al diccionario
  
def search_contact(name):
    return agenda.get(name, "Contact not found") #buscamos un contacto por nombre

def show_contacts():
    for name, info in agenda.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}") #mostramos todos los contactos
        
#test

add_contact("Alice", "123-456-7890", "alice@example.com")
add_contact("Bob", "987-654-3210", "bob@example.com")
print(search_contact("Ruben")) #deberia mostrar Not Found
print(search_contact("Alice")) #deberia mostrar el contacto de Alice
show_contacts()