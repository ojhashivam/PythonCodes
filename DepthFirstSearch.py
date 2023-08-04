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

def dfs(start,graph,visited):
    visited.append(start)
    queue.append(start)

    while queue:
        m=queue.pop(len(queue)-1)
        print('-',m,end='')

        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
print("The DFS For The Given Graph Is:")
dfs('1',graph,visited)