class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        currPos = 0
        nextPos = 1

        while nextPos < len(A):
            while nextPos < len(A) and A[currPos] == A[nextPos]:
                nextPos += 1
                length -= 1
            if nextPos != currPos+1 and nextPos < len(A):
                A[currPos+1] = A[nextPos]
            currPos += 1
            nextPos += 1

        return length
