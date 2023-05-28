"""
💡 **Q5.** Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

**Example 1:**

Input: nums = [3,2,1,5,6,4], k = 2

Output: 5

Algorithm:
1. Create a mini heap and add all elements from the array into the heap 1 by 1
2. Heap will store k largest element at any point 
3. head of the heap has kth largest element

TC : O( n log k)

TC : O( k)


"""
import heapq

def kLargestelement(array:list,k:int)->int:
   return heapq.nlargest(k,array)[-1]


if __name__=="__main__":
    print(kLargestelement([3,2,1,5,6,4], k = 2))
    