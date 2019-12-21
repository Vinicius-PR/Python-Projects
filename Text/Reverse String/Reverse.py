"""
This program just reverse a string and print it.
"""

if __name__ == '__main__':
    string_input = input("Enter a phrase, word or anything: ")
    reversed_string = string_input[::-1]
    print("The reversed input is: {}".format(reversed_string))
