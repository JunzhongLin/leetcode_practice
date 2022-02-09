'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if node == []:
            return [[]]

        if not node:
            return node

        node_dict = {}

        def _get_node(old_node, node_dict=node_dict):
            if old_node in node_dict:
                return node_dict[old_node]
            else:
                node_dict[old_node] = Node(val=old_node.val)
                return node_dict[old_node]

        stack = [node]

        while stack:
            old_node = stack.pop()
            new_node = _get_node(old_node)
            for old_neighbor in old_node.neighbors:
                if _get_node(old_neighbor) not in new_node.neighbors:
                    new_node.neighbors.append(_get_node(old_neighbor))
                if _get_node(old_neighbor).neighbors == []:
                    stack.append(old_neighbor)

        return node_dict[node]