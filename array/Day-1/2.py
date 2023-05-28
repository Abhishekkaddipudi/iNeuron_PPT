
"""
💡 **Q2.** You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**Example :**

Input: prices = [7,1,5,3,6,4]

Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Algorithm :
1. let max_profit =0
2. For each position , calculate the min_value till now 
            if min_value> price:
                min_value=price
            else:
                calculate: profit=price-min_value
3. max_profit = max(max_profit,profit)


TC: O(n)

SC : O(1)

"""

def stock(list1:list)->int:
    
    min=float("inf")
    ans=0

    for num in list1:
        if num <min:
            min=num
        profit=num-min
        ans=max(ans,profit)
    return ans


if __name__=="__main__":
    print(f"max profit = {stock(list1=[7,1,5,3,6,4])}")


