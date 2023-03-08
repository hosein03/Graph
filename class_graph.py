class Graph:
    def __init__(self, G):
        self.G = G
        self.edges = list() # this is the list, that will contain our edges in tuples.
        self.coloring = {}

    def MakeEmpty(self, G):
        self.G = [] #G is the list of Vertices.

    def InsertVertex(self, G , v):
        self.G.append(v)
    
    def InsertEdge(self, G, u, v):
        if u and v in self.G:
            self.edges.append((u, v))
        elif u or v not in self.G:
            print(str(u), + " or " + str(v) + " are not a vertex of our graph.")

    def NumVertices(self, G):
        Ver = "the number of vertices are: "
        print(Ver + str(len(self.G)))

    def NumEdges(self, G):
        Edg = "the number of edges are: "
        print(Edg + str(len(self.edges)))

    def ListOfVertices(self, G):
        print("our vertices are: ")
        for i in self.G:
            print(i)

    def AdjacentVertices(self, G, v):
        text = []
        if v in self.G:
            for i in self.edges:
                if i[0] == v:
                    text.append(i[1])
        
            print("the adjucent vertices of " + str(v) + " are: ")
            for a in text:
                print(a)
        
        elif v not in self.G:
            print(str(v) + " is not a vertex of " + G)

    def ColorVertex(self, G, v):
        if v in self.G:
            color = input("what color do you want your vertex to be? ")
            self.coloring[v] = color
        elif v not in self.G:
            print(str(v) + " is not a vertex of our graph.")

    def IsColored(self, G, v):
        if v in self.G:
            for i in self.coloring.keys():
                if i == v:
                    print(str(v) + " is color is " + str(self.coloring[v]))
        elif v not in self.G:
            print(str(v) + " is not a vertex of our graph.")

    def IsAdjucent(self, G, u, v):
        flag = False
        for i in self.edges:
            if ((i[0] == v and i[1] == u) or (i[0] == u and i[1] == v)):
                flag = True
        
        if flag == True:
            print(str(u) + " is adjucent to " + str(v))
        elif flag == False:
            print(str(u) + " is not adjucent to " + str(v))
