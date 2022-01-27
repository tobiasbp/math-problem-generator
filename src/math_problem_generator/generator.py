"""
Math problem generator. Needs python 3.8 or higher.
"""
import operator
import random

from typing import List, Sequence, TypedDict, Union


class SimpleMathProblemRange(TypedDict):
    min: int
    max: int


class SimpleMathProblemRequest(TypedDict):
    type: str
    operator: str
    problem: List[SimpleMathProblemRange]
    no_of_problems: int
    seed: Union[str, None]


class SimpleMathProblem(TypedDict):
    type: str
    operator: str
    problem: List[Union[int, float]]
    solution: Union[None, int, float]
    users_answer: Union[None, int, float]


class MatrixMathProblemMatrix(TypedDict):
    row: Sequence[Union[int, float]]
    col: Sequence[Union[int, float]]


class MatrixMathProblemRequest(TypedDict):
    type: str
    operator: str
    collumns: int
    rows: int
    no_of_problems: int
    seed: Union[str, None]


class MatrixMathProblem(TypedDict):
    type: str
    operator: str
    problem: MatrixMathProblemMatrix
    solution: List[List[Union[int, float]]]
    users_answer: Union[None, List[List[Union[int, float]]]]


class MissingNumberRange(TypedDict):
    min: int
    max: int


class MissingNumberRequest(TypedDict):
    type: str
    operator: str
    problem: List[MissingNumberRange]
    no_of_problems: int
    seed: Union[str, None]


class MissingNumberProblem(TypedDict):
    type: str
    operator: str
    problem: List[Union[None, int, float]]
    solution: Union[None, int, float]
    users_answer: Union[None, int, float]


def string_to_operator(operator_name: str):
    """
    Return an operator function from a string argument
    """

    # Define the operator function to use
    if operator_name == "add":
        o = operator.add
    elif operator_name == "sub":
        o = operator.sub
    elif operator_name == "mul":
        o = operator.mul
    elif operator_name == "div":
        o = operator.truediv
    else:
        raise ValueError(f"Invalid operator: '{operator_name}'")
    return o


def simple_solution(
    operator_name: str, numbers: List[Union[int, float]]
) -> Union[None, int, float]:
    """
    Calculate the solution for a list of numbers and an operator
    """

    if len(numbers) < 2:
        raise ValueError("Numbers list too short")

    # get the operator function
    o = string_to_operator(operator_name)

    # Calculate result
    r = numbers[0]
    for n in numbers[1:]:
        try:
            r = o(r, n)
        except ZeroDivisionError:
            return None

    return r


def matrix_solution(
    operator_name: str,
    row: Sequence[Union[int, float]],
    col: Sequence[Union[int, float]],
    no_of_decimals: int = 2,
) -> List[List[Union[int, float]]]:
    """
    Generate the solution to a matrix problem
    """
    # get the operator function
    o = string_to_operator(operator_name)

    solution = []
    for c in col:
        solution.append([round(o(r, c), no_of_decimals) for r in row])
    return solution


def simple_problems(request: SimpleMathProblemRequest) -> List[SimpleMathProblem]:
    """
    Generate simple math problems like 1+2=x
    """

    # Can't generate problems with less than 2 numbers
    if len(request["problem"]) < 2:
        raise ValueError("Argument 'numbers' less that 2")

    # Set seed for predictable problems
    if s := request["seed"]:
        random.seed(s)

    problem_list = []

    # Generate the problems
    for i in range(request["no_of_problems"]):
        # Empty problem dict
        p: SimpleMathProblem = {
            "type": "simple",
            "operator": request["operator"],
            "problem": [],
            "solution": None,
            "users_answer": None,
        }

        # Generate numbers for problem
        for nd in request["problem"]:
            p["problem"].append(random.randint(nd["min"], nd["max"]))

        # Add the result to the problem
        p["solution"] = simple_solution(request["operator"], p["problem"])

        # Add problem to list of problems
        problem_list.append(p)

    return problem_list


def matrix_problems(request: MatrixMathProblemRequest) -> List[MatrixMathProblem]:
    """
    Generate a list of matrix math problems
    """

    if t := request["type"] != "matrix":
        raise ValueError(f"Argument 'type' must be 'matrix'. Recieved '{t}'")

    if c := int(request["collumns"]) < 1:
        raise ValueError(
            f"Argument 'collumns' must be a positive integer. Recieved '{c}'"
        )

    if r := int(request["rows"]) < 1:
        raise ValueError(f"Argument 'rows' must be a positive integer. Recieved '{r}'")

    # Set seed for predictable problems
    if s := request["seed"]:
        random.seed(s)

    problem_list = []

    # Lowest number in ranges for col & row
    # Should probably be part of problem request
    base_no = 1

    # Generate matrix problems
    for i in range(request["no_of_problems"]):

        col = random.sample(range(base_no, request["rows"] + base_no), request["rows"])
        row = random.sample(
            range(base_no, request["collumns"] + base_no), request["collumns"]
        )

        p: MatrixMathProblem = {
            "type": "matrix",
            "operator": request["operator"],
            "problem": {
                "row": row,
                "col": col,
            },
            "solution": matrix_solution(request["operator"], row, col),
            "users_answer": None,
        }

        # Add problem to list of problems
        problem_list.append(p)

    return problem_list


def missing_number_problems(
    request: MissingNumberRequest,
) -> List[MissingNumberProblem]:
    """
    Generate missing number problems like 1+x=3
    """
    if request["type"] != "missing_number":
        raise ValueError(f"Invalid problem type in request: '{request['type']}'")

    # Can't generate problems with less than 2 numbers
    if len(request["problem"]) < 2:
        raise ValueError("Argument 'numbers' less that 2")

    # Set seed for predictable problems
    if s := request["seed"]:
        random.seed(s)

    problem_list = []

    # Generate the problems
    for i in range(request["no_of_problems"]):
        # Empty problem dict
        p: MissingNumberProblem = {
            "type": request["type"],
            "operator": request["operator"],
            "problem": [],
            "solution": None,
            "users_answer": None,
        }

        # Generate numbers for problem (Like 1 + 9)
        for nd in request["problem"]:
            if request["operator"] != "div" or p["problem"] == []:
                p["problem"].append(random.randint(nd["min"], nd["max"]))
            else:
                if (pl := len(request["problem"])) > 2:
                    raise ValueError(
                        f"Invalid problem length '{pl}' for problem type "
                        f"'{request['type']}' with operator '{request['operator']}'"
                    )
                if not (
                    # Divisors of previous integer in problem in range of min/max
                    divisors := [
                        n
                        for n in range(nd["min"], nd["max"] + 1)
                        if p["problem"][-1] % n == 0  # type: ignore
                    ]
                ):
                    raise ValueError(
                        f"No divisors for {p['problem'][-1]} "
                        f"in range {nd['min']}-{nd['max']}"
                    )
                else:
                    # Add a random visisor to the problem
                    p["problem"].append(random.choice(divisors))

        # Add the result to the problem. We now have [1,9,10] to represent 1 + 9 = 10
        p["problem"].append(
            simple_solution(request["operator"], p["problem"])  # type: ignore
        )

        # Randomly get an index for the number to remove from the problem.
        # Can not be the last entry (The result)
        i = random.randint(0, len(request["problem"]) - 1)
        # The number we are about to remove from the problem list, is the solution
        p["solution"] = p["problem"][i]
        # Swap the number the user has to calculate with None
        p["problem"][i] = None

        # Add problem to list of problems
        problem_list.append(p)

    return problem_list


# Can't have typing for request, since both types
# are not supported for the "problem" functions.
def problems(
    request,
) -> Union[
    List[SimpleMathProblem], List[MatrixMathProblem], List[MissingNumberProblem]
]:
    """
    Generate problems from any supported type of math problem request
    """
    if request["type"] == "simple":
        return simple_problems(request)
    if request["type"] == "matrix":
        return matrix_problems(request)
    if request["type"] == "missing_number":
        return missing_number_problems(request)
    else:
        raise ValueError(f"Unsupported type '{request['type']}' in request")
