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
visited = set()
 
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
 
dfs(visited, graph, '8')
