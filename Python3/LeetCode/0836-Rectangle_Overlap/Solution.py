from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # rectangle index 0 and 2 mean x coordinate
        # 0 => button-left
        # 2 => top-right
        # R1_0   R2_0   R1_2   R2_2 
        # R1_X---R2_X---R1_X---R2_X
        # So R1_2 must bigger than R2_0 if there is overlap
        # But question didn't insure rec2 is R2 and rec1 is R1 in this situation.
        # So use min max to
        x = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        y = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        return x and y