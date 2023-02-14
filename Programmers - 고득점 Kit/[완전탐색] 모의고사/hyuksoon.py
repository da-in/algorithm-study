def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt=[0,0,0]
    for i in range(len(answers)):
        if a[i%5]==answers[i]:
            cnt[0]+=1
        if b[i%8]==answers[i]:
            cnt[1]+=1   
        if c[i%10]==answers[i]:
            cnt[2]+=1
    
    return [i+1 for i in range(3) if cnt[i]==max(cnt)]
