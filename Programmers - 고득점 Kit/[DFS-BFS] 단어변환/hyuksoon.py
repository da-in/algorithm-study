from collections import deque
def solution(begin, target, words):
    answer = 0
    
    def find(word,cnt):
        
        for idx,w in enumerate(words):
            if not visit[idx]:
                ck=0
                for i in range(len(w)):
                    if w[i]!=word[i]:
                        ck+=1
                if ck==1:
                    visit[idx]=True
                    q.append([w,cnt+1])
            
    q=deque()
    q.append([begin,0])
    visit=[False]*(len(words))
    while q:
        word,cnt=q.popleft()
        if word==target:
            return cnt
        find(word,cnt)
            
    return answer
