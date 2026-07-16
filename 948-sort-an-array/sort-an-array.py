class Solution:
    def sortArray(self, nums):
        # Merge Sort implementation
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)
        
        def merge(left, right):
            merged = []
            i = j = 0
            
            # Merge two sorted halves
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            # Add remaining elements
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return merged
        
        return merge_sort(nums)


# Example 1
print(Solution().sortArray([5,2,3,1]))   # Output: [1,2,3,5]

# Example 2
print(Solution().sortArray([5,1,1,2,0,0])) # Output: [0,0,1,1,2,5]
