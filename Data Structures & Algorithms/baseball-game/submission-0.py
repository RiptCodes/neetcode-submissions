class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_scores = []
        x = 0
        #Firstly I want to define the operations
        for i in range(len(operations)):
            x = operations[i]
            if x == "+":
                addition = new_scores[-1] + new_scores[-2]
                new_scores.append(addition)
            elif x == "D":
                new_scores.append(2*new_scores[-1])
            elif x == "C":
                new_scores.pop()
            else:
                x = int(x)
                new_scores.append(x)

        total = 0
        for i in new_scores:
            total += i
        return total