import json
import pickle
import pprint

# gets input contact info from user and adds the contact(dict) to the contact "database"(list)
def add_contact(lst):
    first_name = input('First name: ')
    last_name = input('Last name: ')
    phone = input('phone: ')
    d = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
    }
    lst.append(d)

# deletes the last item from a list
def delete_last_contact(lst):
    del lst[-1]


# gets the contact list and a name from the user and prints the contact info connected to that name
def lookup_by_name(lst, name):
    for contact in lst:
        if contact['first_name'] == name:
            print(contact)
            return
    print('No contact with that name')


# gets the contacts list and a name from the user and delete the contact info connected to that name
def delete_contact_by_name(lst, name):
    for i in range(len(lst)):
        if lst[i]['first_name'] == name:
            del lst[i]
            break

# saves the contact "Database" (list) to a json or pickle file (object)
def save(lst, selection):
    data = {'contacts': lst}
    if selection == 'j':
        with open('contacts.json', 'w') as f:
            json.dump(data, f)
    else:
        with open('contacts.pickle', 'wb') as f:
            pickle.dump(data, f)

# pretty prints the contact info
def print_contacts(data):
    pprint.pprint(data)


start_menu = """
j - load contacts from json file
p - load contacts from pickle file
r - rewrite contacts files
"""

menu = """
a - add contact
dl - delete last contact
dn - delete contact by name
l - lookup contact by name
p - print contacts
x - save and exit
"""

sub_menu = """
j - save as json
p - save as pickle
"""


def main():
    print(start_menu)
    start_selection = input("Enter selection: ")
    if start_selection == 'j':
        with open('contacts.json', 'r') as f:
            data = json.load(f)
    elif start_selection == 'p':
        with open('contacts.pickle', 'rb') as f:
            data = pickle.load(f)
    else:
        data = {'contacts': []}
    while True:
        print(menu)
        selection = input("Your selection: ")
        if selection == 'a':
            add_contact(data['contacts'])
        if selection == 'dl':
            delete_last_contact(data['contacts'])
        if selection == 'dn':
            delete_contact_by_name(data['contacts'], input('Contact to delete: '))
        if selection == 'l':
            lookup_by_name(data['contacts'], input('Name to lookup: '))
        if selection == 'p':
            print_contacts(data)
        if selection == 'x':
            print(sub_menu)
            save_selection = input('save as: ')
            save(data['contacts'], save_selection)
            break


if __name__ == "__main__":
    main()
