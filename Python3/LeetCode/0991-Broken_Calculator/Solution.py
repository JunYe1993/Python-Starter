class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        # Method.1: X to Y (multiply and subtraction)
        # Method.2: Y to X (division and sum)
        # If do it with Method.1, it need to be like normal BFS.
        # You need to record some extra path beside the shortest one.
        # Scenario like 3->6->5->10, when X become 6, you can do either subtraction or multiply
        # But which is the shortest one you never know until one path X become Y. 
        # Before that you need to record both.
        # When you do it with Method.2. You would always do division when Y > X and Y % 2 == 0.

        step = 0
        while Y != X:
            if Y == X: return step
            elif Y < X: return step + X - Y
            elif Y > X: Y = Y+1 if Y%2 else Y//2
            step += 1
        return step