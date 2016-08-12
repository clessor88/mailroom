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


def donor_name(dictionary):
    """Get Full Name and Donation Amount."""
    first_name = input("Please Enter First Name :")
    last_name = input("Please Enter Last Name :")
    full_name = (last_name, first_name)
    amt = input('"Please enter donoation amount :')
    dictionary.setdeafult(full_name, default=[amt])
    