def solution(nums):
    answer = 0
    new_array = []
    for i in range(0, len(nums)):
        if nums[i] not in new_array:
            new_array.append(nums[i])
    if len(new_array) > len(nums) / 2:
        answer = len(nums) / 2
    else: 
        answer = len(new_array)
    
    return answer