class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        ways = [0] * (n+1)
        ways[0] = 1

        for i in range(n):
            ways[i+1] += ways[i]
            if i+2 <= n:
                ways[i+2] += ways[i]

        return ways[n]
