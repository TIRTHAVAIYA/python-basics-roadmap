contact_book = {}

def add_contact(name , number):
    contact_book[name] = number
    print(f"Contact '{name} added/updated.")

def view_contact(name):
    number = contact_book.get(name,"contact not found.")    
    print(f"Contact Name: {name},Number :{number}")

def view_all():
    if contact_book:
        print("\n --- ALL CONTACTS ---")
        for name , number in contact_book.items():
            print(f"{name}: {number}")
    else:
        print("Contact book is empty")            


 ## user interaction 

print("\n SIMPLE CONTACT BOOK")    
while True:
    action = input("Enter 'add' , 'view', 'all' , or 'done': ").lower()

    if action == 'add':
        name = input("Enter contact name :")
        number = input("Enter phone number: ")
        add_contact(name,number)
    elif action == 'view':
        name = input("Enter contact name to view:")
        view_contact(name)
    elif action == 'all':
        view_all() 
    elif action == 'done':
        print("Exiting contact book")
        break
    else:
        print("Invalid command.")