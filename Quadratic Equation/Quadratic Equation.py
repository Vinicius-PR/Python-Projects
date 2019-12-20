"""
This is a program that calculate the roots, vertices and plot the graphic of a quadratic equation.
Also tell if it is ascending or descending.
"""

import matplotlib.pyplot as plt
import numpy as np


def welcome():
    print("Welcome to quadratic equation solver")
    print("This resolve the equation of the type ax² + bx + c = 0")
    print("You have to give us the coefficients a, b and c. The rest I'll handle.")
    print("ATTENTION: The a must be different of 0.")


def ask_for_value():
    """Return a tuple with the coefficients a, b and c."""
    while True:
        try:
            value_a = int(input("\nType the value of a: "))
            test_value_a = 10/value_a
            break
        except ZeroDivisionError:
            print("The value of 'a' can not be zero. Try again: ")
        except:
            print("Invalid value, try again: ")
    while True:
        try:
            value_b = int(input("\nType the value of b: "))
            break
        except:
            print("Invalid value, try again")
    while True:
        try:
            value_c = int(input("\nType the value of c: "))
            break
        except:
            print("Invalid value, try again")
    return value_a, value_b, value_c


def calculate_delta(a, b, c):
    return (b ** 2) - 4 * a * c


def calculate_roots(a, b, delta):
    """Calculate the roots and round them up to 3 decimal points."""
    return round(((-b + delta ** (1 / 2)) / (2 * a)), 3), round(((-b - delta ** (1 / 2)) / (2 * a)), 3)


def calculate_vertices(a, b, delta):
    """Return a tuple with the X and Y of the vertices."""
    return round(-b / (2 * a), 2), round(-delta / (4 * a), 2)


def check_route(a):
    if a > 0:
        return "This quadratic equation is Ascending"
    else:
        return "This quadratic equation is Descending"


def get_formula(a, b, c):
    """Return the formula as a string."""
    if b == 0 and c == 0:
        formula = "{}x² = 0".format(a)
    elif c == 0:
        formula = "{}x² {}{}x = 0".format(a, "+" if b > 0 else "", b)
    elif b == 0:
        formula = "{}x² {}{} = 0".format(a, "+" if c > 0 else "", c)
    else:
        formula = "{}x² {}{}x {}{} = 0".format(a, "+" if b > 0 else "", b, "+" if c > 0 else "", c)
    return formula


if __name__ == "__main__":
    welcome()
    a, b, c = ask_for_value()
    delta = calculate_delta(a, b, c)
    vertices = calculate_vertices(a, b, delta)
    formula = get_formula(a, b, c)

    # Calculate the roots or pass if there is no way to calculate(when delta is less than 0)
    if delta > 0 or delta == 0:
        roots = calculate_roots(a, b, delta)
    else:
        pass

    # displaying the equation and its roots, if have it:
    if delta > 0:
        print("The two roots of the equation {} are: {}".format(formula, roots))
    elif delta == 0:
        print("The only root of the equation {} is: {}".format(formula, roots[0]))
    else:
        print("The equation {} has no roots. Delta < 0".format(formula))

    # Ascending or Descending?
    check_route(a)

    print("The coordinates of the vertices are: {}".format(vertices))

    """Code to deal with the graph:"""
    if delta > 0 or delta == 0:
        low_range = roots[0] - 5
        high_range = roots[1] + 5
    else:
        low_range = -10
        high_range = 10

    # Using numpy to deal with a list of float numbers.
    X_values = [i for i in np.arange(low_range, high_range + 0.2, 0.2)]
    Y_values = []
    for i in X_values:
        hold_value = (a * i ** 2) + (b * i) + c
        Y_values.append(hold_value)

    plt.plot(X_values, Y_values)
    plt.plot(vertices[0], vertices[1], 'go', label='V' + str(vertices))
    plt.legend()
    plt.grid(True)
    plt.title(formula)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()
