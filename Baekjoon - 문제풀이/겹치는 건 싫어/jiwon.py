import sys

n,k = map(int, sys.stdin.readline().split())
value_list = list(map(int, sys.stdin.readline().split()))
max_value = 0

def solution(value_list):
    value_dict = dict()

    for i in range(n):
        value = value_list[i]
        if value not in value_dict:
            value_dict[value] = 1
        elif value in value_dict:
            if value_dict[value]+1>k:
                temp = value_list.index(value)
                value_list = value_list[temp:]
                max_value = sum(value_dict.values())
                if len(value_list)>max_value:
                    return solution(value_list)
                break
            value_dict[value]+=1
    return 0

print(solution(value_list))

