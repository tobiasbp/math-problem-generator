import pytest

from math_problem_generator import generator as g


def test_get_result_add():
    assert g.get_result("add", [10, 1, 1000]) == 1011


def test_get_result_sub():
    assert g.get_result("sub", [10, 1, 1000]) == -991


def test_get_result_mul():
    assert g.get_result("mul", [2, 4]) == 8
    assert g.get_result("mul", [-2, 10]) == -20
    assert g.get_result("mul", [-2, -10]) == 20


def test_get_result_not_enough_numbers():
    with pytest.raises(ValueError):
        g.get_result("sub", [10])


def test_get_result_invalid_operator():
    with pytest.raises(ValueError):
        g.get_result("invalid-operator", [10, 20])
