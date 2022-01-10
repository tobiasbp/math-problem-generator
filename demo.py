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
print(json.dumps(list_of_problems[:2], sort_keys=True, indent=4))
