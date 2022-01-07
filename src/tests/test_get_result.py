import pytest

from math_problem_generator import generator as g


def test_simple_solution_add():
    assert g.simple_solution("add", [10, 1, 1000]) == 1011


def test_simple_solution_sub():
    assert g.simple_solution("sub", [10, 1, 1000]) == -991


def test_simple_solution_mul():
    assert g.simple_solution("mul", [2, 4]) == 8
    assert g.simple_solution("mul", [-2, 10]) == -20
    assert g.simple_solution("mul", [-2, -10]) == 20


def test_simple_solution_not_enough_numbers():
    with pytest.raises(ValueError):
        g.simple_solution("sub", [10])


def test_simple_solution_invalid_operator():
    with pytest.raises(ValueError):
        g.simple_solution("invalid-operator", [10, 20])
