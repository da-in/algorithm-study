def solution(s):
    nums = list(map(int, s.split(" ")))
    return str(min(nums)) + " " + str(max(nums))
