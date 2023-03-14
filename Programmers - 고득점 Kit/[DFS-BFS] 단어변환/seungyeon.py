from collections import deque


def main():
    print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))  

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    v = [ 0 for i in range(len(words))]

    while q:
        word, cnt = q.popleft()

        if word == target:
            answer = cnt
            break 

        for i in range(len(words)):
            cnt = 0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        cnt += 1
                if cnt == 1:
                    q.append([words[i], cnt+1])
                    v[i] = 1
                    
    return answer


if __name__ == "__main__":
    main()