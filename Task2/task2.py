import os
import sys

def main():
    lines = sys.stdin.read().split("\n")

    lines = lines if lines[-1] != '' else lines[:-1]

    n = m = k = 0
    bad = []
    for i in range(0, len(lines)):
        if i == 0:
            n, m, k  = lines[i].split(" ")
            continue

        dim1, dim2 = lines[i].split(" ")
        bad.append([dim1, dim2])

    
if __name__ == '__main__':
    main()
