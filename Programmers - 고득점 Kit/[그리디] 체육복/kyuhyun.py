def solution(n, lost, reserve):
 
    students = [1] * n
    
    # 체육복이 한개도 없는사람
    for i in list(set(lost) - set(reserve)):
        students[i-1] = 0
    # 체육복이 2개 있는 사람
    for i in list(set(reserve) - set(lost)):
        students[i-1] = 2
    
    # 첫번째랑 마지막 처리
    if students[0] == 0 and students[1] == 2:
        students[0] = students[1] = 1
    
    if students[n-1] == 0 and students[n-2] == 2:
        students[n-1] =  students[n-2] = 1

    # 없는 사람한테 나눠주기
    for i in range(1, len(students)-1):
        if students[i] == 0:
            if students[i-1] == 2:
                students[i-1] = students[i] = 1
                continue
            
            elif students[i+1] == 2:
                students[i+1] = students[i] = 1

    return n - students.count(0)
