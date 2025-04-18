class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # ## set
        # s = set()

        # for num in nums:
        #     if num in s:
        #         return True
        #     s.add(num)
        # return False

        ## map
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
                return True
            dic[num] = 1
        return False