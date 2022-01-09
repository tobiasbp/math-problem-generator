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

The representation of the problem _1 + 2 + 7 = 10_:
```
{
    'type': 'simple',
    'operator': 'add',
    'problem': [1, 2, 7],
    'solution': 10,
    'users_answer': None
}
```
# How to install
The package is distributed via [pypi.org](https://pypi.org/), and can be installed with _pip_ like this:
```
pip3 install math-problem-generator
```

# Examples
How to use the package.

```python
# Import the package
from math_problem_generator import generator

# Generate 2 simple addition problems with
# 4 numbers between 1 and 10 to be added
p = generator.simple_problems(
        "add",no_of_problems=2,min_number=1,max_number=10,numbers=4
    )

# Print the math problems
print(p)
```

The code above should print something like this:
```
[
    {'type': 'simple', 'operator': 'add', 'problem': [5, 2, 3, 6], 'solution': 16, 'users_answer': None},
    {'type': 'simple', 'operator': 'add', 'problem': [6, 10, 10, 5], 'solution': 31, 'users_answer': None}]
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
