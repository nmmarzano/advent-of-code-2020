input_data = 'input.txt'
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
ignored_keys = ['cid']


def is_valid_passport(passport):
    present_keys = []
    
    for pair in passport.split():
        key = pair.split(':')[0]
        if key not in ignored_keys:
            present_keys.append(key)

    return set(present_keys) == set(keys)


def count_valid_passports(passports):
    count = 0

    for passport in passports:
        if is_valid_passport(passport):
            count += 1

    return count


def main():
    with open(input_data) as f:
        print(count_valid_passports(f.read().split('\n\n')))


if __name__ == '__main__':
    main()
