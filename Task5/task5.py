import os
import sys

def set_sit(grid, array):
    for i in array:
        grid[i[0]][i[1]] = '#'

def set_up(grid, array):
    for i in array:
        grid[i[0]][i[1]] = 'L'

def occupied(char):
    if char == '#':
        return 1
    else:
        return 0

def change_grid(grid):
    sit_down = []
    get_up = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == '.':
                continue
            count = 0
            if j == 0:
                if i == 0:
                    if (grid[i][j+1] == 'L' or grid[i][j+1] == '.') and (grid[i+1][j] == 'L' or grid[i+1][j] == '.') and (grid[i+1][j+1] == 'L' or grid[i+1][j+1] == '.'):
                        sit_down.append((i,j))
                    count += occupied(grid[i][j+1])
                    count += occupied(grid[i+1][j])
                    count += occupied(grid[i+1][j+1])
                    if count >= 4:
                        get_up.append((i,j))
                        continue

                elif i == (len(grid) - 1):
                    if (grid[i-1][j] == 'L' or grid[i-1][j] == '.') and (grid[i-1][j+1] == 'L' or grid[i-1][j+1] == '.') and (grid[i][j+1] == 'L' or grid[i][j+1] == '.'):
                        sit_down.append((i,j))
                        continue
                    count += occupied(grid[i-1][j])
                    count += occupied(grid[i-1][j+1])
                    count += occupied(grid[i][j+1])
                    continue

                else:
                    if (grid[i-1][j] == 'L' or grid[i-1][j] == '.') and (grid[i-1][j+1] == 'L' or grid[i-1][j+1] == '.') and (grid[i][j+1] == 'L' or grid[i][j+1] == '.') and (grid[i+1][j] == 'L' or grid[i+1][j] == '.') and (grid[i+1][j+1] == 'L' or grid[i+1][j+1] == '.'):
                        sit_down.append((i,j))
                        continue
                    #if grid[i-1][j] == '#' or grid[i-1][j+1] == '#' or grid[i][j+1] == '#' or grid[i+1][j] == '#' or grid[i+1][j+1] == '#':
                    count += occupied(grid[i-1][j])
                    count += occupied(grid[i-1][j+1])
                    count += occupied(grid[i][j+1])
                    count += occupied(grid[i+1][j])
                    count += occupied(grid[i+1][j+1])
                    if count >= 4:
                        get_up.append((i,j))
                        continue
            elif j == (len(grid[i]) - 1):
                if i == 0:
                    if (grid[i][j-1] == 'L' or grid[i][j-1] == '.') and (grid[i+1][j-1] == 'L' or grid[i+1][j-1] == '.') and (grid[i+1][j] == 'L' or grid[i+1][j] == '.'):
                        sit_down.append((i,j))
                        continue
                    count += occupied(grid[i][j-1])
                    count += occupied(grid[i+1][j-1])
                    count += occupied(grid[i+1][j])
                    if count >= 4:
                        get_up.append((i,j))
                        continue

                elif i == (len(grid) - 1):
                    if (grid[i-1][j] == 'L' or grid[i-1][j] == '.') and (grid[i-1][j-1] == 'L' or grid[i-1][j-1] == '.') and (grid[i][j-1] == 'L' or grid[i][j-1] == '.'):
                        sit_down.append((i,j))
                        continue
                    count += occupied(grid[i-1][j])
                    count += occupied(grid[i-1][j-1])
                    count += occupied(grid[i][j-1])
                    if count >= 4:
                        get_up.append((i,j))
                        continue
                else:
                    if (grid[i-1][j] == 'L' or grid[i-1][j] == '.') and (grid[i-1][j-1] == 'L' or grid[i-1][j-1] == '.') and (grid[i][j-1] == 'L' or grid[i][j-1] == '.') and (grid[i+1][j-1] == 'L' or grid[i+1][j-1] == '.') and (grid[i+1][j] == 'L' or grid[i+1][j] == '.'):
                        sit_down.append((i,j))
                        continue
                    count += occupied(grid[i-1][j])
                    count += occupied(grid[i-1][j-1])
                    count += occupied(grid[i][j-1])
                    count += occupied(grid[i+1][j-1])
                    count += occupied(grid[i+1][j])
                    if count >= 4:
                        get_up.append((i,j))
                        continue
            elif i == 0:
                if (grid[i][j-1] == 'L' or grid[i][j-1] == '.') and (grid[i+1][j-1] == 'L' or grid[i+1][j-1] == '.') and (grid[i+1][j] == 'L' or grid[i+1][j] == '.') and (grid[i+1][j+1] == 'L' or grid[i+1][j+1] == '.') and (grid[i][j+1] == 'L' or grid[i][j+1] == '.'):
                    sit_down.append((i,j))
                    continue
                count += occupied(grid[i][j-1])
                count += occupied(grid[i+1][j-1])
                count += occupied(grid[i+1][j])
                count += occupied(grid[i+1][j+1])
                count += occupied(grid[i][j+1])
                if count >= 4:
                    get_up.append((i,j))
                    continue
            elif i == (len(grid) - 1):
                if (grid[i][j-1] == 'L' or grid[i][j-1] == '.') and (grid[i-1][j-1] == 'L' or grid[i-1][j-1] == '.') and (grid[i-1][j] == 'L' or grid[i-1][j] == '.') and (grid[i-1][j+1] == 'L' or grid[i-1][j+1] == '.') and (grid[i][j+1] == 'L' or grid[i][j+1] == '.'):
                    sit_down.append((i,j))
                    continue
                count += occupied(grid[i][j-1])
                count += occupied(grid[i-1][j-1])
                count += occupied(grid[i-1][j])
                count += occupied(grid[i-1][j+1])
                count += occupied(grid[i][j+1])
                if count >= 4:
                    get_up.append((i,j))
                    continue
            else:
                if (grid[i-1][j] == 'L' or grid[i-1][j] == '.') and (grid[i-1][j+1] == 'L' or grid[i-1][j+1] == '.') and (grid[i][j+1] == 'L' or grid[i][j+1] == '.') and (grid[i+1][j+1] == 'L' or grid[i+1][j+1] == '.') and (grid[i+1][j] == 'L' or grid[i+1][j] == '.') and (grid[i+1][j-1] == 'L' or grid[i+1][j-1] == '.') and (grid[i][j-1] == 'L' or grid[i][j-1] == '.') and (grid[i-1][j-1] == 'L' or grid[i-1][j-1] == '.'):
                    sit_down.append((i,j))
                    continue
                count += occupied(grid[i-1][j])
                count += occupied(grid[i-1][j+1])
                count += occupied(grid[i][j+1])
                count += occupied(grid[i+1][j+1])
                count += occupied(grid[i+1][j])
                count += occupied(grid[i+1][j-1])
                count += occupied(grid[i][j-1])
                count += occupied(grid[i-1][j-1])
                if count >= 4:
                    get_up.append((i,j))
                    continue
    set_sit(grid, sit_down)
    set_up(grid, get_up)

def isequal(left, right):
    for i in range(0, len(left) - 1):
        for j in range(0, len(left[i]) - 1):
            if left[i][j] != right[i][j]:
                return False
    return True

def print_grid(grid):
    for i in grid:
        for j in i:
            print(f'{j}', end='')
        print('\n', end='')

def run_algorithm(grid):
    done = False
    count = 0
    while not done:
        temp = []
        count += 1
        for i in grid:
            temp.append(i.copy())
        change_grid(grid)
        if isequal(temp, grid):
            done = True;
    print_grid(grid)

def main():
    lines = sys.stdin.read().split("\n")

    lines = lines if lines[-1] != '' else lines[:-1]

    grid = []

    for i in range(0, len(lines)):
        grid.append([lines[i][j] for j in range(0, len(lines[i]))])

    run_algorithm(grid)

if __name__ == '__main__':
    main()
