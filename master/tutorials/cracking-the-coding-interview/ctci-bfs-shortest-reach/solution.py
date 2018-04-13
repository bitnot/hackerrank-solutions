infinity =  1000000
weight = 6

class Node(object):
    __slots__= ('number','dist','nodes','visited','queued')
    
    def __init__(self, number):
        self.number = number
        self.dist = infinity
        self.nodes = []
        self.visited = False
        self.queued = False
        
    def connect(self, node):
        self.nodes.append(node) 
        node.nodes.append(self) 
        

q = int(input().strip());
for q0 in range(0,q):
    #load
    nrNodes,nrEdges = [int(i) for i in input().strip().split(' ')]
    nodes = {};
    for nodeNr in range(0, nrNodes):
        nodes[nodeNr] = Node(nodeNr+1)
    for edgeNr in range(0,nrEdges):
        x,y = [int(i)-1 for i in input().strip().split(' ')]
        nodes[x].connect(nodes[y]) 
    startNr = int(input().strip()) - 1

    #traverse
    queue = []
    nodes[startNr].dist = 0
    nodes[startNr].queued = True
    queue.append(nodes[startNr])
   
    while len(queue) > 0:
        current = queue.pop(0)    
        current.visited = True
        newDist = current.dist + weight
        for neighbour in current.nodes:
            if neighbour.dist > newDist:
                neighbour.dist = newDist
            if not (neighbour.visited or neighbour.queued):
                neighbour.queued = True
                queue.append(neighbour)
    
    distances = []
    for i in range(0, len(nodes)):
        if i != startNr:
            dist = nodes[i].dist
            distances.append(dist if dist != infinity else -1)
    print(" ".join([str(d) for d in distances]))