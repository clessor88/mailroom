# -*- coding: utf-8 -*-
from __future__ import unicode_literals

TEST_DICT = {
    ('lessor', 'crystal'): [10, 40, 25],
    ('harrison', 'mike'): [30, 40, 15],
    ('smith', 'john'): [10, 25],
    ('python', 'monty'): [42]
}

donor_list = {
    ('lessor', 'crystal'): [10, 40, 25],
    ('harrison', 'mike'): [30, 40, 15],
    ('smith', 'john'): [10, 25],
    ('python', 'monty'): [42],
}

TEST_LIST = [
    (('harrison', 'mike'), [30, 40, 15], 28.333333333333332),
    (('lessor', 'crystal'), [10, 40, 25], 25.0),
    (('python', 'monty'), [42], 42.0),
    (('smith', 'john'), [10, 25], 17.5)
]


def test_validate_first_0():
    """Test validation for first name."""
    from mailroom import validate_first_name
    assert validate_first_name('mike') == 'mike'


def test_validate_last_name():
    """Test a valid input for last name."""
    from mailroom import validate_last_name
    assert validate_last_name('harrison') == 'harrison'


def test_validate_amount():
    """Test a valid input for amount."""
    from mailroom import validate_amt
    assert validate_amt('100') == 100


def test_sort_donors():
    """Test sort donors."""
    from mailroom import sort_donors
    result = TEST_LIST
    assert sort_donors(donor_list) == result
