input_file = 'input.txt'

rows = 128
columns = 8


def get_position(bpass):
    pass_rows = bpass[:7]
    pass_columns = bpass[7:]

    row = (0, rows)
    column = (0, columns)

    for c in pass_rows:
        if c == 'F':
            row = (row[0], (row[0] + row[1])/2)
        elif c == 'B':
            row = ((row[0] + row[1])/2, row[1])

    for c in pass_columns:
        if c == 'L':
            column = (column[0], (column[0] + column[1])/2)
        elif c == 'R':
            column = ((column[0] + column[1])/2, column[1])

    return (int(row[0]), int(column[0]))


def get_id(position):
    return position[0] * 8 + position[1]


def get_highest_id(bpasses):
    highest = 0

    for bpass in bpasses:
        bpass_id = get_id(get_position(bpass))
        if bpass_id > highest:
            highest = bpass_id

    return highest


def main():
    with open(input_file) as f:
        print(get_highest_id(f.read().split('\n')))


if __name__ == '__main__':
    main()
