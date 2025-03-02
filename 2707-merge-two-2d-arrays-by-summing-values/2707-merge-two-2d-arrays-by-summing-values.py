class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        a = 0
        b = 0
        ans = []
        while a < len(nums1) and b < len(nums2):
            if  nums1[a][0] == nums2[b][0]:
                tmp = nums1[a][1] + nums2[b][1]
                ans.append([nums1[a][0], tmp])
                a += 1
                b += 1
            elif nums1[a][0] < nums2[b][0]:
                ans.append(nums1[a])
                a += 1
            else:
                ans.append(nums2[b])
                b += 1
        while a < len(nums1):
            ans.append(nums1[a])
            a += 1
        while b < len(nums2):
            ans.append(nums2[b])
            b += 1
        
        return ans