class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        curr = m + n - 1
        aPos = m - 1
        bPos = n - 1

        while aPos >= 0 and bPos >= 0:
            if A[aPos] > B[bPos]:
                A[curr] = A[aPos]
                aPos -= 1
            else:
                A[curr] = B[bPos]
                bPos -= 1
            curr -= 1

        while aPos >= 0:
            A[curr] = A[aPos]
            aPos -= 1
            curr -= 1

        while bPos >= 0:
            A[curr] = B[bPos]
            bPos -= 1
            curr -= 1

