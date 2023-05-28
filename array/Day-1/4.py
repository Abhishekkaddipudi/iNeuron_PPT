"""

💡 **Q4.** Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

**Example:**

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation:

nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.

nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.

nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].

Notice that the order of the output and the order of the triplets does not matter.

Algorithm:

1. Sort the array 
2. if current value >0 , break the loop 
  -> if current value is same as one before skip it 
  -> call 2sum for current positon
  2sum:
  1. set l= i+1,h=lastindex
  2. while l<h:
        if sum of num[l] and num[h]<-num[i]:
            increament l
        elif num[l]+num[h]>-num[i]:
            decreament h
        else:
            add triplets to ans
            increament l
            decreamnet h


TC: O(n^2)

SC : O(n) depending on which sorting algo is used
"""




from typing import List

def threeSum( nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSumII(nums, i, res)
    return res

def twoSumII(nums: List[int], i: int, res: List[List[int]]):
    lo, hi = i + 1, len(nums) - 1
    while (lo < hi):
        sum = nums[i] + nums[lo] + nums[hi]
        if sum < 0:
            lo += 1
        elif sum > 0:
            hi -= 1
        else:
            res.append([nums[i], nums[lo], nums[hi]])
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo - 1]:
                lo += 1



if __name__=="__main__":
    print(threeSum([-1,0,1,2,-1,-4]))
