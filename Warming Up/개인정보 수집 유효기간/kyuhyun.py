import re

def solution(today, terms, privacies):
    answer = []
    i = 0
    while(i < len(privacies)) :
        year = int(privacies[i][0:4])
        month = int(privacies[i][5:7])
        day = int(privacies[i][8:10])
        
        for j in range(len(terms)):
            if privacies[i][11] == terms[j][0]:
                month += int(re.sub(r'[^0-9]', '', terms[j]))
                             
                if month % 12 == 0 : 
                    year += (month // 12) -1 
                    month = 12
                else:
                    year += (month // 12)
                    month %= 12
        i += 1 
        expireDay = year * 10000 + month * 100 + day
            
        if int(re.sub(r'[^0-9]', '', today)) >= expireDay:
            answer.append(i)       
            
return answer

//시간복잡도가 무려 O(N^2),,
