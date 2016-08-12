# -*- coding: utf-8 -*-
def sort_donors(donor_dict):
    """Turns donors into list and sorts in decending order."""
    sorted_donors = sorted(donor_dict, key=lambda x: sum(donor_dict[x]), reverse=True)
    for k in sorted_donors:
        print("{}: {}: {}".format(k, donor_dict[k], float(sum(donor_dict[k]))/len(donor_dict[k])))
