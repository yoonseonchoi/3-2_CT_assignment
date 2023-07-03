def foundSolution(final_cell) -> bool:
    for y in range(len(room)):
        for x in range(len(room[y])):
            if room[y][x] == ' ':  # cell not visited and not obstacle
                return False

    y = final_cell[0]
    x = final_cell[1]
    room[y][x] = 'F'
    return True


def output(final_cell) -> None:
    divider = ' - -' * len(room[0])

    print(f'The robot end on col {final_cell[1]}, row {final_cell[0]}\n\n')
    print(divider)

    for y in range(len(room)):
        for x in range(len(room[y])):
            txt = str(path.index([y, x])) if [y, x] in path else room[y][x]
            print('|' + txt.center(3), end='')
        print('|\n' + divider)


def listOfCandidates(current_cell) -> list[list[int]]:
    y = current_cell[0]
    x = current_cell[1]
    possible_cells: list[list[int]] = []

    for cell in [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]:  # check next possible cells
        i = cell[0]
        j = cell[1]

        # cell outside room
        if i < 0 or i >= len(room) or j < 0 or j >= len(room[i]):
            continue

        # cell not visited and not obstacle
        if room[i][j] == ' ':
            possible_cells.append([i, j])

    return possible_cells


def place(cell) -> None:
    y = cell[0]
    x = cell[1]
    room[y][x] = 'o'
    path.append(cell)


def remove(cell) -> None:
    y = cell[0]
    x = cell[1]
    room[y][x] = ' '
    path.pop()


def backtrack(candidate) -> None:
    if foundSolution(candidate):
        output(candidate)
        return

    for nextCandidate in listOfCandidates(candidate):
        place(nextCandidate)
        backtrack(nextCandidate)
        remove(nextCandidate)


path: list[list[int]] = [[2, 0]]
room: list[list[str]] = [
    [' ', ' ', ' ', ' ', 'x', ' ', ' '],
    [' ', ' ', ' ', ' ', 'x', ' ', ' '],
    ['S', ' ', ' ', ' ', ' ', ' ', ' '],
    ['x', 'x', 'x', 'x', 'x', 'x', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

backtrack(path[0])

