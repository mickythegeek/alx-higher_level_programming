#!/usr/bin/python3
for char in range(ord('a'), ord('z')+1):
    if (char != ord('q')) & (char != ord('e')):
        print('{}'.format(chr(char)), end='')
