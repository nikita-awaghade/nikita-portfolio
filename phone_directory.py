# Dictionary to store phone directory data
phone_directory = {}


def show_menu():
    print("\n--- PHONE DIRECTORY MENU ---")
    print("1. Add/Update Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Delete Contact")
    print("5. Exit")


while True:
    show_menu()
    choice = input("\nEnter choice (1-5): ")

    # 1. Add or Update Contact
    if choice == '1':
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        if name in phone_directory:
            print(f"Updating existing contact for {name}.")

        phone_directory[name] = phone
        print("Contact saved successfully!")

    # 2. Search Contact
    elif choice == '2':
        name = input("Enter name to search: ").strip()

        if name in phone_directory:
            print(f"Found -> Name: {name}, Phone: {phone_directory[name]}")
        else:
            print("Contact not found!")

    # 3. View All Contacts
    elif choice == '3':
        if not phone_directory:
            print("Directory is empty!")
        else:
            print("\n--- ALL CONTACTS ---")

            for name, phone in phone_directory.items():
                print(f"{name} : {phone}")

    # 4. Delete Contact
    elif choice == '4':
        name = input("Enter name to delete: ").strip()

        if name in phone_directory:
            del phone_directory[name]
            print(f"Contact for {name} deleted successfully!")
        else:
            print("Contact not found!")

    # 5. Exit
    elif choice == '5':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please select a number between 1 and 5.")