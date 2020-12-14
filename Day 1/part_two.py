from functools import reduce

input_data = 'input.txt'


def find_sum_recursive(nums, target, quantity):
    if quantity  == 1:
        if target in nums:
            return [target]
        else:
            return None
    else:
        members = []
        for i in range(len(nums) - 1):
            if nums[i] > target:
                continue
            members = find_sum_recursive(nums[i + 1:], target - nums[i], quantity - 1)
            if not members == None:
                members.append(nums[i])
                return members
        if members == None or members == []:
            return None


def find_sum_iterative(nums, target):
    for i in range(len(nums) - 1):
        if nums[i] > target:
            continue
        new_target = target - nums[i]

        for j in range(i + 1, len(nums) - 1):
            if nums[j] > new_target:
                continue
            if new_target - nums[j] in nums[j + 1:]:
                return (nums[i], nums[j], new_target - nums[j])


def main():
    with open(input_data) as f:
        input_list = [int(line) for line in f.read().split('\n')]
    
        answer = find_sum_recursive(input_list, 2020, 3)
        # answer = find_sum_iterative(input_list, 2020)
        if not answer == None:
            print(reduce((lambda x, y: x * y), answer))
        else:
            print('No answer found.')


if __name__ == '__main__':
    main()
