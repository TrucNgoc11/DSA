from typing import List


def get_min_distortion(packets: List[int], max_frame: int) -> int:
    #Time: O(max_frame * n)
    #Space: O(1)
    ans = float("inf")
    for val in range(max_frame + 1):
        ans = min(ans, get_distortion(packets, val))
    return ans


def get_distortion(packets: List[int], replace_val: int) -> int:
    #Time: O(n)
    #Space: O(1)
    if len(packets) < 2:
        return 0
    ans = 0
    for idx in range(1, len(packets)):
        prev_val = packets[idx - 1] if packets[idx - 1] != 0 else replace_val
        cur_val = packets[idx] if packets[idx] != 0 else replace_val
        ans = max(ans, abs(prev_val - cur_val))
    return ans


def test():
    test_case = [
        ([0], 1),
        ([4,0,3,2], 2),
        ([0,0,3,1], 4)
    ]
    for packets, max_frame in test_case:
        print(get_min_distortion(packets, max_frame))


test()

