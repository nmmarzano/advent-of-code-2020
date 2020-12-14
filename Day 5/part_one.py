input_file = 'input.txt'

rows = 128
columns = 8


def main():
    with open(input_file) as f:
        print(len(f.readlines()))


if __name__ == '__main__':
    main()
