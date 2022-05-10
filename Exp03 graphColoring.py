class Graph:
    def __init__(self, edges, N):
       
        self.adj = [[] for _ in range(N)]
 
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)
 
def graphColor(graph):
 
    result = {}
 
    for u in range(N):
 
        assigned = set([result.get(i) for i in graph.adj[u] if i in result])
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1
 
        result[u] = color
 
    for v in range(N):
        print("Color assigned to vertex", v, "is", colors[result[v]])
 
colors = ["MAUVE","BLUE","GREEN","RED","YELLOW","ORANGE","PINK","BLACK","BROWN","WHITE",
          "PURPLE","VIOLET"]

N = int(input("Enter no of vertices: "))
edges = list(tuple(map(int,input().split())) for r in range(N))  
 
graph = Graph(edges, N)
graphColor(graph)
