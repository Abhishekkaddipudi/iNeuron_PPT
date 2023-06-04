def MoveZeros(nums:list)->list:
    
    """
    This function moves zeros to end of the list
    """
    low=0
    high=len(nums)-1
    while low<=high:
        if nums[high]==0:
            high-=1
        elif nums[low]==0:
            nums.append(0)
            nums.pop(low)
        else:
            low+=1
            