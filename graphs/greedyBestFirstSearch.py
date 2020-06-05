try:
    from .graph import *
except:
    # Running file as __main__
    from graph import *

import heapq


def greedyBestFirstSearch(graph, startNode, endNode, heuristic, visual=False):
    """
    Search for a path from start to end using the greedy method.
    Graph must have nodes that can generate a heuristic value for distance.
    :param graph:     Graph object to be searched for a path
    :param startNode: Node object to start search at
    :param endNode:   Node object being searched for
    :param heuristic: Heuristic function to find distance to end node
                      Parameters: startNode, endNode
    :param visual:    Set to true to output visual
    :return:          endNode object. If no path to endNode, None.
    """
    pq = [] # Priority Queue
    visited = set()

    heapq.heappush(pq, startNode)

    while pq:
        current = heapq.heappop(pq)

        if current.id == endNode.id:
            return current
        
        for neighbor in graph.neighbors(current.id):
            if neighbor.id not in visited:
                if visual:
                    print("CurrentNode:", current, "Checking Neighbor:", neighbor)

                neighbor.prevNode = current
                visited.add(neighbor.id)
                priority = heuristic(neighbor, endNode)
                neighbor.priority = priority
                heapq.heappush(pq, neighbor)



def greedyBestFirstSearchPath(graph, startNode, endNode, heuristic, visual=False):
    """
    Get a path from start to end using the greedy method.
    Graph must have nodes that can generate a heuristic value for distance.
    :param graph:     Graph object to be searched for a path
    :param startNode: Node object to start search at
    :param endNode:   Node object being searched for
    :param heuristic: Heuristic function to find distance to end node
                      Parameters: startNode, endNode
    :param visual:    Set to true to output visual
    :return:          Path to the endNode. If no path, empty list.
    """
    # The return value endNode has the prevNode value, allowing 
    # us to trace backward.
    # The arg for this func may not have prevNode.
    endNode = greedyBestFirstSearch(graph, startNode, endNode, heuristic, visual=visual)
    return trace_path(startNode, endNode)



if __name__ == "__main__":
    g = GridGraph(10, 10)

    print(greedyBestFirstSearchPath(g, Node('0,0'), Node('-5,-5'), GridGraph.heuristic, visual=True))
    # Empty list
    print(greedyBestFirstSearchPath(g, Node('0,0'), Node('5,5'), GridGraph.heuristic, visual=True))
    print(greedyBestFirstSearchPath(g, Node('9,0'), Node('2,9'), GridGraph.heuristic, visual=True))