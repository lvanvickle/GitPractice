from utils.math_operations import add, subtract
from utils.string_operations import reverse_string
import numpy as np
from sympy import Symbol, solve

if __name__ == "__main__":
    # Using custom math_operations module
    print(f"\n\033[4m{'Math Operations:'}\033[0m")
    print(f"Add: 6 + 3 = {add(6, 3)}")
    print(f"Subtract: 6 - 3 = {subtract(6, 3)}")
    #print(f"Multiply: 6 * 3 = {multiply(6, 3)}")
    #print(f"Divide: 6 * 3 = {divide(6, 3)}")

    # Using custom string_operations module
    print(f"\n\033[4m{'String Operations:'}\033[0m")
    print(f"Reverse 'hello': {reverse_string('hello')}")

    # Using NumPy
    print(f"\n\033[4m{'NumPy Operations:'}\033[0m")
    array = np.array([1, 2, 3, 4, 5])
    print(f"Original array: {array}")
    print(f"Array multipled by 2: {array * 2}")

    # Using SymPy
    print(f"\n\033[4m{'Sympy Operations:'}\033[0m")
    x = Symbol('x')
    equation = x**2 - 4
    solution = solve(equation, x)
    print(f"Solutions to x\u00B2 - 4 = 0: {solution}")


    