# numbers 입력값
# answer 출력값
# 입력값에서 찾아서 본인보다 크면 넣고, 같으면 다음꺼 넣고, 없으면 -1



def main():
    solution([9, 1, 5, 3, 6, 2])

def solution(numbers):
    answer = []
#     answer.append(numbers.pop(0))
#     while(len(numbers) != 1):
#         if(numbers.pop(0) == answer.pop(0)):
#             numbers.insert(0)
#             answer.append(numbers.pop(0))
#             answer.pop(0)
#         else:
#             answer.append(numbers.pop(0))
#     answer.append(-1)
    return answer



# from queue import PriorityQueue
# def main():
#     print("hello?")
#     solution([9, 1, 5, 3, 6, 2])

# def solution(numbers):
#     answer = []
    
#     answer = numbers
#     sort = sorted(numbers)

#     for i in range(len(answer)):
#         for j in range(len(sort)):
#             if answer[i] < sort[j]:
#                 if(j==len(sort)-1):
#                     answer[i] = -1
#                 answer[i] = sort[j]
#             elif answer[i] == sort[j]:
#                 continue
#     print("hello")
#     print(answer)


# def solution(numbers):
#     answer = []
    
#     while(len(numbers) != 0):
#         last = numbers.pop()
#         answer.append(last)

#         if last == answer.pop():
#             numbers.insert(0,last)
#             answer.append(numbers.pop())
#             answer.pop()
#         elif (len(answer) == 0): answer.append(-1)
#         else: answer.append(numbers.pop(0))

#     print(answer)
#     return answer

if __name__ == "__main__":
    main()



#     #   answer.append(numbers.pop(0))
#     #     if(len(answer) == 0): answer.append(-1)


#     #     if(numbers.pop(0) == answer.pop(0)):
#     #         numbers.insert(0)
#     #         answer.append(numbers.pop(0))
#     #         answer.pop(0)
#     #     elif(numbers.pop(0) > answer.pop(0)):
#     #         numbers.insert(0)
#     #         answer.append(numbers.pop(0))
#     #         answer.pop(0)
#     #     else:
#     #         answer.append(numbers.pop(0))
#     # answer.append(-1)




