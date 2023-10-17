class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        import math
        
        A1 = math.sqrt( (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1])**2 )
        A2 = math.sqrt( (p4[0] - p1[0]) ** 2 + (p4[1] - p1[1])**2 )
        A3 = math.sqrt( (p3[0] - p1[0]) ** 2 + (p3[1] - p1[1])**2 )

        B1 = math.sqrt( (p3[0] - p2[0]) ** 2 + (p3[1] - p2[1])**2 )
        B2 = math.sqrt( (p4[0] - p2[0]) ** 2 + (p4[1] - p2[1])**2 )

        C1 = math.sqrt( (p4[0] - p3[0]) ** 2 + (p4[1] - p3[1])**2 )

        list1 = [A1,A2,A3,B1,B2,C1]
        max_value = max(list1)
        max_value_list = []
        count = 0
        for i in list1:
            if i == max_value:
                count += 1
                max_value_list.append(i)
                list1.remove(i)

        if len(max_value_list) != 2:
            return False
        else:
            
            if list1[0] == list1[1] == list1[2] == list1[2] and max_value_list[0] == max_value_list[1]:
                return True
            else:
                return False
