def solution(arr):
    n = len(arr)
    dp_max = [[0 for _ in range(n)] for _ in range(n)]
    dp_min = [[1001 for _ in range(n)] for _ in range(n)]

    # 숫자 담는 배열
    num = []
    # 기호 담는 배열
    log = []

    for i in range(len(arr)):
        if i % 2 == 0:
            num.append(int(arr[i]))
        else:
            log.append(arr[i])
            
    # 숫자가 1개면 step = 0, 숫자가 두개면 step = 1, ...
    for step in range(n):
        # step에 따라 만들수 있는 숫자 조합
        for i in range(n - step):

            j = i + step

            if step == 0:
                dp_max[i][i] = num[i]
                dp_min[i][i] = num[i]
            else:   
                # i 부터 j번째 수까지 괄호 하나씩 늘리면서 계산
                for k in range(i, j):
                    if log[k] == '+' :
                        dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j]) # 더하기의 최대
                        dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j]) # 더하기의 최소
                    else:
                        dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j]) # 빼기의 최대
                        dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j]) # 빼기의 최소

    return dp_max[0][n-1]
