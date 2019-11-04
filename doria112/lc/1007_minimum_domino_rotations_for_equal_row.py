class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        moves = {}
        for i, a in enumerate(A):
            b = B[i]
            new_moves = {}
            if i > 0:
                if a == b and a in moves:
                    new_moves[a] = moves[a]
                else:
                    if a in moves:
                        new_moves[a] = [moves[a][0], moves[a][1]+1]
                    if b in moves:
                        new_moves[b] = [moves[b][0]+1, moves[b][1]]
                moves = new_moves
            else:
                if a == b:
                    moves[a] = [0,0]
                else:
                    moves[a] = [0,1]
                    moves[b] = [1,0]
        smallest = -1
        for k,v in moves.items():
            if smallest == -1:
                smallest = min(v[0], v[1])
            else:
                smallest = min(smallest, v[0], v[1])
        return smallest

# special case: upper and lower are the same number, no need to rotate
