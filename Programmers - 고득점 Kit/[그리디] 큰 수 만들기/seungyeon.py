# 보이는 대로 작으느 수를 빼면 됨.

import heapq
def main():
    print(solution("177252841",4))

def solution(number, k):
    stack=[]
    for num in number:
        while stack and stack[-1] < num and k > 0: # ***
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack)
    
if __name__ == "__main__":
    main()