# Python package math_problem_generator
A python package for generating simple math problems. The package is only for
generating the problems. There is no support for presentation or user interaction.
The user of the library submits a JSON formatted _problem request_,
and recieves a list of math problems.


# How to install
The package is distributed via [pypi.org](https://pypi.org/), and can be
installed with the package manager _pip_ like this:
```
pip3 install math-problem-generator
```

# Types of problems
The package supports three types of math problems: _simple_, _matrix_ and _missing_number_.
All problem types must specify an operator. The supported operators are:

| Operator | String representation |
|----------|-----------------------|
| Addition | _add_ |
| Subtraction | _sub_ |
| Multiplication | _mul_ |
| Divison | _div_ |

## Simple
A simple math problem like _1 + 2 = 3_.

A JSON request for 25 problems where three integers between 1 and 9 are to be added.
A seed can be supplied, if the same set of problems are required for repeated requests:
```
{
    "type": "simple",
    "operator": "add",
    "problem": [
        {
            "min": 1,
            "max": 9
        },
        {
            "min": 1,
            "max": 9
        },
        {
            "min": 1,
            "max": 9
        }
    ],
    "no_of_problems": 25,
    "seed": null
}
```

The JSON representation of the problem _1 + 2 + 7 = 10_:
```
{
    "type": "simple",
    "operator": "add",
    "problem": [1, 2, 7],
    "solution": 10,
    "users_answer": null
}
```

## Matrix
Type matrix problem type consists of a matrix where the cells are the result of an
operator and the matching row/col values. The lowest value in a row/col is always 1.
Here is an example of a matrix where the operator is _add_. The solution to the cell
marked _x_ is `3 + 2 = 5` (collumn + row).

| _add_ | 1 | 2 | 3 |
|-------| - | - | - |
| 1     |   |   |   |
| 2     |   |   |   |
| 3     |   | x |   |

This table shows the problem matrix with the correct solution.

| _add_ | 1 | 2 | 3 |
|-------| - | - | - |
| 1     | 2 | 3 | 4 |
| 2     | 3 | 4 | 5 |
| 3     | 4 | 5 | 6 |

A request for 25 matrix problems of size 5 x 5 with the _mul_ operator:

```
{
    "type": "matrix",
    "operator": "mul",
    "collumns": 5,
    "rows": 5,
    "no_of_problems": 25,
    "seed": null
}
```

A matrix problem of size 2 x 2 with the _add_ operator:
```
{
    "operator": "add",
    "problem": {
        "col": [10, 20],
        "row": [1,  2]
    },
    "solution": [
        [
            [11, 21],
            [12, 22]
        ]
    ],
    "type": "matrix",
    "users_answer": null
}
```
## Missing number
A simple math problem where the result is known, but one number is missing.
An example of this type of problem is `1 + x = 5`. The solution is 4. For the _div_
operator, the problem length is limitied to 2. That is, a problem like `10 / 5 / x = 2`
is not allowed.

A request for 25 _missing_number_ problems with two two digit numbers to be added:
```
{
    "type": "missing_number",
    "operator": "add",
    "problem": [
        {
            "min": 10,
            "max": 99
        },
        {
            "min": 10,
            "max": 99
        }
    ],
    "no_of_problems": 25,
    "seed": null
}
```

The JSON representation of the problem _15 + x = 20_:
```
{
    "type": "missing_number",
    "operator": "add",
    "problem": [15, null, 20],
    "solution": 5,
    "users_answer": null
}
```

# Examples
How to use the package. The code below is in _demo.py_ in the root of the repository.

```python
#!/usr/bin/env python

import json
from pathlib import Path

from math_problem_generator import generator


# Load simple problem request from JSON file
simple_problem_request = json.loads(
    Path("tests/json/simple_math_problem_add.json").read_text()
)

# Load matrix problem request from JSON file
matrix_problem_request = json.loads(
    Path("tests/json/matrix_math_problem_add.json").read_text()
)

# Generate simple problems from request JSON
list_of_simple_problems = generator.problems(simple_problem_request)

# Generate matrix problems from request JSON
list_of_matrix_problems = generator.problems(matrix_problem_request)

# Print a simple problem as JSON
print(json.dumps(list_of_simple_problems[:1], sort_keys=True, indent=4))

# Print a matrix problem as JSON
print(json.dumps(list_of_matrix_problems[:1], sort_keys=True, indent=4))

```

# Development

Setup virtual environment
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip3 install -r requirements-dev.txt`
4. `pip install -e src/`
5. `pre-commit install`

Leave virtual environment (when done)
1. `deactivate`
