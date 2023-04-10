def solution(s):
    answer = 1000000

    for length in range(1, len(s)+ 1):
        ts = s
        total_length = len(ts)
        slice = []
        count = 1
        
        #문자열 length 만큼 쪼개기
        while ts:
            temp = ts[:length]
            slice.append(temp)
            ts = ts[length:]
        
        # answer 구하는 연산
        for i in range(len(slice)):
            if i == len(slice) -1:
                if count > 1:
                    total_length -= length * count
                    total_length += length + len(str(count))
                break

            if slice[i] == slice[i+1]:
                count += 1

            elif count > 1:
                total_length -= length * count
                total_length += length + len(str(count))
                count = 1
    
        answer = min(answer, total_length)
    return answer
