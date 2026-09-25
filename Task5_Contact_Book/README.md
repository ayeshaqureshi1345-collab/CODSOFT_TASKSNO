# Contact Book

## Description

This is a simple Python Contact Book application that allows users to manage their contacts. Users can add, view, search, update, and delete contacts.

The contacts are stored in a JSON file so that they can be saved and accessed again when the program is run.

## Features

* Add a new contact
* View all contacts
* Search for a contact
* Update contact details
* Delete a contact
* Save contacts using a JSON file
* Simple menu-based interface

## Technologies Used

* Python
* JSON
* File Handling

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python contact_book.py
```

4. Select an option from the menu.

## Example

```text
===== CONTACT BOOK =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 1
Enter name: Ayesha
Enter phone number: 9876543210
Enter email: ayesha@example.com

Contact added successfully!
```

## Data Storage

Contacts are stored in the `contacts.json` file. The file is automatically created when a contact is added.
