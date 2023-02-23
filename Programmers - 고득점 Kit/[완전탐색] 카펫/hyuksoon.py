def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1):
        if yellow%i==0:
            if (2*i)+(2*(yellow//i))+4==brown:
                return [max(i+2,(yellow//i)+2),min(i+2,(yellow//i)+2)]
    return answer