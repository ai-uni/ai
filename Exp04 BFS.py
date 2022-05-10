graph = {
    '1' : ['2','3','10'],
  '2' : ['7','8'],
  '7' : [],
  '8' : ['11','12' ],
  '3' : ['5','6'],
  '5' : [],
  '6' :[],
  '10':[],
  '11':[],
  '12':[]

}
 
visited = [] # Keep track of visited nodes.
queue = []   # Queue
 
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0) 
        print (s), 
        for neighbour in graph[s]:
              if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
 
# Driver Code
bfs(visited, graph, '1')
