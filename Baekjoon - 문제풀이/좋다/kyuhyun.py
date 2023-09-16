N = int(input())
nums = list(map(int, input().split(" ")))
cnt = 0
nums.sort()

for i in range(N):
    num = nums[i]
    
    tmp = nums[:i]
    tmp.extend(nums[i+1:])

    left = 0
    right = len(tmp) - 1

    while left < right:
        union = tmp[left] + tmp[right]

        if union < num:
           left += 1
           continue
        if union > num: 
            right -= 1
            continue
        if union == num:
            cnt += 1
            break
    
print(cnt)
