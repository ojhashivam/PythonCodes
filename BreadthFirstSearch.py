graph={
    '1':['8','5','2'],
    '8':['6','4','3'],
    '6':['10','7'],
    '2':['9'],
    '10':[],
    '7':[],
    '5':[],
    '9':[],
    '4':[],
    '3':[]
}

visited=[]
queue=[]

def bfs(start,graph,visited):
    visited.append(start)
    queue.append(start)

    while queue:
        m=queue.pop(0)
        print('-',m,end='')

        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
print("The BFS For The Given Graph Is:")
bfs('1',graph,visited)