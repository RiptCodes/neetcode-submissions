class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialising a stack for the results array
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j

            stack.append(i)

            
        return result
            
        