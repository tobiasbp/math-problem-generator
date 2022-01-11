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
