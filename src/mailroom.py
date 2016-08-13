# -*- coding: utf-8 -*-
donor_list = {
    ('lessor', 'crystal'): [10, 40, 25],
    ('harrison', 'mike'): [30, 40, 15],
    ('smith', 'john'): [10, 25],
    ('python', 'monty'): [42]
}


def sort_donors(donor_list):
    """Turn donors into list and sorts in decending order."""
    sorted_donors = sorted(donor_list, key=lambda x: sum(donor_list[x]), reverse=True)
    new_list = []
    for k in sorted_donors:
        donor_info = "{}: {}: {}".format(k, donor_list[k], float(sum(donor_list[k])) / len(donor_list[k]))
        new_list.append(donor_info)
    return new_list

# TODO - Create prettify donor_list


def get_list():
    """Loop through dictionary and print names."""
    for key in donor_list:
        print("{},{}}".format(key[0], key[1]))
    get_last_name()


def get_first_name():
    first_name = input("Please enter first name or type list for list of donors:")
    if first_name == first_name.isalpha():
        return first_name
    else:
        print('Please type only letters')
        get_first_name()


def get_last_name():
    last_name = input("Please enter last name:")
    if last_name == last_name.isalpha():
        if last_name.lower() == 'list':
            get_list()
        elif last_name.lower() == 'q':
            welcome_prompt()
        else:
            return last_name
    else:
        print('Please type only letters')
        get_last_name()


def get_amount():
    amt = input("Please enter donation amount:")
    if amt == amt.isnumeric():
        return amt
    else:
        print('Please enter only numbers')
        get_amount()


def add_info_and_email():
    tmp = {}
    tmp[(get_last_name(), get_first_name())] = [get_amount()]
    print("Thank you, {} {}, for your generous donation of {}!".format(list(tmp.keys())[0][0], list(tmp.keys())[0][1], list(tmp.values())[0]))
    donor_list.update(tmp)
    welcome_prompt()


def welcome_prompt():
    choice = input("WELCOME! Press 1 to send a thank you, press 2 to view report, or 'q' to return to beginning:")
    if choice == '1':
        add_info_and_email()
    elif choice == '2':
        sort_donors()
    elif choice.lower() == 'q':
        return
    else:
        print('Invalid choice, please try again')
        welcome_prompt()