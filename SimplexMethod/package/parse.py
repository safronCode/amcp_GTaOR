from collections import defaultdict
import re
import numpy as np

def parse_mps(file_path):
    rows = {}
    columns = defaultdict(list)
    rhs = {}
    bounds = {}
    integer_variables = set()
    current_section = None
    in_int_section = False
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith("NAME"):
                continue
            elif line.startswith("ROWS"):
                current_section = "ROWS"
                continue
            elif line.startswith("COLUMNS"):
                current_section = "COLUMNS"
                continue
            elif line.startswith("RHS"):
                current_section = "RHS"
                continue
            elif line.startswith("BOUNDS"):
                current_section = "BOUNDS"
                continue
            elif line.startswith("ENDATA"):
                break

            if current_section == "ROWS":
                row_type = line[0]
                row_name = line[1:].strip()
                rows[row_name] = row_type

            elif current_section == "COLUMNS":
                parts = re.split(r"\s+", line)
                if parts[1] == "'MARKER'":
                    if parts[2] == "'INTORG'":
                        in_int_section = True
                    elif parts[2] == "'INTEND'":
                        in_int_section = False
                    continue

                col_name = parts[0]
                row_name = parts[1]
                value = parts[2]

                if in_int_section:
                    integer_variables.add(col_name)

                columns[col_name].append((row_name, value))

            elif current_section == "RHS":
                parts = re.split(r"\s+", line)
                row_name = parts[1]
                value = parts[2]
                rhs[row_name] = value

            elif current_section == "BOUNDS":
                parts = re.split(r"\s+", line)
                bound_type = parts[0]
                bound_name = parts[2]
                value = parts[3] if len(parts) > 3 else None
                bounds[bound_name] = (bound_type, value)

    return rows, columns, rhs, bounds, integer_variables

def get_A(arr, r, c):
    A = np.zeros((r,c))
    for key in arr.keys():
        for elem in arr[key]:
            if elem[0] != 'OBJROW':
                A[int(elem[0][1:])-1, int(key[1:])] = elem[1]
    return (A)

def get_b(arr):
    b = np.array([
        float(constaint)
        for row, constaint in arr.items()
    ])
    return b

def get_c(arr):
    c = np.zeros((int(list(arr.keys())[-1][1:]))+1)
    for key in arr.keys():
        for elem in arr[key]:
            if elem[0] == 'OBJROW':
                c[(int(key[1:]))] = elem[1]
    return c

def get_sign(arr):
    constraint_map = {'L': 1, 'E': 0,'N': 0,'G': -1}
    sign = np.array([
        constraint_map[constraint]
        for row, constraint in arr.items()
        if row != 'OBJROW'
    ])
    return sign






