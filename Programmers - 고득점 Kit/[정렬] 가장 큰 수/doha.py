import functools
def solution(numbers):
    answer = ""
    str_numbers = list(map(str, numbers))      
    
    tmp = sorted(str_numbers, key=functools.cmp_to_key(sort_num), reverse = True)
    
    answer = ''.join(tmp)
    
    return str(int(answer))
    
def sort_num(num1, num2):
    if num1 + num2 < num2 + num1:
        return -1
    elif num1 + num2 == num2 + num1:
        return 0
    else:
        return 1


# 아래는 풀리긴 하지만, 시간초과 발생해서 폐기

from itertools import permutations
def solution(numbers):
    answer = list(map(str, numbers))
    dic = {}
    for a in answer:
        dic[a[0]] = []
        
    for a in answer:
        dic[a[0]].append(a)
        
    sort_dict = list(dict(sorted(dic.items(), reverse = True)).values())
    answer = ""
    for i in range(len(sort_dict)):
        sort_dict[i] = sort_arr(sort_dict[i])
        answer += sort_dict[i]
        
    return answer

def sort_arr(arr):
    sum = ""
    tmp = []
    for a in permutations(arr, len(arr)):
        tmp.append(''.join(a))
            
    sum += max(tmp)
    
    return sum


