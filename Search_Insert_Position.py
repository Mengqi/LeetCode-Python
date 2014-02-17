class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if len(A) == 0:
            return 0

        start = 0
        end = len(A) - 1
        while start < end:
            mid = (start + end) / 2
            if target <= A[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # only one left
        if target <= A[start]:
            return start
        else:
            return start+1

