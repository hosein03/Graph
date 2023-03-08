# Graph
firstly the class Graph is made,
and then in the __init__ function a list named 'edges' for our edges and a dictionary named 'coloring' for the colors of vertices are made

in the MakeEmpty function we take a variable name (G) and make it a list for our vertices.

in the InsertVertex function, we take a variable which is a vertex and add it to the list.

in the InsertEdge function we will add the 2 variable as a tuple to our list representing the edges.
that is if both are already a vertex.

in the NumVertices will give out the number of vertices.

in the NumEdges we will see how many edges we have.

the ListOfVertices function will print out all of the vertices

the AdjacentVertices will take a variable, will check if it's a vertex and if so, will show you a list of vertexes that are adjucent to it.

the ColorVertex will take a variable, will check if it's a vertex and if so, will ask what color you want it to be,
and then adds it to the dictionary of color.

in the IsColored function it will check if a vertex is colored and if it is it will say what color.

the IsAdjucent functin will see if a vertex is adjucent to another.
