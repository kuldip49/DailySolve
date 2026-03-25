#1672

class Solution:
    def maximumWealth(accounts: list[list[int]]):
        wealth = 0
        for i in range(len(accounts)):
            print(accounts[i])
            add = 0
            for j in accounts[i]:
               add+=j
            if add > wealth:
                wealth = add
        return wealth

print(Solution.maximumWealth([[1,2,3],[3,2,1]]))


