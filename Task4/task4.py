import os
import sys

def main():
    lines = sys.stdin.read().split("\n")
    lines = lines if lines[-1] != '' else lines[:-1]
    arr = []
    print("Test")
    for i in range(1, len(lines)):
        arr.append(lines[i])
    print("ree")
    rtn = arr[1:] + arr[:1]
    print(rtn)



if __name__ == '__main__':
    print("Hello")
    main()
