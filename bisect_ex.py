from bisect import bisect_left, bisect_right

if __name__ == '__main__':
    temp = [1,3,3,3,5]

    def bs_left(k):
        left, right = 0, len(temp)-1
        while left <= right:
            mid = (left+right)//2
            if k <= temp[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # print(right, left)
        return left

    def bs_right(k):
        left, right = 0, len(temp)-1
        while left <= right:
            mid = (left+right)//2
            if temp[mid] <= k:
                left = mid + 1
            else:
                right = mid - 1
        # print(right, left)
        return left

    print(bisect_left(temp, 3))
    print(bs_left(3))
    print()
    print(bisect_right(temp, 3))
    print(bs_right(3))