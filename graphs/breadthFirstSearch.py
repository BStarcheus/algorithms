try:
    from .graph import *
except:
    # Running file as __main__
    from graph import *

def breadthFirstSearch(graph, startNode, endNode, visual=False):
    """
    Search the graph until you find the endNode using breadth first search.
    :param graph:     Graph object to be searched for a path
    :param startNode: Node object to start search at
    :param endNode:   Node object being searched for
    :param visual:    Set to true to output visual
    :return:          endNode object. If no path to endNode, None.
    """
    visited = set() # Set of node ids
    queue = []   # Queue of nodes

    queue.append(startNode)
    visited.add(startNode.id)

    while queue:
        current = queue.pop(0)

        if current.id == endNode.id:
            return current

        for neighbor in graph.neighbors(current.id):
            if neighbor.id not in visited:
                if visual:
                    print("CurrentNode:", current, "Checking Neighbor:", neighbor)

                neighbor.prevNode = current
                visited.add(neighbor.id)
                queue.append(neighbor)


def breadthFirstSearchPath(graph, startNode, endNode, visual=False):
    """
    Returns the first path found from a start to end node
    using breadth first search.
    :param graph:     Graph object to be searched for a path
    :param startNode: Node object to start search at
    :param endNode:   Node object being searched for
    :param visual:    Set to true to output visual
    :return:          Path to the endNode. If no path, empty list.
    """
    # The return value endNode has the prevNode value.
    # The arg for this func may not have prevNode.
    endNode = breadthFirstSearch(graph, startNode, endNode, visual=visual)
    return trace_path(startNode, endNode)




if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    a.adjacent = [c, b, e]
    b.adjacent = [a, c]
    c.adjacent = [a, b, e]
    e.adjacent = [c, a]
    g = Graph({a.id:a, b.id:b, c.id:c, d.id:d, e.id:e})

    print(breadthFirstSearchPath(g, a, b, visual=True))
    # [a, b]
    print(breadthFirstSearchPath(g, a, d, visual=True))
    # Empty list
    print(breadthFirstSearchPath(g, b, e, visual=True))
    # [b, a, e]