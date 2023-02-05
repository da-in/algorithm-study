def solution(name):
    answer = 0
    arr= [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    i = 0
    while True:
        answer += arr[i]
        arr[i] = 0
        if sum(arr) == 0:
            break
        left,right = 1,1
        while arr[i-left] == 0:
            left += 1
        while arr[i+right] == 0:
            right += 1
        answer += left if left < right else right
        i += -left if left < right else right

    return answer