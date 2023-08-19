from typing import List

def quick_sort(num_list: List, l, r) -> List:
    if l >= r:
        return
    i, j = l , r
    pivot = num_list[(l + r) // 2]
    while i <= j:
        while num_list[i] < pivot:
            i += 1
        while num_list[j] > pivot:
            j -= 1
        if i <= j:
            num_list[i], num_list[j] = num_list[j], num_list[i]
            i += 1
            j -= 1
    quick_sort(num_list, l, j)
    quick_sort(num_list, i, r)

def binarysearch(num_list: List, l, r, x) -> int:
    while l + 1 < r:
        mid = (l + r) // 2
        if x <= num_list[mid]:
            r = mid
        else:
            l = mid
    return True if num_list[r] == x else False


def solve():
    test_case = int(input())
    for _ in range(test_case):
        n, m = map(int, input().split())
        num_list = sorted(list(map(int, input().split())))
        ans = 0
        #quick_sort(num_list, 0 , n - 1)
        for i in range(n):
            k = m - num_list[i]
            if i < n - 1 and binarysearch(num_list, i, n - 1, k) is True:
                ans += 1
        print(ans)


solve()
