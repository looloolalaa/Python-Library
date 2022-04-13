import itertools

if __name__ == '__main__':
    target = [0, 1, 2, 3, 4]
    print(list(itertools.combinations(target, 3)))
    print(list(itertools.permutations(target, 3)))
    print(list(itertools.product(target, repeat=3)))
    print(list(itertools.combinations_with_replacement(target, 3)))
    # 5H3

