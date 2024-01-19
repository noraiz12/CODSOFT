# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 00:42:23 2024

@author: PMLS
"""

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

    def view_contact_list(self):
        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}\tPhone: {contact.phone_number}")

    def search_contact(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == old_name:
                self.contacts[i] = new_contact
                print(f"Contact {old_name} updated successfully.")
                return
        print(f"Contact {old_name} not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(query)
            if found_contacts:
                print("\nFound Contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}\tPhone: {contact.phone_number}")
            else:
                print("No contacts found.")

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name (press Enter to keep the same): ")
            new_phone = input("Enter new phone number (press Enter to keep the same): ")
            new_email = input("Enter new email (press Enter to keep the same): ")
            new_address = input("Enter new address (press Enter to keep the same): ")

            for contact in contact_book.contacts:
                if contact.name == old_name:
                    new_contact = Contact(
                        new_name if new_name else contact.name,
                        new_phone if new_phone else contact.phone_number,
                        new_email if new_email else contact.email,
                        new_address if new_address else contact.address
                    )
                    contact_book.update_contact(old_name, new_contact)
                    break
            else:
                print(f"Contact {old_name} not found.")

        elif choice == '5':
            name_to_delete = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name_to_delete)

        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
