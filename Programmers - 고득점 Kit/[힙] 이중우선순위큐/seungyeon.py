def main():
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", 
                    "I 97", "D 1", "D -1", "I 333"]))

def solution(operations):
    answer = [0,0]
    que = []
    for oper in operations:
        c,n=oper.split(" ")
        if c == 'I':
            que.append(int(n))
        elif c == 'D':
            if que:
                if n == '1' :
                    que.remove(max(que))
                elif n == '-1':
                    que.remove(min(que))
    if que: 
        answer[0] = max(que)
        answer[1] = min(que)
    else: 
        answer[0] = 0
        answer[1] = 0

    return answer
if __name__ == "__main__":
    main()