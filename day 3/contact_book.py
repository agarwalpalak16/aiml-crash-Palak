contacts = [
    {"name": "Alex", "phone": "9876543210", "email": "alex@gmail.com"},
    {"name": "Rahul", "phone": "9876543211", "email": "rahul@gmail.com"},
    {"name": "Priya", "phone": "9876543212", "email": "priya@gmail.com"},
    {"name": "Riya", "phone": "9876543213", "email": "riya@gmail.com"},
    {"name": "Yash", "phone": "9876543214", "email": "yash@gmail.com"}
]

def find_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    return "Contact not found"

search = input("Enter contact name: ")

print(find_contact(search))