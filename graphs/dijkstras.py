try:
    from .graph import *
except:
    # Running file as __main__
    from graph import *

import heapq

def dijkstras(graph, startNode, endNode, visual=False):
    """
    Search for a path using Dijksta's Algorithm.
    Graph must have nodes with a cost attribute.
    :param graph:     Graph object to be searched for a path
    :param startNode: Node object to start search at
    :param endNode:   Node object being searched for
    :param visual:    Set to true to output visual
    :return:          endNode object. If no path to endNode, None
    """
    pq = [] # Priority Queue
    visited = set()

    startNode.totalCost = startNode.cost
    heapq.heappush(pq, startNode)

    while pq:
        current = heapq.heappop(pq)

        if current.id == endNode.id:
            return current
        
        for neighbor in graph.neighbors(current.id):
            newTotalCost = current.totalCost + neighbor.cost
            
            if (neighbor.id not in visited or 
                (neighbor.totalCost is not None and newTotalCost < neighbor.totalCost)):
                if visual:
                    print("CurrentNode:", current, "Checking Neighbor:", neighbor)

                neighbor.prevNode = current
                visited.add(neighbor.id)
                neighbor.totalCost = newTotalCost
                heapq.heappush(pq, neighbor)


def dijkstrasPath(graph, startNode, endNode, visual=False):
    """
    Get a path from start to end using Dijkstra's Algorithm.
    Graph must have nodes with a cost attribute.
    :param graph:     Graph object to be searched for a path
    :param startNode: Node object to start search at
    :param endNode:   Node object being searched for
    :param visual:    Set to true to output visual
    :return:          Path to the endNode. If no path, empty list.
    """
    # The return value endNode has the prevNode value, allowing 
    # us to trace backward.
    # The arg for this func may not have prevNode.
    endNode = dijkstras(graph, startNode, endNode, visual=visual)
    return trace_path(startNode, endNode)



if __name__ == "__main__":
    g = GridGraph(10, 10)

    print(dijkstrasPath(g, Node('0,0'), Node('-5,-5'), visual=True))
    # Empty list
    print(dijkstrasPath(g, Node('0,0'), Node('5,5'), visual=True))
    print(dijkstrasPath(g, Node('9,0'), Node('2,9'), visual=True))