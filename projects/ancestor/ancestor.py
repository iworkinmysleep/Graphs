"""
Understand
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
-given input 6, should return 10
-given input 7, should return 4
-given input 11, should return -1

Plan
-vertices = people represented by IDs
-edges = path from parent to child

-dfs to return earliest ancestor
"""

from collections import deque


def earliest_ancestor(ancestors, starting_node):
    # create a graph with IDs as vertices and edges represented as paths from parent to child
    ancestor_graph = {}
    for edge in ancestors:
        parent, child = edge[0], edge[1]
        if child not in ancestor_graph:
            ancestor_graph[child] = set()
        ancestor_graph[child].add(parent)

    earliest_known_ancestor = -1

    q = deque()
    q.append(starting_node)
    while len(q) > 0:
        curr = q.popleft()
        if curr in ancestor_graph:
            lowest_ID = None
            for parent in ancestor_graph[curr]:
                if lowest_ID is None:
                    lowest_ID = parent
                elif parent < lowest_ID:
                    lowest_ID = parent
                q.append(parent)
            if lowest_ID is not None:
                earliest_known_ancestor = lowest_ID

    return earliest_known_ancestor
