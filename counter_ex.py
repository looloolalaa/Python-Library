from collections import Counter

if __name__ == '__main__':
    # similar to 'defaultdict(int)'

    # ex1
    inputs = [1, 2, 2, 3, 3, 4, 4, 4, 4, 0]
    print(Counter(inputs))

    # ex2
    x_counter = Counter()
    for i in inputs:
        x_counter[i] += 1
    print(x_counter)
