input_data = 'input.txt'


def count_answers(results):
    answers = set()
    for line in results.split('\n'):
        answers.update(set(line))
    return len(answers)


def answer_count_sum(groups):
    total = 0
    for group in groups:
        total += count_answers(group)
    return total


def main():
    with open(input_data) as f:
        print(answer_count_sum(f.read().split('\n\n')))


if __name__ == '__main__':
    main()
