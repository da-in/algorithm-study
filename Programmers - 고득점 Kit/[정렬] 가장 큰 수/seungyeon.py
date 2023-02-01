from itertools import permutations
maxStr = ""
def main():
    # [6, 10, 2]
    numbers=[1, 10, 100, 1000, 818, 81, 898, 89, 0, 0] 
    solution(numbers)

def solution(numbers):

    per = list(permutations(numbers,len(numbers)))

    rows=len(per)
    cols=len(numbers)
    arr = [""*cols]*rows

    # 비효율. DFS는 시간초과
    for i in range(rows):
        for j in range(len(per[i])):
            arr[i] += str(per[i][j])
        arr[i] = int(arr[i])

    arr = sorted(arr)
    return str(arr[len(arr)-1])



if __name__ == "__main__":
    main()

    # s = "".join(str(numbers[1]))
