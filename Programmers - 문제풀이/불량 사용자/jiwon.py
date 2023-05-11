def solution(user_id, banned_id):
    answer = 0
    
    user_id.sort()
    user_id.sort(key = lambda x: len(x))
    
    for b in banned_id:
        for u in user_id:
            if len(b)==len(u):
                pass
            
    return answer