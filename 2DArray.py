from lib2to3.pgen2.token import MINUS
from tkinter import HORIZONTAL


Array = [
[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15]
]
# print(Array)

##########################################################
##########################################################
#### BFS ALgorithm 
# def BFS(arr):
#     h = len(arr) 
#     w = len(arr[0]) 

#     q = [[0,0]]
#     output = []

#     while len(q):
#         r, c = q.pop(0)
#         output.append(arr[r][c])

#         if r < h and c +1 < w:
#             if [r,c+1] not in q:
#                 q.append([r,c+1])
        
#         if r+1 < h and c  < w:
#             if [r+1,c] not in q:
#                 q.append([r+1,c])                
#     print(output)
# BFS(Array)

##########################################################
##########################################################
##### DFS ALgorithm 
# def DFS(arr):
#     output = []
#     row = len(arr)
#     col = len(arr[0])

#     dRow = [0,1,0,-1] ## Directions
#     dCol = [-1,0,1,0]

#     visted = [[False for i in range(col)] for j in range(row)] ### Empty array to track visited nodes

#     stack = [[0,0]]

#     while len(stack) > 0 :
#         curr_r, curr_c = stack.pop() # last element 
  
#         if curr_r < 0 or curr_c <0 or curr_r >= row or curr_c >= col:
#             continue
#         elif visted[curr_r][curr_c] :
#             continue

#         visted[curr_r][curr_c] = True

#         output.append(arr[curr_r][curr_c])

#         for i in range(4):
#             next_row = curr_r + dRow[i]
#             next_col = curr_c + dCol[i]
#             stack.append([next_row,next_col])

#     print(output)

# DFS(Array)
# DFS([[-1,2,3],[0,9,8],[1,0,1]])
    

##########################################################
##########################################################
# Given a 2D Array containing onlys 1's(land) and o's(water)
# count the number of islands.
# An island is land connected horizontally or vertically 


# arr = [
# [1,1,1,1,0],
# [1,1,0,1,0],
# [1,1,0,0,1],
# [0,0,0,1,1]
# ]

# rl = len(arr)
# cl = len(arr[0])
# count = 0 

# for i in range(rl):
#     for j in range(cl):
#         if arr[i][j] == 1:
#             count += 1
#         #### BFS Algo ####
#             q = [[i,j]]
#             while len(q) > 0:
#                 r, c = q.pop(0)
#                 if arr[r][c] != 0:
#                     arr[r][c] = 0  

#                     if r < rl and c +1 < cl: ### right side of curr node
#                         if arr[r][c+1] == 1:
#                             q.append([r,c+1])
                    
#                     if r < rl and c - 1 > 0: #### left side of curr node
#                         if arr[r][c-1] == 1:
#                             q.append([r,c-1])

#                     if r+1 < rl and c  < cl:#### down of curr node
#                         if arr[r+1][c] == 1:
#                             q.append([r+1,c])  
# print(count)
        
        
##########################################################
##########################################################
# Given a 2D Array containing 0's(empty cell) and 1's(fresh orange)
# and 2's (rotten orange). every mintues all fresh orange immediately
# adjacent (4 direction) to rotten oranges will rot 
# how many mintuesmust pass untill all oranges are rotten ?
# if all the oranges's can't rot return -1

# def check(arr):
#     rl = len(arr)
#     cl = len(arr[0])
#     minutes = 0 
#     q = []
#     for i in range(rl):
#         for j in range(cl):
#             if arr[i][j] == 2: 
#                 q.append([i,j])

#     while len(q):
#         l = len(q)
#         count = 0 
#         while count < l:
#             r,c = q.pop(0)
#             arr[r][c] = 2
#             if r-1 >= 0 : 
#                 if arr[r-1][c] == 1:
#                     # arr[r-1][c] = 2 
#                     q.append([r-1,c])
#             if r+1 < rl : 
#                 if arr[r+1][c] == 1:
#                     # arr[r+1][c] = 2  
#                     q.append([r+1,c])
#             if c-1 >= 0 : 
#                 if arr[r][c-1] == 1:
#                     # arr[r][c-1] = 2  
#                     q.append([r,c-1])
#             if c+1 < cl : 
#                 if arr[r][c+1] == 1:
#                     # arr[r][c+1] = 2  
#                     q.append([r,c+1])
#             count += 1
#         minutes += 1

#     for i in range(rl):
#         for j in range(cl):
#             if arr[i][j] == 1: 
#                 return -1
#     return minutes


# a1 = [
# [1,1,1,0,0],
# [2,1,1,0,0],
# [0,0,0,1,2],
# [0,0,0,0,1]
# ]

# a2 = [
# [1,1,1,0,0],
# [2,1,1,0,0],
# [0,0,0,1,2],
# [1,0,0,0,1]
# ]

# print(check(a1))    
# print(check(a2))             

        

##########################################################
##########################################################
# Given a 2D Array containing 0's(gates) and -1's(walls)
# and NOne's (empty room). fill each empty room with the number 
# of steps to nearest gate.


arr =  [
[None,   -1,   0, None],
[None, None, None,  -1],
[None,   -1, None,  -1],
[   0,   -1, None,None]
]

rl = len(arr)
cl = len(arr[0])

q = []
for i in range(rl):
    for j in range(cl):
        if arr[i][j] == 0 :
            q.append([i,j])

while len(q):
    r,c = q.pop(0)

    if r-1 >= 0 : 
        if arr[r-1][c] == None:
            arr[r-1][c] = arr[r][c] +1 
            q.append([r-1,c])
        elif arr[r-1][c] > arr[r][c] +1:
            arr[r-1][c] = arr[r][c] +1
            q.append([r-1,c])
    if r+1 < rl : 
        if arr[r+1][c] == None:
            arr[r+1][c] = arr[r][c] +1 
            q.append([r+1,c])
        elif arr[r+1][c] > arr[r][c] +1:
            arr[r+1][c] = arr[r][c] +1
            q.append([r+1,c])

    if c-1 >= 0 : 
        if arr[r][c-1] == None:
            arr[r][c-1] = arr[r][c] +1 
            q.append([r,c-1])
        elif arr[r][c-1] > arr[r][c] +1:
            arr[r][c-1] = arr[r][c] +1
            q.append([r,c-1])

    if c+1 < cl : 
        if arr[r][c+1] == None:
            arr[r][c+1] = arr[r][c] +1 
            q.append([r,c+1])
        elif arr[r][c+1]> arr[r][c] +1:
            arr[r][c+1] = arr[r][c] +1
            q.append([r,c+1])  
print(arr)