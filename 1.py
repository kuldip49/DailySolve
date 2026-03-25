class Solution:
    def subtractProductAndSum(n):
        sum = 0
        mul = 1
        for i in str(n):
            sum += int(i)
            mul *= int(i)
        return (mul - sum)
print(Solution.subtractProductAndSum(234))