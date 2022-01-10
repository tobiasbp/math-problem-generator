# Python package math_problem_generator
A python package for generating simple math problems. The package is only for
generating the problems. There is no support for presentation or user interaction.

# Problems
## Simple

A simple math problem like _1 + 2 = 3_. The supported operators are:

| Operator | String representation |
|----------|-----------------------|
| Addition | _add_ |
| Subtraction | _sub_ |
| Multiplication | _mul_ |
| Divison | _div_ |

A JSON request for 25 problems where three integers between 1 and 9 are to be added:
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
# How to install
The package is distributed via [pypi.org](https://pypi.org/), and can be installed with _pip_ like this:
```
pip3 install math-problem-generator
```

# Examples
How to use the package. The code below is in _demo.py_ in the root of the repository.

```python
#!/usr/bin/env python

import json
from pathlib import Path

from math_problem_generator import generator


# Load problem request from JSON file
problem_request = json.loads(
    Path("tests/json/simple_math_problem_add.json").read_text()
)

# Generate simple problems from request
list_of_problems = generator.simple_problems(problem_request)

# Print the math problems
print(json.dumps(list_of_problems[0], sort_keys=True, indent=4))
```

The code above should print a two JSON formatted simple math problems like this:
```json
[
    {
        "operator": "add",
        "problem": [
            9,
            1,
            9
        ],
        "solution": 19,
        "type": "simple",
        "users_answer": null
    },
    {
        "operator": "add",
        "problem": [
            6,
            9,
            2
        ],
        "solution": 17,
        "type": "simple",
        "users_answer": null
    }
]

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
