import re

input_data = 'input.txt'


keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
ignored_keys = ['cid']


def is_valid_passport(passport):
    present_keys = []
    
    for pair in passport.split():
        key, value = pair.split(':')
        if key not in ignored_keys:
            present_keys.append(key)
            if key == 'byr':
                if not re.search('^\d{4}$', value) or not 1920 <= int(value) <= 2002:
                    return False
            elif key == 'iyr':
                if not re.search('^\d{4}$', value) or not 2010 <= int(value) <= 2020:
                    return False
            elif key == 'eyr':
                if not re.search('^\d{4}$', value) or not 2020 <= int(value) <= 2030:
                    return False
            elif key == 'hgt':
                match = re.search('^(\d{2,3})(cm|in)$', value)
                if not match:
                    return False
                if match.group(2) == 'cm':
                    if not 150 <= int(match.group(1)) <= 193:
                        return False
                else:
                    if not 59 <= int(match.group(1)) <= 76:
                        return False
            elif key == 'hcl':
                if not re.search('^#[a-f0-9]{6}$', value):
                    return False
            elif key == 'ecl':
                if not value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    return False
            elif key == 'pid':
                if not re.search('^\d{9}$', value):
                    return False

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
