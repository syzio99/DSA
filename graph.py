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