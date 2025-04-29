class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for p,s in pairs:
            time = (target - p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
                
        fleets = len(stack)

        return fleets
