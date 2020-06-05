try:
    from .graph import *
except:
    # Running file as __main__
    from graph import *

def depthFirstSearch(graph, startNode, endNode, visual=False, visited=None):
    """
    Search the graph until you find the endNode using depth first search.
    :param graph:     Graph object to be searched for a path
    :param startNode: Node object to start search at
    :param endNode:   Node object being searched for
    :param visual:    Set to true to output visual
    :param visited:   Set of visited node ids
    :return:          endNode object. If no path to endNode, None.
    """
    if visited is None: visited = set()

    if visual:
        print("Checking:", startNode)

    if startNode.id == endNode.id:
        return startNode

    visited.add(startNode.id)
    
    for neighbor in graph.neighbors(startNode.id):
        if neighbor.id not in visited:
            neighbor.prevNode = startNode
            newEndNode = depthFirstSearch(graph, neighbor, endNode, visual=visual, visited=visited)

            if newEndNode is not None and endNode.id == newEndNode.id:
                return newEndNode


def depthFirstSearchPath(graph, startNode, endNode, visual=False):
    """
    Get the first path found from a start to end node
    using depth first search.
    :param graph:     Graph object to be searched for a path
    :param startNode: Node object to start search at
    :param endNode:   Node object being searched for
    :param visual:    Set to true to output visual
    :return:          Path to the endNode. If no path, empty list.
    """
    # The return value endNode has the prevNode value.
    # The arg for this func may not have prevNode.
    endNode = depthFirstSearch(graph, startNode, endNode, visual=visual)
    return trace_path(startNode, endNode)



if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    a.adjacent = [c, b, e]
    b.adjacent = [a]
    c.adjacent = [a, e]
    e.adjacent = [c, a]
    g = Graph({a.id:a, b.id:b, c.id:c, d.id:d, e.id:e})
    
    print(depthFirstSearchPath(g, a, b, visual=True))
    # [a, b]
    print(depthFirstSearchPath(g, a, d, visual=True))
    # Empty list
    print(depthFirstSearchPath(g, a, e, visual=True))
    # [a, c, e] 
    # Although [a, e] is the shortest path, DFS gets this path
