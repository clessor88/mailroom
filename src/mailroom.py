# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

donor_list = {
    ('lessor', 'crystal'): [10, 40, 25],
    ('harrison', 'mike'): [30, 40, 15],
    ('smith', 'john'): [10, 25],
    ('python', 'monty'): [42],
}


def sort_donors(lst):
    """Turn donors into list and sorts in decending order."""
    sorted_donors = sorted(donor_list, key=lambda x: sum(donor_list[x]), reverse=True)
    new_list = []
    for k in sorted_donors:
        avg = float((sum(donor_list[k])) / len(donor_list[k]))
        donor_info = (k, donor_list[k], avg, )
        new_list.append(donor_info)
    return new_list


def prettyfy(lst):
    """"Take a list and print out a petty series of strings."""
    print(('Name' + ' ' * 16)+'||'+('History'+' '*13)+'||'+'Avg Donation')
    for item in lst:
        name = ("{}, {}".format(item[0][0].capitalize(), item[0][1].capitalize())+" "*10)[:20]
        history = ((str(item[1]))[1:-1] + (' ' * 40))[:20]
        avg = str(round(float(item[2]), 2))
        print(name + '||' + history + '||' + avg)
    welcome_prompt()


def get_list():
    """Loop through dictionary and print names."""
    for key in donor_list:
        print("{},{}".format(key[0], key[1]))
    return validate_last_name(get_last_name())


def get_first_name():
    """Get first name."""
    return input(u"Please enter first name:")


def validate_first_name(first_name):
    """Validate first name."""
    if first_name.isalpha():
        return first_name
    else:
        print(u'Please type only letters')
        return validate_first_name(get_first_name())


def get_last_name():
    """Get Last name from input."""
    return input(u"Please enter last name, or type list for list of donors:")


def validate_last_name(last_name):
    """Validate last name to be valid."""
    if last_name.isalpha():
        if last_name.lower() == 'list':
            return get_list()
        elif last_name.lower() == 'q':
            return welcome_prompt()
        else:
            return last_name
    else:
        print(u'Please type only letters')
        return validate_last_name(get_last_name())


def get_amount():
    """Get amount of donation."""
    return input(u"Please enter donation amount:")


def validate_amt(amt):
    """Validate if amt is a number."""
    if amt.isdigit():
        return int(amt)
    else:
        print(u'Please enter only numbers')
        return validate_amt(get_amount())


def add_info_and_email():
    """Call gets funcs and validates them. Add to dict and print."""
    last = validate_last_name(get_last_name())
    first = validate_first_name(get_first_name())
    amount = validate_amt(get_amount())
    if (last, first) in donor_list:
        donor_list[(last, first)].append(amount)
    else:
        donor_list.setdefault((last, first), [amount])
    print(u"Thank you, {} {}, for your generous donation of {}!".format(first, last, amount))
    welcome_prompt()


def welcome_prompt():
    """Begining welcome prmpt."""
    choice = input(u"WELCOME! Press 1 to send a thank you, press 2 to view report, or 'q' to return to beginning:")
    if choice == '1' or choice == 1:
        add_info_and_email()
    elif choice == '2' or choice == 2:
        prettyfy(sort_donors(donor_list))
    elif choice == 'q' or choice == 'Q':
        return
    else:
        print(u'Invalid choice, please try again')
        welcome_prompt()


if __name__ == "__main__":
    welcome_prompt()
