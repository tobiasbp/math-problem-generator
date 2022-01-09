import pytest

from math_problem_generator import generator as g


def test_problem_repeatable():
    # Same seed gives same result
    p1 = g.simple_problems("add", seed="foo", no_of_problems=200)
    p2 = g.simple_problems("add", seed="foo", no_of_problems=200)
    assert p1 == p2


def test_problem_keys():
    # problem has expected keys
    p = g.simple_problems(
        "add",
        no_of_problems=1,
    )[0]
    assert "type" in p
    assert "operator" in p
    assert "problem" in p
    assert "solution" in p
    assert "users_answer" in p


def test_problem_data():
    # Data in problem is of expected type
    p = g.simple_problems(
        "add",
        no_of_problems=1,
    )[0]
    assert isinstance(p["type"], str)
    assert isinstance(p["operator"], str)
    assert isinstance(p["problem"], list)
    assert isinstance(p["solution"], int)
    assert p["users_answer"] is None


def test_problem_seed():
    # Seed gives same result
    r = [
        {
            "type": "simple",
            "operator": "add",
            "problem": [33, 32],
            "solution": 65,
            "users_answer": None,
        }
    ]
    p = g.simple_problems(
        "add",
        seed="foobar",
        no_of_problems=1,
        min_number=1,
        max_number=100,
        numbers=2,
    )
    assert p == r


def test_problem_operator_add():
    g.simple_problems(
        "add",
    )


def test_problem_operator_sub():
    g.simple_problems(
        "sub",
    )


def test_problem_operator_mul():
    g.simple_problems(
        "mul",
    )


def test_problem_operator_div():
    g.simple_problems(
        "div",
    )


def test_problem_operator_unsupported():
    with pytest.raises(ValueError):
        g.simple_problems(
            "unsupported-operator",
        )
