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
    result = ["('harrison', 'mike'): [30, 40, 15]: 28.333333333333332", "('lessor', 'crystal'): [10, 40, 25]: 25.0", "('python', 'monty'): [42]: 42.0", "('smith', 'john'): [10, 25]: 17.5"]
    assert sort_donors(TEST_DICT) == result
