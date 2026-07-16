class Solution:
    def relativeSortArray(self, arr1, arr2):
        # Step 1: Create rank map for arr2
        rank = {num: i for i, num in enumerate(arr2)}
        
        # Step 2: Sort arr1 using custom key
        arr1.sort(key=lambda x: (rank.get(x, float('inf')), x))
        
        return arr1
