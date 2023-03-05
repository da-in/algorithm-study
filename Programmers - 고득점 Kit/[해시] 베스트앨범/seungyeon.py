
    
def main():
    print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))

def solution(genres, plays):
    answer = []

    total={}
    genre={}
    
    for i in range(len(genres)):
        if genres[i] in total:
            total[genres[i]] += plays[i]
        else:
            total[genres[i]] = plays[i]
        if genres[i] in genre:
            genre[genres[i]].append([plays[i],i])
        else:
            genre[genres[i]] = [[plays[i],i]]
    
    sort_total = sorted(total,reverse=True)

    for x in sort_total:
        sort_genre = sorted(genre[x],key=lambda x: (-x[0],x[1])) #내림차순, 오름차순

        if len(sort_genre) == 1: # 1개일 경우
            answer.append(sort_genre[0][1])
        else:
            for i in range(2): # 2개일 경우 
                answer.append(sort_genre[i][1])

    
    # n = arr.pop(-1)
    # print(n)
    # answer.append(arr.pop(-1))
    
    # print(arr.pop(-1))
    
    return answer
    
if __name__ == "__main__":
    main()