from itertools import permutations

def solution(word):
    answer = 0
    target=['A','A','A','A','A', 'E','E','E','E','E', 'I','I','I','I','I', 'O','O','O','O','O', 'U','U','U','U','U']
    data=set()
    for i in range(1,6):
        lists=list(permutations(target,i))
        for l in lists:
                data.add(''.join(list(l)))
    data=list(data)
    data.sort()
    
    for i in range(len(data)):
        if data[i]==word:
                return i+1
    return answer