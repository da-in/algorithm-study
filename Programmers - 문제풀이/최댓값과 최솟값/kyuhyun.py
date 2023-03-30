def solution(s):
    s = list(map(int ,s.split(" ")))
    s.sort()
    return str(s[0]) + " " +str(s[-1])
