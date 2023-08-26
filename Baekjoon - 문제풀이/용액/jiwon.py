import sys

N = int(input())
solution_list = list(map(int, sys.stdin.readline().split()))
sum = 2000000000

for i in range(N):
    current = solution_list[i]

    start = i+1
    end = N-1

    while start<=end:
        mid = (start+end)//2
        temp_sum = current + solution_list[mid]

        if abs(temp_sum) < sum:
            sum = abs(temp_sum)
            result = (solution_list[i], solution_list[mid])

            if result == 0:
                break

        if temp_sum < 0:
            start = mid+1
        else:
            end = mid-1

print(result[0], result[1])