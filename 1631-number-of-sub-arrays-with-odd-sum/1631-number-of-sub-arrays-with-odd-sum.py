class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        # # Prefix Sum and odd, even prefix counts
        currSum = oddCnt = evenCnt = count = 0
        MOD = 10**9 + 7
        
        for num in arr:
            currSum += num
            if currSum % 2: #odd
                count = (count + 1 + evenCnt) % MOD
                oddCnt += 1
            else: #even
                count = (count + oddCnt) % MOD
                evenCnt += 1
        return count

        # # Brute Force : (O(n^2)) : TLE
        # count = 0
        # for i in range(len(arr)):
        #     for j in range(i, len(arr)):
        #         if sum(arr[i:j+1]) % 2 == 1:
        #             # print(i, j, count)
        #             count +=1 
        #             # print(f"i: {i} ; j: {j} ; arr[i:j]: {arr[i:j+1]} ; sum: {sum(arr[i:j+1]) % 2 == 1}")
        # return count
