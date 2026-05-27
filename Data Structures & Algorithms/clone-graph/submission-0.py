"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}

        if node is None:
            return None

        def dfs(node):
            '''clone all nodes and neighbors with recurisive calls''' 
            # pass in every node we visit 
            if node in oldToNew: # did we already clone it? 
                return oldToNew[node] # return clone 
            copy = Node(node.val)
            oldToNew[node] = copy 
            for nei in node.neighbors:
                # run dfs on that neighbor
                copy.neighbors.append(dfs(nei))
                # will return that copy 
            return copy 

        return dfs(node) # will give us the undirected graph