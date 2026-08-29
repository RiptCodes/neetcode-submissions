class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_scores = []
        #Firstly I want to define the operations
        for ops in operations:
            if ops == "+":
                addition = new_scores[-1] + new_scores[-2]
                new_scores.append(addition)
            elif ops == "D":
                new_scores.append(2*new_scores[-1])
            elif ops == "C":
                new_scores.pop()
            else:
                new_scores.append(int(ops))

        total = 0
        for i in new_scores:
            total += i
        return total