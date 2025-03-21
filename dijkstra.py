
def dijkstra(graph,start,goal):
    unvisited={n:float('inf') for n in graph.keys()}
    unvisited[start]=0
    visited={} # empty list to store nodes once their shortest distance is finalized .
    revPath={} # stores the predecessor of each node to reconstruct the shortest path .



    while unvisited:
        # minNode is the node in unvisited with the smallest tentative distance
        # comparing the nodes based on their distances 
        minNode=min(unvisited, key=unvisited.get) # unvisited.get fetches the current distance of each node.

        visited[minNode]=unvisited[minNode]

        #if we find the goal we should stop searching further 
        if minNode==goal:
            break

        for neighbor in graph.get(minNode):
            if neighbor in visited:
                continue

            #calculates a tentative distance to neighbor by adding :
            tempDist=unvisited[minNode]+graph[minNode][neighbor]


            # updates the tentative distance of neighbor if the new path is shorter 
            if tempDist < unvisited[neighbor]:
                unvisited[neighbor]=tempDist
                revPath[neighbor]=minNode
        
        # ensure minnode isnt processed again in the future 
        unvisited.pop(minNode)

    # reconstruct the shortest path : 
    node=goal
    revPathString=node
    while node!=start:
        revPathString+=revPath[node]
        node=revPath[node]

    # reverse the path to get the forward direction 
    fwdPath=revPathString[::-1]
    return fwdPath, visited[goal]


if __name__=='__main__':
    myGraph={
        'A':{'B':2, 'C':9, 'F':4},
        'B':{'C':6, 'E':3, 'F':2},
        'C':{'D':1},
        'D':{'C':2},
        'E':{'D':5,'C':2},
        'F':{'E':3}
    }

    startNode='A'
    goalNode='D'
    path,cost=dijkstra(myGraph,startNode,goalNode)
    print(f'The cost to reach from {startNode} to {goalNode} is {cost}.')
    print(f'The path is : {path}')


"""
Step-by-Step:

    Initialization:

        unvisited = {'A': 0, 'B': ∞, 'C': ∞, 'D': ∞, 'E': ∞, 'F': ∞}.

    Process A:

        Update neighbors B, C, F with distances 2, 9, 4.

        revPath: {'B': 'A', 'C': 'A', 'F': 'A'}.

    Process B (distance 2):

        Update C (via B: 2 + 6 = 8), E (2 + 3 = 5), F (2 + 2 = 4).

        revPath: {'C': 'B', 'E': 'B'}.

    Process F (distance 4):

        Update E (4 + 3 = 7, but E already has a shorter path via B).

    Process E (distance 5):

        Update D (5 + 5 = 10), C (5 + 2 = 7, shorter than 8).

        revPath: {'D': 'E', 'C': 'E'}.

    Process C (distance 7):

        Update D (7 + 1 = 8, shorter than 10).

        revPath: {'D': 'C'}.

    Process D (distance 8):

        D is the goal. Exit loop.

Result:

    Path: A -> B -> E -> C -> D (path string 'ABECD').

    Cost: 8.

"""