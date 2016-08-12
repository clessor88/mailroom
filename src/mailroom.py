# -*- coding: utf-8 -*-


def sort_donors(donor_dict):
    """Turn donors into list and sorts in decending order."""
    sorted_donors = sorted(donor_dict, key=lambda x: sum(donor_dict[x]), reverse=True)
    new_list = []
    for k in sorted_donors:
        donor_info = "{}: {}: {}".format(k, donor_dict[k], float(sum(donor_dict[k])) / len(donor_dict[k]))
        new_list.append(donor_info)
    return new_list

# TODO - Create prettify donor_list


def get_list(dictionary):
    """Loop through dictionary and print names."""
    for key in dictionary:
        print("{},{}}".format(key[0], key[1]))
    donor_name(dictionary)


def donor_name(dictionary):
    """Get Full Name and Donation Amount."""
    first_name = input("Please Enter First Name or type list for list of donor:")
    if first_name.lower() == 'list':
        get_list(dictionary)
    else:
        last_name = input("Please Enter Last Name :")
        amt = input('"Please enter donoation amount :')
        dictionary[(last_name, first_name)] = [amt]
