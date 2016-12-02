#task 14 - breadth first search 
class Graph():
    def __init__(self):
        self.adjlist={}

    def AddNode(self,value,connectedto):
        self.adjlist.update({value : connectedto})

    def AddEdge(self,value,othernode):
         self.adjlist[value].append(othernode)
         

    def BFS(self, start):
        route = []
        queue=[start]
        while queue:
            visited=queue.pop()
            if not visited in route:
                route=route+[visited]
                queue=queue+self.adjlist[visited]
        return route      

           
        

        
Graph = Graph()
Graph.AddNode(1,[2])
Graph.AddNode(4,[2,3,5])
Graph.AddNode(3,[3,4])
Graph.AddNode(2,[1,4])
Graph.AddNode(5,[4,5])
Graph.AddNode(6,[6,5])

print (Graph.adjlist)
print (Graph.BFS(4))
