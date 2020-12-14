input_data = 'input.txt'


def count_trees(treemap, slope_x, slope_y):
    count = 0

    x = 0
    y = 0
    loop_limit = len(treemap[0])
    while y < len(treemap):
        if treemap[y][x % loop_limit] == '#':
            count += 1
        x += slope_x
        y += slope_y
    
    return count


def main():
    with open(input_data) as f:
        print(count_trees(f.read().split('\n'), 3, 1))


if __name__ == '__main__':
    main()
