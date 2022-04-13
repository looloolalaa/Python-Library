if __name__ == '__main__':
    temp = ['asd', 'aa', 'b', 'abc']
    temp.sort(key=lambda x: (len(x), x))
    # 길이로 정렬 후, 길이가 같으면 사전순 정렬

    temp2 = [(0, 0), (4, -1), (2, 2), (3, 9), (-2, 0), (4, 4)]
    temp2.sort(key=lambda x: (x[0], -x[1]))
    # 첫 번째 요소로 오름차순 정렬 후, 값이 같으면 두 번째 요소로 내림차순 정렬
    print(temp2)
