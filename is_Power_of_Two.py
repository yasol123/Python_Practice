class Solution:
    """
    input: n = 16
    2^4 = 16
    Output: True

    input: n = 1024
    2^10 = 11024
    Output: True

    input: n=5
    2^2 = 4, 2^3 = 8
    Output: False
    """
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n%2 != 0 or n == 0:
            return False
        return self.isPowerOfTwo(n/2)
