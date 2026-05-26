class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuples = sorted(zip(position,speed))
        tuples = zip(*tuples)
        position, speed = [list(t) for t in tuples]
        for i in range(len(position)):
            position[i] = (target - position[i])/speed[i]
        stack = []
        for pos in position:
            while stack and stack[-1]<=pos:
                stack.pop()
            stack.append(pos)
        return len(stack)