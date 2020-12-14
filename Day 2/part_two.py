input_data = 'input.txt'

def is_valid_password(lo, hi, letter, pw):
    count = 0

    if pw[lo - 1] == letter:
        count += 1
    if pw[hi - 1] == letter:
        count += 1

    return count == 1


def count_valid_passwords(pws):
    count = 0
    
    for line in pws:
        limits, letter, pw = line.split(' ')
        lo, hi = map(int, limits.split('-'))
        letter = letter[0]
        if is_valid_password(lo, hi, letter, pw):
            count += 1
            
    return count


def main():
    with open(input_data) as f:
        print(count_valid_passwords(f.read().split('\n')))


if __name__ == '__main__':
    main()
