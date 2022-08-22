### Graph 

# 1      4______6_______7
# |      |
# 0______3_____5
#        |
#        2_____8 
#### Adjacent list Implementation 
# graph = [
#     [1,3],# neighbour of node 0 
#     [0],# neighbour of node 1
#     [3,8],# neighbour of node 2
#     [0,2,4,5],# neighbour of node 3
#     [3,6],# neighbour of node 4
#     [3],# neighbour of node 5
#     [4,7],# neighbour of node 6
#     [6],# neighbour of node 7
#     [2]# neighbour of node 8
# ]

#### Adjacent matrix Implementation 
#### 0 means no connection between nodes and 1 means connection
# graph2 = [
# #node:  0   1   2   3   4   5   6  7   8  node 
#        [0,  1,  0,  1,  0,  0,  0, 0,  0], # 0

#        [1,  0,  0,  0,  0,  0,  0, 0,  0], # 1

#        [0,  0,  0,  1,  0,  0,  0, 0,  1], # 2

#        [1,  0,  1,  0,  1,  1,  0, 0,  0], # 3

#        [0,  0,  0,  1,  0,  0,  1, 0,  0], # 4

#        [0,  0,  0,  1,  0,  0,  0, 0,  0], # 5

#        [0,  0,  0,  0,  1,  0,  0, 1,  0], # 6

#        [0,  0,  0,  0,  0,  0,  1, 0,  0], # 7

#        [0,  0,  1,  0,  0,  0,  0, 0,  0], # 8   
# ]

#### BFS traversal 
# def BFS(graph, starting_node):
#     q = [starting_node] ## node 0 
#     result = []
#     visited = {}
#     while len(q):
#         vertex = q.pop(0)
#         result.append(vertex)
#         visited[vertex] = True
#         for i in graph[vertex]:
#             if i not in visited.keys():
#                 q.append(i)
#     return result

# print(BFS(graph,4))

#### DFS traversal 
# def DFS(graph, vertex, result, visited):
#     if vertex in visited.keys():
#         return 
#     else:
#         result.append(vertex)
#         visited[vertex] = True
#         for i in graph[vertex]:
#             DFS(graph, i , result, visited)

# result = []
# DFS(graph, 5, result, {})
# print(result)

########################################################
########################################################
########################################################
# A compnay has n employees with unique IDs from 0 to n-1
# the head of the company has ID headID
# you will receive a managers arrays where managers[i] is the
# ID of the manager for employee i. Each employee has one 
# direct manager. the compnay head has no managers(managers[headID]= -1)
# it's guranteed the subordination relationships will have a tree structure.

# the head dof the compnay wants to inform their direct 
# subordinates who will inform his direct subordinates 
# who will inform their direct subordinates and so on until 
# everyone knows the news
# you will recieve an inform_time array where informTime[i]
# is the time it takes for employee i to inform all their direct 
# subordinates. return the total number f minutes it takes to 
# inform all employees of the new 

managers = [2,2,4,6,-1,4,4,5]
inform_time = [0,0,4,0,7,3,6,0]

### creating adjacent list with dict 
graph = {}
for i in range(len(managers)):
    if managers[i] not in graph.keys():
        graph[managers[i]] = [i]
    else:
        graph[managers[i]].append(i)

# Unsing BFS lvl order traversal 
head = graph[-1]
q = []
q.extend(head)
time = 0 
while len(q):
    curr_time = 0 
    l = len(q)
    count = 0 
    while count < l :
        vertex = q.pop(0)
        curr_time = max(curr_time, inform_time[vertex])
        if vertex in graph.keys():
            q.extend(graph[vertex])
        count += 1
    time += curr_time


print(time)


