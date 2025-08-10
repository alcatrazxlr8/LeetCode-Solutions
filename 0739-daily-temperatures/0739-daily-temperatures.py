class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temps)

        for i in range(len(temps)):

            while stack and temps[i] > stack[-1][0]:
                    t, idx = stack.pop()
                    ans[idx] = i-idx
            stack.append((temps[i], i))

        return ans
            