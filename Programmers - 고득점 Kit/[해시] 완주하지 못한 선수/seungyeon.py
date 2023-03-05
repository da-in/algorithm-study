def main():
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))

def solution(participant,completion):
    participant.sort()
    completion.sort()
    for i in range (len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    else:
        return participant[-1]

# # 시간초과
# def solution(participant, completion):
    
#     for i in range(len(completion)):
#         if completion[i] not in participant : 
#             participant.append(completion[i])
#         participant.remove(completion[i])
#     return str(participant[0])
    
if __name__ == "__main__":
    main()