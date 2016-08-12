# -*- coding: utf-8 -*-
TEST_DICT = {
    ('lessor', 'crystal'): [10, 40, 25],
    ('harrison', 'mike'): [30, 40, 15],
    ('smith', 'john'): [10, 25],
    ('python', 'monty'): [42]
}


def test_sort_donors():
    """Sorts donor outputs from most to least donated"""
    from mailroom import sort_donors
    result = [('harrison', 'mike'), ('lessor', 'crystal'), ('python', 'monty'), ('smith', 'john')]
    assert sort_donors(TEST_DICT) == result
