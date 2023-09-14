def get_val(val, replace_val):
    return val if val != 0 else replace_val


def get_distortion(packets, replace_val):
    ans = float("-inf")
    for idx in range(1, len(packets)):
        ans = max(ans, abs(get_val(packets[idx], replace_val) - get_val(packets[idx - 1], replace_val)))
    # print(ans, packets, replace_val)
    return ans


def get_min_distortion(packets, max_frame):
    if len(packets) < 2:
        return 0

    l, r = -1, max_frame
    while l + 1 < r:
        mid = (l + r) // 2
        f1, f2 = get_distortion(packets, mid), get_distortion(packets, mid + 1)
        if f1 <= f2:
            r = mid
        else:
            l = mid
    return get_distortion(packets, r)


def test():
    test_case = [
        ([0], 1),
        ([4,0,3,2], 2),
        ([0,0,3,1], 4)
    ]
    for packets, max_frame in test_case:
        print(get_min_distortion(packets, max_frame))


test()