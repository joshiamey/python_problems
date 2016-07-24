class Vertex:
    def __init__(self,key):
        self.id = key
        self.adjacencyList = {}

    def addNeighbour(self,other_vertex,weight=0):
        self.adjacencyList[other_vertex]  = weight

    def getAdjacencyList(self):
        return self.adjacencyList.keys()

    def getId(self):
        return self.id

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.adjacencyList])

    def getWeight(self,other_vertex):
        return self.adjacencyList[other_vertex]

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numEdges = 0
        self.numVertices = 0
        

    def addVertex(self,key):
        nv = Vertex(key)
        self.numVertices += 1
        self.vertices[key] = nv

    def addEdge(self,f,to,weight=0):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if to not in self.vertices:
            nv = self.addVertex(to)
        
        self.vertices[f].addNeighbour(t,weight)
        self.numEdges += 1

    def V(self):
        return self.numVertices

    def E(self):
        return self.numEdges

    def __contains__(self,key):
        return key in self.vertices

    def vertex(self,key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            print('Vertex not present')
            return None

    def vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())