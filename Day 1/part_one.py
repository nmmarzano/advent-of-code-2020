input_data = 'input.txt'


def find_sum(nums, target):
    for i in range(len(nums) - 1):
        if nums[i] > target:
            continue
        if target - nums[i] in nums[i + 1:]:
            return (nums[i], target - nums[i])


def main():
    with open(input_data) as f:
        input_list = [int(line) for line in f.read().split('\n')]
        answer = find_sum(input_list, 2020)
        print(answer[0] * answer[1])


if __name__ == '__main__':
    main()
