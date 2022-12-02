class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        
        labels = {x:x for x in range(n)}
        unique = n
        # path compression 
        def find_label(a):
            if labels[a] != a:
                labels[a] = find_label(labels[a])
            return labels[a]
        
        for log in logs:
            print(labels)
            l1 = find_label(log[1])
            l2 = find_label(log[2])
            # when acquaint happens, two sets combined, number of unique labels reduce by 1
            # can optimize by union by rank
            if l1 != l2:
                labels[l1] = l2
                unique -= 1
            if unique == 1:
                return log[0]

        return -1
