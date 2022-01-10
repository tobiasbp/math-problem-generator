"""
Math problem generator. Needs python 3.8 or higher.
"""
import operator
import random

from typing import List, TypedDict, Union


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


def simple_solution(
    operator_name: str, numbers: List[Union[int, float]]
) -> Union[None, int, float]:
    """
    Calculate the solution for a list of numbers and an operator
    """

    if len(numbers) < 2:
        raise ValueError("Numbers list too short")

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

    # Calculate result
    r = numbers[0]
    for n in numbers[1:]:
        try:
            r = o(r, n)
        except ZeroDivisionError:
            return None

    return r


# FIXME: numbers: int > [[min,max],[min,max]]
def simple_problems(request: SimpleMathProblemRequest) -> List[SimpleMathProblem]:
    """
    Generate simple math problems like 1+2=3
    """

    # Can't generate problems with less than 2 numbers
    if len(request["problem"]) < 2:
        raise ValueError("Argument 'numbers' less that 2")

    # Supply sees for predictable problems
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
