class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        single = 0
        for num in A:
            single ^= num

        return single
