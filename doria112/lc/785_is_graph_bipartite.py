class UnionFind:
    def __init__(self, graph: List[List[int]]):
        self.nodes = collections.defaultdict()
        for i, node_list in enumerate(graph):
            if i not in self.nodes:
                self.nodes[i] = i
            #print(node_list)
            for n in node_list:
                self.nodes[n] = n

    
    def find(self, node):
        if self.nodes[node] == node:
            return node
        else:
            parent = self.find(self.nodes[node])
            self.nodes[node] = parent
            return self.nodes[node]
    
    def union(self, node1, node2):
        self.nodes[node1] = self.find(node2)
    
    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf = UnionFind(graph)
        for node_list in graph:
            if len(node_list) == 0:
                continue
            n1 = node_list[0]
            for n2 in node_list[1:]:
                uf.union(n1, n2)
                n1 = n2
        
        for n1, node_list in enumerate(graph):
            for n2 in node_list:
                if uf.find(n1) == uf.find(n2):
                    return False
        return True
