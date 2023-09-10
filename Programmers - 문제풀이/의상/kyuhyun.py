def solution(clothes):
    answer = 1
    types = {}
    
    for wear, clothes_type in clothes:
        if clothes_type in types:
            types[clothes_type] += 1
        else:
            types[clothes_type] = 1
            
    for val in types.values():
        answer *= (val + 1)

    return answer - 1
