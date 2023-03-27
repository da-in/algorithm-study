def solution(s):
    data=list(map(int, s.split(" ")))
    return str(min(data))+" "+str(max(data))