try:
    from .board import *
except:
    # Running file as __main__
    from board import *

import heapq

def astar(graph, startNode, endNode, heuristic, visual=False):
    """
    Search for a path using A* Algorithm.
    Graph must have nodes with a cost attribute.
    :param graph:     Graph object to be searched for a path
    :param startNode: Node object to start search at
    :param endNode:   Node object being searched for
    :param heuristic: Heuristic function to find distance to end node
                      Parameters: startNode, endNode
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
                neighbor.priority = newTotalCost + heuristic(neighbor, endNode)
                heapq.heappush(pq, neighbor)


def astarPath(graph, startNode, endNode, heuristic, visual=False):
    """
    Search for a path using A* Algorithm.
    Graph must have nodes with a cost attribute.
    :param graph:     Graph object to be searched for a path
    :param startNode: Node object to start search at
    :param endNode:   Node object being searched for
    :param heuristic: Heuristic function to find distance to end node
                      Parameters: startNode, endNode
    :param visual:    Set to true to output visual
    :return:          endNode object. If no path to endNode, None
    """
    # The return value endNode has the prevNode value, allowing 
    # us to trace backward.
    # The arg for this func may not have prevNode.
    endNode = astar(graph, startNode, endNode, heuristic, visual=visual)
    return trace_path(startNode, endNode)


if __name__ == "__main__":
    g = GridGraph(10, 10)
    print("Starting at 0,0, looking for -5,-5")
    print(astarPath(g, g['0,0'], Node('-5,-5'), GridGraph.heuristic, visual=True))
    # Empty list

    b = Board() # Random board
    print(f"Starting at {b.start}, looking for {b.end}")
    print(astarPath(b, b[b.start], b[b.end], GridGraph.heuristic, visual=True))