from itertools import product
def solution(word):
    c = ["A","E", "I", "O", "U"]
    res = []
    for i in range(1, 6):
        for str in product(c, repeat=i) :
            res.append("".join(str))

    res.sort()        
    
    return res.index(word) + 1
