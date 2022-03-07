# Create empty global dictionary
PHONEBOOK = {}


def display_menu():
    # Display phone book options to user
    print('------------------------')
    print('1. Create a New Contact')
    print('2. Display Existing Contacts')
    print('3. Search for a contact')
    print('4. Update a contact')
    print('5. Delete a contact')
    print('6. Exit')
    print('------------------------')


def contact_information():
    # Have user enter contact information
    print('------------------------')
    print('Creating Contact - Please Enter information')
    while True:
        check = input('Name: ')
        # Change the name into lowercase
        name = check.lower()
        number = input('Enter Number: ')
        if name and number:
            print('Contact made')
            return name, number


def create_contact(name, number):
    # Create contact in phone book
    PHONEBOOK[name] = number


def display_phonebook():
    # Display contact entries
    if not any(PHONEBOOK):
        print('No Contacts')
        
    # Print phone book contacts
    print('Displaying Contacts')
    for name, number in sorted(PHONEBOOK.items()):
        print()
        print(f'Name: {name.title()}')
        print(f'Number: {number}')
        print('------------------------')


def search_contact():
    # Search for contacts in dictionary
    # Look up contact by name
    check = input('Enter contact name: ')
    # Convert contact name to lowercase
    name = check.lower()
    print('Searching Contacts...')
    if name in PHONEBOOK:
        print(f'Number: {PHONEBOOK[name]}')
    else:
        print('Contact not Found')


def update_contact():
    # Update contact information
    check = input('Enter contact name: ')
    name = check.lower()
    if name in PHONEBOOK:
        number = input('Enter new number: ')
        print('Updating Contact...')
        PHONEBOOK[name] = number
        print('Contact Updated')
    else:
        print('Contact not Found')


def delete_contact():
    # Remove contact entry
    check = input('Enter contact name: ')
    name = check.lower()
    if name in PHONEBOOK:
        print('Deleting Contact...')
        PHONEBOOK.pop(name)
        print('Contact Removed')
    else:
        print('Contact not Found')


def main():
    while True:
        # Display menu and ask for selection
        display_menu()
        option = input('Choose an option: ')
        # Check for valid entry
        if option.isnumeric():
            choice = int(option)
        else:
            continue
        # Menu choices
        # Create Contact
        if choice == 1:
            name, number = contact_information()
            create_contact(name, number)
        # Disply Contacts
        if choice == 2:
            display_phonebook()
        # Search for a Contact
        if choice == 3:
            search_contact()
        # Update a Contact
        if choice == 4:
            update_contact()
        # Delete a contact
        if choice == 5:
            delete_contact()
        # Exit
        if choice == 6:
            break


main()
