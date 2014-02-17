class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 0:
            return 0

        numList = [0] * (n + 1)
        numList[0] = 1

        for tree_size in range(1, n+1):
            for left_size in range(tree_size):
                right_size = tree_size - 1 - left_size
                numList[tree_size] += numList[left_size] * numList[right_size]

        return numList[n]
