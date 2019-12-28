"""
A simple program that generate the Fibonacci sequence of N numbers.
"""

if __name__ == '__main__':
    fibonacci_numbers = [0, 1]
    while True:
        try:
            N = int(input("Enter how many numbers the Fibonacci sequence will have: "))
            if N <= 1:
                test = N / 0
            break
        except ValueError:
            print("Wrong input. Try again.")
        except ZeroDivisionError:
            print("Value must be greater than 1.")

    for i in range(N - 2):
        fibonacci_numbers.append(fibonacci_numbers[i] + fibonacci_numbers[i + 1])
    print(fibonacci_numbers)
