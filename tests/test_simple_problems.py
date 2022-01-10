import pytest
import json

from pathlib import Path

from math_problem_generator import generator as g

with open(
    Path(__file__).resolve().parent / "json/simple_math_problem_add.json"
) as json_file:
    SIMPLE_MATH_PROBLEM_ADD = json.load(json_file)

with open(
    Path(__file__).resolve().parent / "json/simple_math_problem_sub.json"
) as json_file:
    SIMPLE_MATH_PROBLEM_SUB = json.load(json_file)

with open(
    Path(__file__).resolve().parent / "json/simple_math_problem_mul.json"
) as json_file:
    SIMPLE_MATH_PROBLEM_MUL = json.load(json_file)

with open(
    Path(__file__).resolve().parent / "json/simple_math_problem_div.json"
) as json_file:
    SIMPLE_MATH_PROBLEM_DIV = json.load(json_file)


def test_problem_repeatable():
    # Same seed gives same result
    data = SIMPLE_MATH_PROBLEM_ADD
    data["seed"] = "foobar"
    p1 = g.simple_problems(data)
    p2 = g.simple_problems(data)
    assert p1 == p2


def test_problem_keys():
    # problem has expected keys
    p = g.simple_problems(SIMPLE_MATH_PROBLEM_ADD)[0]
    assert "type" in p
    assert "operator" in p
    assert "problem" in p
    assert "solution" in p
    assert "users_answer" in p


def test_problem_data():
    # Data in problem is of expected type
    p = g.simple_problems(SIMPLE_MATH_PROBLEM_ADD)[0]
    assert isinstance(p["type"], str)
    assert isinstance(p["operator"], str)
    assert isinstance(p["problem"], list)
    assert isinstance(p["solution"], int)
    assert p["users_answer"] is None


def test_problem_seed():
    # If a seed is supplied, problms are always the same
    d = SIMPLE_MATH_PROBLEM_ADD
    d["seed"] = "some-seed"
    p = g.simple_problems(d)
    assert p[0]["solution"] == 18
    assert p[1]["solution"] == 11
    assert p[2]["solution"] == 11


def test_problem_operator_add():
    g.simple_problems(SIMPLE_MATH_PROBLEM_ADD)


def test_problem_operator_sub():
    g.simple_problems(SIMPLE_MATH_PROBLEM_SUB)


def test_problem_operator_mul():
    g.simple_problems(
        SIMPLE_MATH_PROBLEM_MUL,
    )


def test_problem_operator_div():
    g.simple_problems(SIMPLE_MATH_PROBLEM_DIV)


def test_problem_operator_unsupported():
    d = SIMPLE_MATH_PROBLEM_ADD
    d["operator"] = "not-an-operator"
    with pytest.raises(ValueError):
        g.simple_problems(d)
