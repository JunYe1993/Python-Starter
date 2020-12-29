from typing import List

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        area = 0
        area += (C-A) * (D-B)
        area += (G-E) * (H-F)
        
        overlaparea = 0
        x1, x2 = max(A, E), min(C, G)
        y1, y2 = max(B, F), min(D, H)
        xlength = x2 - x1
        ylength = y2 - y1
        
        if xlength > 0 and ylength > 0:
            overlaparea = xlength * ylength

        return area - overlaparea

    def computeAreaHouzz(self, rec1, rec2, rec3):
        print()
        area = 0
        minX = min(rec1[0], rec2[0], rec3[0])
        maxX = max(rec1[2], rec2[2], rec3[2])
        
        minY, maxY = None, None
        for x in range(minX+1, maxX):
            
            minY, maxY = None, None
            if rec1[0] <= x <= rec1[2]:
                minY = rec1[1]
                maxY = rec1[3]
            if rec2[0] <= x <= rec2[2]:
                minY = rec2[1] if minY == None else min(minY, rec2[1])
                maxY = rec2[3] if maxY == None else max(maxY, rec2[3])
            if rec3[0] <= x <= rec3[2]:
                minY = rec3[1] if minY == None else min(minY, rec3[1])
                maxY = rec3[3] if maxY == None else max(maxY, rec3[3])
            
            pre_minY, pre_maxY = None, None
            if rec1[0] <= x-1 <= rec1[2]:
                pre_minY = rec1[1]
                pre_maxY = rec1[3]
            if rec2[0] <= x-1 <= rec2[2]:
                pre_minY = rec2[1] if pre_minY == None else min(pre_minY, rec2[1])
                pre_maxY = rec2[3] if pre_maxY == None else max(pre_maxY, rec2[3])
            if rec3[0] <= x-1 <= rec3[2]:
                pre_minY = rec3[1] if pre_minY == None else min(pre_minY, rec3[1])
                pre_maxY = rec3[3] if pre_maxY == None else max(pre_maxY, rec3[3])
            
            area += min(maxY - minY, pre_maxY - pre_minY)
        area += maxY - minY
        return area