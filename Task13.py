class Graph():
    def __init__(self):
        self.adjlist={}

    def AddNode(self,value,connectedto):
        self.adjlist.update({value : connectedto})

    def AddEdge(self,value,othernode):
         self.adjlist[value].append(othernode)



Graph = Graph()
Graph.AddNode(1,[2])
Graph.AddNode(2,[3,4])
Graph.AddNode(3,[1,4])
Graph.AddNode(4,[1,2,4])
Graph.AddNode(5,[5,4])

print (Graph)

