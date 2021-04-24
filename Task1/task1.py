import os
import sys

def fact(num):
    total = 1
    for counter in range(1, num + 1):
        total *= counter

    return total

def counter_zeros(num):
    counter_zero = 0

    while num > 0:
        temp =  num % 10
        if temp == 0:
            counter_zero += 1
        num /= 10

    return counter_zero

def main():
    lines = sys.stdin.read().split("\n")

    lines = lines if lines[-1] != '' else lines[:-1]

    for i in range(0, len(lines)):
        num = int(lines[i])

        factorial = fact(num)
        zeros = counter_zeros(factorial)

        print(f'{zeros}')


if __name__ == '__main__':
    main()
