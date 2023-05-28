"""

<aside>
💡 **Q6.** Given an integer array nums and an integer k, return the kth smallest element in the array. Note that it is the kth smallest element in the sorted order, not the kth distinct element.

**Example 1:**

Input: nums = [3,2,1,5,6,4], k = 2

Output: 2

Algorithm:
1. Create a mini heap and add all elements from the array into the heap 1 by 1
2. Heap will store k largest element at any point 
3. pop the smallest element which is kth smallest element

"""

import heapq

def kSmallestElement(array:list,k:int)->int:
    return heapq.nsmallest(k,array)[-1]


if __name__=="__main__":
    print(kSmallestElement([3,2,1,5,6,4], k = 2))
    