#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_of_arguments = len(sys.argv) - 1

    if number_of_arguments == 0:
        print("{} arguments .".format(number_of_arguments))
    elif number_of_arguments == 1:
        print("{} argument:".format(number_of_arguments))
    else:
        print("{} arguments:".format(number_of_arguments))

    if number_of_arguments >= 1:
        number_of_arguments = 0
        for arg in sys.argv:
            if number_of_arguments != 0:
                print("{}: {}".format(number_of_arguments, arg))
            number_of_arguments += 1
