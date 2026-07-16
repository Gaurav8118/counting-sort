class Solution:
    def minMovesToSeat(self, seats, students):
        # Step 1: Sort both arrays
        seats.sort()
        students.sort()
        
        # Step 2: Pair each student with a seat
        moves = 0
        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])
        
        return moves


# Example 1
print(Solution().minMovesToSeat([3,1,5], [2,7,4]))   # Output: 4

# Example 2
print(Solution().minMovesToSeat([4,1,5,9], [1,3,2,6])) # Output: 7

# Example 3
print(Solution().minMovesToSeat([2,2,6,6], [1,3,2,6])) # Output: 4
