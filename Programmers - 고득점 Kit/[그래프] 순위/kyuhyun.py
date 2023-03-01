def solution(n, results):
    answer = 0
    dict = {}

    for i in range(1, n + 1):
        dict[i] = {"win": set(), "lose": set()}

    for winner, loser in results:
        dict[winner]["lose"].add(loser)
        dict[loser]["win"].add(winner)

    for i in range(1, n+1):
        # 나한테 진 사람의 명단을 나에게 이긴 사람의 "lose" 명단에 추가해줘야 함
        for winner in dict[i]["win"]:
            dict[winner]["lose"].update(dict[i]["lose"])
        # 나한테 이긴 사람의 명단을 나에게 진 사람의 "win" 명단에 추가해줘야 함    
        for loser in dict[i]["lose"]:
            dict[loser]["win"].update(dict[i]["win"])

    for i in range(1, n+1):
        if len(dict[i]["win"]) + len(dict[i]["lose"]) == n-1:
            answer += 1

    return answer
