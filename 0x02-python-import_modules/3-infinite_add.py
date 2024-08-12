#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    output = 0
    args = sys.argv
    for i in args:
        if i != sys.argv[0]:
            output += int(i)
    print(output)
