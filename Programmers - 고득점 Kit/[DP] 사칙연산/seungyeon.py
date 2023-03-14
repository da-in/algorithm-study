def main():
    print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))

def solution(arr):
    minmax = [0, 0]
    sum_value = 0
    for idx in range(len(arr)-1, -1, -1):
        if arr[idx] == '+':
            continue
        elif arr[idx] == '-':
            tempmin, tempmax = minmax
            minmax[0] = min(-(sum_value + tempmax), -sum_value+tempmin)

            minus_v = int(arr[idx+1])
            minmax[1] = max(-(sum_value+tempmin), -minus_v+(sum_value-minus_v)+tempmax)

            sum_value = 0
        elif int(arr[idx]) >= 0:
            sum_value += int(arr[idx])
    minmax[1] += sum_value
    return minmax[1]

    
if __name__ == "__main__":
    main()