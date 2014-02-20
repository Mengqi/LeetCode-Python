class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max = A[-1]
        sum = 0
        for i in reversed(range(len(A))):
            if sum >= 0:
                sum += A[i]
            else:
                sum = A[i]

            if sum > max:
                max = sum

        return max
