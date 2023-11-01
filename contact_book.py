address_book = {}


def add_contact():
    name = input("Enter name:")
    phone = input("Enter phone:")
    town = input("Enter town:")
    address_book[name] = {"Phone": phone, "Town": town}
    print(f"Contact {name} has been added.")


def view_contact():
    if not address_book:
        print("There are not contacts here.")
    else:
        for name, details in address_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Town: {details['Town']}")
            print()


def search_contacts():
    name = input("Enter the name to search for:")

    if name in address_book:
        details = address_book[name]
        print(f"Name: {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Town: {details['Town']}")
    else:
        print(f"Contact {name} not found in the book.")


while True:
    print("\n Welcome to the address book!")
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Exit")

    my_choice = int(input("Enter a operation to do(1/2/3/4):"))

    if my_choice == 1:
        add_contact()
    elif my_choice == 2:
        view_contact()
    elif my_choice == 3:
        search_contacts()
    elif my_choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid command.Please enter a number 1, 2, 3 or 4.")
