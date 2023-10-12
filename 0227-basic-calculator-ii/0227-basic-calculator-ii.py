class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s += '+'
        indx = []
        result = 0
        op = '+'

        for i in s:
            if i.isdigit():
                result = (result * 10) + int(i)
            else:
                result = int(result)
                if op == '+':
                    indx.append(result)
                elif op == '-':
                    indx.append(-result)
                elif op == '*':
                    indx.append(indx.pop() * result)
                elif op == '/':
                    indx.append(int(indx.pop() / result))
                result = 0
                op = i
        return (sum(indx))