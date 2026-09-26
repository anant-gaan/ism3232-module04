import math


def test_tax_at_seven_percent():
    subtotal = 200
    tax = subtotal * 0.07
    assert math.isclose(tax, 14.0)


def test_over_limit():
    total = 1500
    limit = 1000
    assert (total > limit) is True


def test_under_limit():
    total = 500
    limit = 1000
    assert (total > limit) is False


def test_type_of_string():
    name = "ISM 3232"
    assert type(name) == str


def test_type_of_coversion():
    s = "42"
    assert int(s) == 42
