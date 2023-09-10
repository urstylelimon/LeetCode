class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        else:
            n = n-1
            list = [True] * (n + 1)
            list[0] = list[1] = False
            count = 0

            for i in range(2, int(n ** 0.5) + 1):
                if list[i]:
                    for j in range(i * i, n + 1, i):
                        list[j] = False

            for k in range(2, n + 1):
                if list[k]:
                    count += 1

            return count