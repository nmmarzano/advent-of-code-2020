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
        input_list = f.read().split('\n')
        count = 1
        count *= count_trees(input_list, 1, 1)
        count *= count_trees(input_list, 3, 1)
        count *= count_trees(input_list, 5, 1)
        count *= count_trees(input_list, 7, 1)
        count *= count_trees(input_list, 1, 2)
        print(count)


if __name__ == '__main__':
    main()
