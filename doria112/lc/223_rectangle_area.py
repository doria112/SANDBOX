class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        union = (C-A)*(D-B) + (G-E)*(H-F)
        # coordinates of intersection
        o1 = max(A, E) # rigth most of A and E
        o2 = max(B, F) # up most of B and F
        o3 = min(C, G) # left most of C and G
        o4 = min(D, H) # down most of D and H
        if (o3 <= o1) or (o4 <= o2): #necessary, in case both negative will lead to postive intersection area
            intersection = 0
        else:
            intersection = (o3 - o1) * (o4 - o2)
        return union - intersection
