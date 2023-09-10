class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        else:
            def check_prime(num):
                list = [True] * (num + 1)
                list[0] = list[1] = False
                count = 0

                for i in range(2, int(num**0.5) + 1):
                    if list[i]:
                        for j in range(i * i, num + 1, i):
                            list[j] = False

                for k in range(2, num + 1):
                    if list[k]:
                        count += 1

                return count

            count = check_prime(n-1)
            return count