"""
Input: 10
2^10 = 1024
Output:1024
"""
def powerOfTwo(n):
    if n==0:
        return 1
    else:
        power = powerOfTwo(n-1)
        print(power)
        return power * 2
print(powerOfTwo(10))
