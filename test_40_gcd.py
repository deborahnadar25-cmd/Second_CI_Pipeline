import importlib

module = importlib.import_module("40_gcd")


def test_gcd():
    assert module.find_gcd(12, 18) == 6


def test_gcd_equal_numbers():
    assert module.find_gcd(10, 10) == 10


def test_gcd_with_zero():
    assert module.find_gcd(5, 0) == 5


def test_gcd_coprime_numbers():
    assert module.find_gcd(7, 13) == 1