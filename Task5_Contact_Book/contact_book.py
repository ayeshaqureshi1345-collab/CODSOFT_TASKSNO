import json

FILE_NAME = "contacts.json"

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("Contact added seccessfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- All Contacts ---")

        for name, details in contacts.items():
            print("Name:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("-------------------")

def search_contact(contacts):
    name = input("Enter name to search: ")

    if name in contacts:
        print("\nContact found!")
        print("Name:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter name to update: ")

    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")

        contacts[name]["phone"] = phone
        contacts[name]["email"] = email

        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n===== MY CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Thank you for using Contact Book!😊")
            break

        else:
            print("Invalid choice. Please try again.")

main()

