def main():
    terms =  ["Z 3", "D 5"]
    privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
    today = "2020.01.01"
    print(solution(today,terms,privacies))

def solution(today, terms, privacies):
    answer = []
    dict = return_dict(terms)
    today = today

    for i in range(len(privacies)):
        privacies_split = privacies[i].split(" ")
        if date(today,dict,privacies_split[0],privacies_split[1]) == False:
            answer.append(i+1)
    return answer

def return_dict(terms):
    dict={}
    for i in range(len(terms)):
        dict[terms[i].split(" ")[0]] = terms[i].split(" ")[1]
    return dict
 
# today[0] : year
# today[1] : month
# today[2] : day
def date(today,dict,due,term):
    validateMonth = int(dict[term])
    today = list(map(int,today.split(".")))
    due = list(map(int,due.split(".")))
    m = due[1] + validateMonth
    if m > 12:
        due[0] += m // 12
        due[1] = m % 12
    else:
        due[1] = m 
    if due[2] == 1:
        due[2] = 28
        if due[1] > 1:
            due[1] -= 1
        else:
            due[1] = 12
            due[0] -= 1
    else : due[2] -= 1  

    # 날짜 비교
    if today[0] > due[0]:
        return False
    elif today[0] == due[0] :
        if today[1] > due[1] :
            return False
        elif today[1] == due[1]:
            if today[2] > due[2]:
                return False
    return True


if __name__ == "__main__":
    main()