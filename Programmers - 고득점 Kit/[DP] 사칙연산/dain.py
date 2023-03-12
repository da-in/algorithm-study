def solution(arr):
    Infinity = float("inf")
    num_len = len(arr) // 2 + 1
    max_arr = [[-Infinity for j in range(num_len)] for i in range(num_len)]
    min_arr = [[Infinity for j in range(num_len)] for i in range(num_len)]

    for i in range(num_len):
        max_arr[i][i] = min_arr[i][i] = int(arr[i * 2])

    for l in range(1, num_len):
        for i in range(num_len - l):
            j = i + l
            for k in range(i, j):
                if arr[k * 2 + 1] == "+":
                    max_arr[i][j] = max(
                        max_arr[i][j], max_arr[i][k] + max_arr[k + 1][j]
                    )
                    min_arr[i][j] = min(
                        min_arr[i][j], min_arr[i][k] + min_arr[k + 1][j]
                    )
                else:
                    max_arr[i][j] = max(
                        max_arr[i][j], max_arr[i][k] - min_arr[k + 1][j]
                    )
                    min_arr[i][j] = min(
                        min_arr[i][j], min_arr[i][k] - max_arr[k + 1][j]
                    )
    return max_arr[0][num_len - 1]
