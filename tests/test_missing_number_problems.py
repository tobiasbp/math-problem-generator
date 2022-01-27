import pytest
import json

from pathlib import Path

from math_problem_generator import generator as g

with open(
    Path(__file__).resolve().parent / "json/missing_number_problem_add.json"
) as json_file:
    MISSING_NUMBER_PROBLEM_ADD = json.load(json_file)

with open(
    Path(__file__).resolve().parent / "json/missing_number_problem_sub.json"
) as json_file:
    MISSING_NUMBER_PROBLEM_SUB = json.load(json_file)

with open(
    Path(__file__).resolve().parent / "json/missing_number_problem_mul.json"
) as json_file:
    MISSING_NUMBER_PROBLEM_MUL = json.load(json_file)

with open(
    Path(__file__).resolve().parent / "json/missing_number_problem_div.json"
) as json_file:
    MISSING_NUMBER_PROBLEM_DIV = json.load(json_file)


def test_problem_seed():
    # Same seed gives same result
    data1 = MISSING_NUMBER_PROBLEM_ADD.copy()
    data1["seed"] = "foobar"
    data2 = MISSING_NUMBER_PROBLEM_ADD.copy()
    data2["seed"] = "foobar"
    p1 = g.missing_number_problems(data1)
    p2 = g.missing_number_problems(data2)
    assert p1 == p2


def test_problem_seed_is_used():
    # Setting seed gives different
    # result than not setting seed
    data1 = MISSING_NUMBER_PROBLEM_ADD.copy()
    data1["seed"] = "foobarfff"
    data2 = MISSING_NUMBER_PROBLEM_ADD.copy()
    p1 = g.missing_number_problems(data1)
    p2 = g.missing_number_problems(data2)
    assert p1 != p2


def test_problem_add():
    # Operator add gives correct results
    data = MISSING_NUMBER_PROBLEM_ADD.copy()
    data["seed"] = "foobar"
    p1 = {
        "type": "missing_number",
        "operator": "add",
        "problem": [None, 79, 109],
        "solution": 30,
        "users_answer": None,
    }
    p2 = {
        "type": "missing_number",
        "operator": "add",
        "problem": [17, None, 27],
        "solution": 10,
        "users_answer": None,
    }
    assert p1 == g.missing_number_problems(data)[1]
    assert p2 == g.missing_number_problems(data)[2]


def test_problem_sub():
    # Operator sub gives correct results
    data = MISSING_NUMBER_PROBLEM_SUB.copy()
    data["seed"] = "seed-for-sub"
    p1 = {
        "type": "missing_number",
        "operator": "sub",
        "problem": [None, 36, 42],
        "solution": 78,
        "users_answer": None,
    }
    p2 = {
        "type": "missing_number",
        "operator": "sub",
        "problem": [None, 91, -66],
        "solution": 25,
        "users_answer": None,
    }
    assert p1 == g.missing_number_problems(data)[1]
    assert p2 == g.missing_number_problems(data)[2]


def test_problem_mul():
    # Operator mul gives correct results
    data = MISSING_NUMBER_PROBLEM_MUL.copy()
    data["seed"] = "seed-for-mul"
    p1 = {
        "type": "missing_number",
        "operator": "mul",
        "problem": [5, None, 60],
        "solution": 12,
        "users_answer": None,
    }
    p2 = {
        "type": "missing_number",
        "operator": "mul",
        "problem": [9, None, 135],
        "solution": 15,
        "users_answer": None,
    }
    assert p1 == g.missing_number_problems(data)[1]
    assert p2 == g.missing_number_problems(data)[2]


def test_problem_div():
    # Operator div gives correct results
    data = MISSING_NUMBER_PROBLEM_DIV.copy()
    data["seed"] = "seed-for-div"
    p1 = {
        "type": "missing_number",
        "operator": "div",
        "problem": [None, 31, 1],
        "solution": 31,
        "users_answer": None,
    }
    p2 = {
        "type": "missing_number",
        "operator": "div",
        "problem": [37, None, 1],
        "solution": 37,
        "users_answer": None,
    }
    assert p1 == g.missing_number_problems(data)[1]
    assert p2 == g.missing_number_problems(data)[2]


# FIXME: Number of problems


def test_problem_invalid_type():
    data = MISSING_NUMBER_PROBLEM_ADD.copy()
    data["type"] = "some-invalid-type"
    with pytest.raises(ValueError):
        g.missing_number_problems(data)


"""
def test_solution_mul_4x3():
    # A 4 X 3 matrix
    row = [0, 1, 2, 3]
    col = [0, 1, 2]
    solution = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
    r = g.matrix_solution("mul", row, col)
    assert solution == r


def test_solution_mul_5x5():
    # A 4 X 3 matrix
    row = [1, 3, 0, 2, 4]
    col = [2, 3, 0, 1, 4]
    solution = [
        [2, 6, 0, 4, 8],
        [3, 9, 0, 6, 12],
        [0, 0, 0, 0, 0],
        [1, 3, 0, 2, 4],
        [4, 12, 0, 8, 16],
    ]
    r = g.matrix_solution("mul", row, col)
    assert solution == r


def test_solution_add_4x3():
    # A 4 X 3 matrix
    row = [0, 1, 2, 3]
    col = [0, 1, 2]
    solution = [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]]
    r = g.matrix_solution("add", row, col)
    assert solution == r


def test_solution_sub_4x3():
    # A 4 X 3 matrix
    row = [0, 1, 2, 3]
    col = [0, 1, 2]
    solution = [[0, 1, 2, 3], [-1, 0, 1, 2], [-2, -1, 0, 1]]
    r = g.matrix_solution("sub", row, col)
    assert solution == r


def test_solution_div_4x3():
    # A 4 X 3 matrix
    row = [8, 16, 32, 24]
    col = [2, 4, 8]
    solution = [[4, 8, 16, 12], [2, 4, 8, 6], [1, 2, 4, 3]]
    r = g.matrix_solution("div", row, col)
    assert solution == r


def test_problem_seed():
    # Same seed gives same result
    data = MATRIX_MATH_PROBLEM_ADD
    data["seed"] = "foobar"
    p1 = g.matrix_problems(data)
    p2 = g.matrix_problems(data)
    assert p1 == p2


def test_matrix_support_in_problem_function():
    # Same seed gives same result
    data = MATRIX_MATH_PROBLEM_ADD
    data["seed"] = "foobar"
    p1 = g.matrix_problems(data)
    p2 = g.problems(data)
    assert p1 == p2


def test_problem_keys():
    # problem has expected keys
    p = g.matrix_problems(MATRIX_MATH_PROBLEM_ADD)[0]
    assert "type" in p
    assert "operator" in p
    assert "col" in p["problem"]
    assert "row" in p["problem"]
    assert "users_answer" in p


def test_problem_data():
    # Data in problem is of expected type
    p = g.matrix_problems(MATRIX_MATH_PROBLEM_ADD)[0]
    assert isinstance(p["type"], str)
    assert isinstance(p["operator"], str)
    assert isinstance(p["problem"], dict)
    assert isinstance(p["problem"]["col"], list)
    assert isinstance(p["problem"]["row"], list)
    assert isinstance(p["solution"], list)
    assert p["users_answer"] is None


def test_problem_operator_div():
    request = MATRIX_MATH_PROBLEM_DIV
    request["seed"] = "some-seed"
    # 'row': [1, 3, 2], 'col': [3, 2, 1]},
    s = [[0.33, 1.0, 0.67], [0.5, 1.5, 1.0], [1.0, 3.0, 2.0]]
    p = g.matrix_problems(MATRIX_MATH_PROBLEM_DIV)[0]
    assert p["solution"] == s


def test_problem_operator_add():
    g.matrix_problems(MATRIX_MATH_PROBLEM_ADD)


def test_problem_operator_sub():
    g.matrix_problems(MATRIX_MATH_PROBLEM_SUB)


def test_problem_operator_mul():
    g.matrix_problems(
        MATRIX_MATH_PROBLEM_MUL,
    )


def test_problem_operator_unsupported():
    d = MATRIX_MATH_PROBLEM_ADD
    d["operator"] = "not-an-operator"
    with pytest.raises(ValueError):
        g.matrix_problems(d)

"""
