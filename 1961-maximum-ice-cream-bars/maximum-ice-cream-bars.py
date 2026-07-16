class Solution:
    def maxIceCream(self, costs, coins):
        # Step 1: Find max price
        max_cost = max(costs)
        
        # Step 2: Counting sort frequency array
        count = [0] * (max_cost + 1)
        for c in costs:
            count[c] += 1
        
        # Step 3: Buy bars starting from cheapest
        bars = 0
        for price in range(1, max_cost + 1):
            if count[price] > 0:
                # How many bars can we buy at this price?
                num = min(count[price], coins // price)
                bars += num
                coins -= num * price
                if coins == 0:
                    break
        
        return bars


# Example 1
print(Solution().maxIceCream([1,3,2,4,1], 7))   # Output: 4
# Example 2
print(Solution().maxIceCream([10,6,8,7,7,8], 5)) # Output: 0
# Example 3
print(Solution().maxIceCream([1,6,3,1,2,5], 20)) # Output: 6
