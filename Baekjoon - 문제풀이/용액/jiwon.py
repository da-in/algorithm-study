import sys

N = input()
solution_list = list(map(int, sys.stdin.readline().split()))
MAX = 1000000000
MIN = -1000000000

sum0 = 2*MAX+1
s1,s2 = 0,0

minus1, minus2 = MIN-1, MIN-1
plus1, plus2 = MAX+1, MAX+1
index = -1
for i in range(len(solution_list)-1):
    if solution_list[i]>0:
        index = i
        break
    if solution_list[i]<0 and solution_list[i+1]<0:
        minus1, minus2 = solution_list[i], solution_list[i+1]
if index<len(solution_list)-1:
    plus1,plus2 = solution_list[index], solution_list[index+1]

# case1: 음수 중 작은거 2개
if minus1!=MIN-1 and minus2!=MIN-1:
    sum0 = -(minus1+minus2)
    s1,s2 = minus1, minus2

# case2: 양수 중 작은거 2개
if plus1!=MAX+1 and plus2!=MAX+1:
    if plus1+plus2<sum0:
        sum0 = plus1+plus2
        s1, s2 = plus1, plus2

# case3: 음수+양수
if index<len(solution_list)-1:
    for i in solution_list[:index]:
        for j in solution_list[index:]:
            sum_solution = i+j
            if sum_solution<0:
                sum_solution = -sum_solution
            if sum_solution<sum0:
                sum0 = sum_solution
                s1,s2 = i,j

print(s1, s2)

# 음수 중 작은거 2개, 양수 중 작은거 2개, 음수+양수