import os
import sys

def start_maximal(node, nodes, connections):
    temp = [i for i in nodes]

    for i in connections:
        if i[0] == node:
            temp.remove(i[1])
        if i[1] == node:
            temp.remove(i[0])

    return temp


def solve(nodes, connections):
    split = len(nodes) / 2
    over = []
    for i in nodes:
        over.append(start_maximal(i, nodes, connections))

    filter_list = []
    for i in over:
        if len(i) == split:
            filter_list.append(i)

    for ind, i in enumerate(filter_list):
        for ind2, j in enumerate(filter_list):
            temp1 = set(i)
            temp2 = set(j)
            if ind == ind2:
                continue
            if temp1.intersection(temp2) != set({}):
                filter_list.remove(j)
                break
    print(filter_list)
    if len(filter_list) == 2:
        print('True')
    else:
        print('False')



def main():
    lines = sys.stdin.read().split("\n")

    lines = lines if lines[-1] != '' else lines[:-1]

    nodes = set({})

    connections = []

    for i in range(0, len(lines)):
        nodes.add(lines[i][0])
        nodes.add(lines[i][1])

        connections.append((lines[i][0], lines[i][1]))

    print(nodes)
    print(connections)
    solve(nodes, connections)

if __name__ == '__main__':
    main()
