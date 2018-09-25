# n, m = [int(x) for x in input().split()]
# arr1 = [int(x) for x in input().split()]
# arr2 = [int(x) for x in input().split()]



def bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


N, M = input().split()
list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]

for x in list2:
    i = bisect_left(list1, x)
    try:
        if list1[i] == x:
            print(i + 1, bisect_right(list1, x, i))
    except IndexError:
        print("0")


def binary_search(lst, x):
    lower_bound = 0
    upper_bound = len(lst)
    while lower_bound != upper_bound:
        compared_value = (lower_bound + upper_bound) // 2  # Целочисленный тип в Python имеет неограниченную длину
        if x == lst[compared_value]:
            return compared_value
        elif x < lst[compared_value]:
            upper_bound = compared_value
        else:
            lower_bound = compared_value + 1
    return None  # если цикл окончен, то значение не найденно

    # else:
    #     print(0)
