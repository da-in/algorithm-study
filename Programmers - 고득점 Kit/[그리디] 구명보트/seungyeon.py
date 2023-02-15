def main():
    print(solution([70, 80,50, 50],100))


def solution(people, limit):
    answer = 0
    people.sort()
    
    left, right = 0, len(people) - 1
    
    while left <= right:
        answer += 1
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
    
    return answer

# def solution(people,limit):
#     answer = 0
#     people.sort(reverse=True)
#     cnt = 0
#     for i in range(len(people)):
#         cnt += people[i]
#         if i < len(people)-1 and cnt + people[i+1]>limit:
#             answer += 1
#             cnt = 0
#         if i == len(people)-1:
#             answer+=1
#     return answer

# def solution(people, limit):
#     answer = 0
#     people.sort()

#     while(people):
#         if people==None: break
#         cnt ,i = 0,0
#         while(cnt <= 100):
#             if cnt <= 100: break
#             print(i)
#             cnt += people[0]
#             people.pop(0)
#             i+=1
#         answer += 1
    
#     print(people)
#     return answer

if __name__ == "__main__":
    main()