class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        ops = {"+","-","*","/"}
        for i in range(0,len(tokens)):
            if tokens[i] == "*":
                numbers[-2] = numbers[-2] * numbers[-1]
                numbers.pop()
            elif tokens[i] == "/":
                numbers[-2]= int(numbers[-2]/numbers[-1])
                numbers.pop()
            elif tokens[i] == "+":
                numbers[-2] = numbers[-2] + numbers[-1]
                numbers.pop()
            elif tokens[i] == "-":
                numbers[-2] = numbers[-2] - numbers[-1]
                numbers.pop()
            else:
                numbers.append(int(tokens[i]))
        return numbers[0]