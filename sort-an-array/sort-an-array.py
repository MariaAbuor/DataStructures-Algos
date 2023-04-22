class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Function to merge two sub-arrays in sorted order.
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0 #i pointer-start of array; j - 0th index of left; k - 0th index of right

            #Merging
            while j < len(left) and k < len(right):#while j and k are in bounds
                if left[j] <= right[k]:#if the left value is less than or equal to the right, insert it into the array
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            #If there are elements left in either side, add them to the array    
            while j < len(left):
                nums[i] = left[j]
                i += 1
                j += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1
        #Function that takes in the array, left and right pointer to determine which portion of the sub-array we are running merge sort on
        def mergeSort(arr, l, r): 
            if l == r: #If the array has one element, the left pointer and the right pointer are equal
                return arr #Return the array
            m = (l + r) // 2 #mid pointer calculation
            mergeSort(arr, l, m)#Sort left side
            mergeSort(arr, m + 1, r)#Sort right side
            merge(arr, l, m, r)#Merge the array
            return arr

        return mergeSort(nums, 0, len(nums) - 1)    