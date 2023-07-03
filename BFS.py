graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
    }
visited=[]
queue=[]
path=[]

def bfs(visited,graph,node,target):
    visited.append(node)
    queue.append(node)
    

    while queue:
        m=queue.pop(0)
        node=m[-1]
        print(m,end=" ")
        if target == m:
            print("true")
        
             
       
        

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        if node<target:
            print(node)
print("following is the breadth-first search")
bfs(visited,graph,'5','4')


                
