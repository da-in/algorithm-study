def solution(N, number):
    answer = -1
    result = [[]]
    
    for i in range(1, 9):
        tmp_list = []
        tmp_list.append(int(str(N) * i))

        for j in range(1, i):
            for num1 in result[j]:
                for num2 in result[i - j]:
                    tmp_list.append(num1 + num2)
                    tmp_list.append(num1 * num2)
                    tmp_list.append(num1 - num2)
                    if num2 != 0:
                        tmp_list.append(num1 // num2)
                        
        tmp_list = list(set(tmp_list))
        
        if number in tmp_list:
            print(tmp_list)
            return i
        
        result.append(tmp_list)

    return answer