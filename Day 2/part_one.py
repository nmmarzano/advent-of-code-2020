input_data = 'input.txt'


def is_valid_password(lo, hi, letter, pw):
    count = 0
    
    for c in pw:
        if c == letter:
            count += 1
        if count > hi:
            return False

    return count >= lo


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
