def solution(s):
    l=s.split(" ")
    int_l = [int(i) for i in l]
    return str(min(int_l))+" "+str(max(int_l))