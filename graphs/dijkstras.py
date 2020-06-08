try:
    from .board import *
except:
    # Running file as __main__
    from board import *

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

    startNode.totalCost = startNode.cost
    heapq.heappush(pq, startNode)

    while pq:
        current = heapq.heappop(pq)

        if visual:
            print("Checking Node:", current)   

        if current.id == endNode.id:
            return current
        
        for neighbor in graph.neighbors(current.id):
            newTotalCost = current.totalCost + neighbor.cost
            
            if newTotalCost < neighbor.totalCost:
                neighbor.prevNode = current
                neighbor.totalCost = newTotalCost
                # Priority is used for comparison in heapq
                neighbor.priority = newTotalCost
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
    print(dijkstrasPath(g, g['0,0'], Node('-5,-5'), visual=True))
    # Empty list

    b = Board() # Random board
    print(dijkstrasPath(b, b[b.start], b[b.end], visual=True))