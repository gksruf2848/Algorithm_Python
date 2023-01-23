def sosu(num):
    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1, len(nums)):
                if sosu(nums[i]+nums[j]+nums[k]):
                    answer += 1
    return answer