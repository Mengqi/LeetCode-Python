class Solution:
    # @return an integer
    def reverse(self, x):
        num = abs(x)
        rev = 0

        while num != 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10

        if x < 0:
            rev = -rev

        return rev
