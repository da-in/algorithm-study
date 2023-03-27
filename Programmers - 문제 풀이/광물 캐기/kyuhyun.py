def solution(picks, minerals):
    k = 0
    hp = 0
    
    if sum(picks)*5 < len(minerals):
        minerals = minerals[:sum(picks)*5]
        
    l = len(minerals) // 5 + 1
    mineral = [[0 for _ in range(3)] for _ in range(l)]


    for i in range(len(minerals)):
        val = minerals[i]
        if val == "diamond":
            mineral[k][0] += 1
        elif val == "iron":
            mineral[k][1] += 1    
        else:
            mineral[k][2] += 1
        if i % 5 == 4:
            k += 1    

    mineral.sort(key=lambda x : (x[0], x[1], x[2]))
    
    for i in range(len(picks)):
        val = picks[i]
        while val and mineral:
            x, y, z = mineral.pop()
            if i == 0:
                hp += x + y + z
            elif i == 1:
                hp += x * 5 + y * 1 + z * 1
            else:
                hp += x * 25 + y * 5 + z * 1    
            val -= 1  
    return hp
