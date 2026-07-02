"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cpyHead = Node(node.val)
        visited = {node: cpyHead}
        toVisit = [node]

        while toVisit:
            og = toVisit.pop()
            cpy = visited[og]

            for neighbor in og.neighbors:
                if neighbor in visited:
                    cpy.neighbors.append(visited[neighbor])
                else:
                    temp = Node(neighbor.val)
                    visited[neighbor] = temp
                    cpy.neighbors.append(temp)
                    toVisit.append(neighbor)
        return cpyHead


        