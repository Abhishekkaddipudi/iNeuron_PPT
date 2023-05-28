"""
💡 **Q3.** Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

**Example:**

Input: nums = [2,3,-2,4]

Output: 6

Explanation: [2,3] has the largest product 6.


Algorithm:

1. initialte res=0
    while traversing numbers , we have to keep track of max product up untill that number (max_so_far)
    and min product up untill that number (min_so_far)
2. max_so_far = max(max_so_Far*curr,min_so_Far*curr,curr)
   min_so_far= min(max_so_Far*curr,min_so_Far*curr,curr)
3. update res= max(res,max_so_far)  


TC : O(n)

SC: O(1)
"""
from typing import List

def maxProduct(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

        max_so_far = temp_max

        result = max(max_so_far, result)

    return result


if __name__ =="__main__":
    print(f"max_product_Subarray={maxProduct([2,3,-2,4])}")