def main():
    print(solution([2, 1, 3, 2],2))


def solution(priorities, location):
    answer = 1
    m = max(priorities)

    while True:
        temp = priorities.pop(0)

        if temp == m :
            if location == 0:
                return answer
            answer += 1
            location -= 1
            m = max(priorities)
        else:
            priorities.append(temp)
            if location == 0:
                location = len(priorities ) -1
            else:
                location -= 1


if __name__ == "__main__":
    main()