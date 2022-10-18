class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        i = 0
        while i < len(bank):
            if bank[i].count("1") == 0:
                bank.pop(i)
            else:
                i+=1
        
        count = 0
        for i in range(len(bank)-1):
            count += bank[i].count("1") * bank[i+1].count("1")
        return count