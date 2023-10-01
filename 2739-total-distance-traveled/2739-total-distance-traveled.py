class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        count = 0
        distance = 0
        i = 1
        while i <= mainTank:
            distance += 10
            count += 1
            if count == 5:
                if additionalTank != 0:
                    mainTank += 1
                    additionalTank -= 1
                count = 0
            i += 1

        return distance
        