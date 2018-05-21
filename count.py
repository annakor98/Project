import numpy as np
import matplotlib.pyplot as plt
import pygame

def color(grid):
    color = (0, 0, 255)
    ans = True
    count_capacitors = 0
    count_inductors = 0

    for i in range (len(grid)):
        if grid[i].mode == 3:
            count_capacitors += 1
        if grid[i].mode == 4:
            count_inductors += 1

    if count_inductors == 0 or count_capacitors == 0:
        ans = False

    for i in range(7):
        for j in range(5):
            s = 0
            if i < 6 and grid[(j*6) + i].mode > 0:
                s += 1
            if i > 0 and grid[(j*6) + i - 1].mode > 0:
                s += 1
            if j < 4 and grid[30 + (j*7) + i].mode > 0:
                s += 1
            if j > 0 and grid[23 + (j*7) + i].mode > 0:
                s += 1

            if s == 1:
                ans = False

    if ans:
        color = (255, 0, 0)

    return color

def count(grid, surface):
    nodes = []
    n = 0
    outputs = []
    m = 0
    elements = []

    colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow']

    for i in range(7):
        for j in range(5):
            s = 0
            c = 0
            if i < 6 and grid[(j*6) + i].mode > 0:
                s += 1
                if grid[(j*6) + i].mode > 1:
                    c += 1
            if i > 0 and grid[(j*6) + i - 1].mode > 0:
                s += 1
                if grid[(j*6) + i - 1].mode > 1:
                    c += 1
            if j < 4 and grid[30 + (j*7) + i].mode > 0:
                s += 1
                if grid[30 + (j * 7) + i].mode > 1:
                    c += 1
            if j > 0 and grid[23 + (j*7) + i].mode > 0:
                s += 1
                if grid[23 + (j * 7) + i].mode > 1:
                    c += 1

            if s > 3 or c > 1:
                nodes.append([i, j])
                n += 1

    nodes.pop()
    n -= 1

    for i in range(len(grid)):
        if grid[i].mode > 3:
            outputs.append(i)
            grid[i].col = colors[m]
            grid[i].draw(surface)
            m += 1
        if grid[i].mode > 1:
            elements.append(i)

    pygame.display.flip()

    matrix = [[0]*(m+n) for _ in range(m+n)]
    RHS = [0]*(m+n)
    h = 0.1
    current = [np.zeros(500) for _ in range(m)]
    for time in range(500):
        for i in range(n+m):
            RHS[i] = 0
            for j in range(n+m):
                matrix[i][j] = 0
        for i in elements:
            t = grid[i]
            begin = -1
            end = -1
            if [(t.x//100)-1, (t.y//100)-1] in nodes:
                begin = nodes.index([(t.x // 100) - 1, (t.y // 100) - 1])
            if t.orient == 'hor':
                if [t.x // 100, (t.y // 100 - 1)] in nodes:
                    end = nodes.index([t.x // 100, (t.y // 100 - 1)])
            else:
                if [(t.x // 100) - 1, t.y // 100] in nodes:
                    end = nodes.index([(t.x // 100) - 1, t.y // 100])

            if t.mode == 2:
                if begin != -1:
                    matrix[begin][begin] += 1000/t.value
                if end != -1:
                    matrix[end][end] += 1000/t.value
                if begin != -1 and end != -1:
                    matrix[begin][end] += -1000/t.value
                    matrix[end][begin] += -1000/t.value

            elif t.mode == 3:
                if begin != -1:
                    matrix[begin][begin] += t.value/h
                    RHS[begin] += t.value * t.prev / h
                if end != -1:
                    matrix[end][end] += t.value/h
                    RHS[end] += -t.value * t.prev / h
                if begin != -1 and end != -1:
                    matrix[begin][end] += -t.value/h
                    matrix[end][begin] += -t.value/h

            elif t.mode == 4:
                ind = outputs.index(i)
                if begin != -1:
                    matrix[n+ind][begin] += 1
                    matrix[begin][n + ind] += 1
                if end != -1:
                    matrix[n+ind][end] += -1
                    matrix[end][n+ind] += -1
                matrix[n+ind][n+ind] += -t.value/h
                RHS[n+ind] += -t.value * t.prev/h

        solution = np.linalg.solve(np.array(matrix), np.array(RHS))
        for i in elements:
            t = grid[i]
            if t.mode == 3:
                u_begin = 0
                u_end = 0
                if [(t.x//100)-1, (t.y//100)-1] in nodes:
                    begin = nodes.index([(t.x // 100) - 1, (t.y // 100) - 1])
                    u_begin = solution[begin]
                if t.orient == 'hor':
                    if [t.x // 100, (t.y // 100 - 1)] in nodes:
                        end = nodes.index([t.x // 100, (t.y // 100 - 1)])
                        u_end = solution[end]
                else:
                    if [(t.x // 100) - 1, t.y // 100] in nodes:
                        end = nodes.index([(t.x // 100) - 1, t.y // 100])
                        u_end = solution[end]

                t.prev = - u_end + u_begin

            if t.mode == 4:
                ind = outputs.index(i)
                t.prev = solution[n+ind]

        for i in range(m):
            current[i][time] = grid[outputs[i]].prev

    x = np.linspace(0, 50, 500)
    plt.figure()
    for i in range(m):
        plt.plot(x, current[i], color=grid[outputs[i]].col)

    plt.xlabel(r'$Time, sec$')
    plt.ylabel(r'$Amperage, A$')

    plt.show()

