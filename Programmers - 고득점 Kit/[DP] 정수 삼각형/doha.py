def solution(triangle):
    n = len(triangle)
    result = [[0] * n for _ in range(n)]   
    result[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                result[i][j] = result[i-1][j] + triangle[i][j]
                
            elif j == len(triangle[i])-1:
                result[i][j] = result[i-1][j-1] + triangle[i][j]
                
            else:
                result[i][j] = max(result[i-1][j] + triangle[i][j], result[i-1][j-1] + triangle[i][j])
        
    return max(result[-1])