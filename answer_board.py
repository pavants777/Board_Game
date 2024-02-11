from board_game import game_before,game_output

grid = [[0,1,0,1,1,0],[0,0,0,1,1,0],[0,1,0,1,1,0],[0,1,0,0,0,0],[0,1,1,1,1,1],[0,0,0,0,0,0]]
game_before(grid,[250,250],[250,0])

# adj_list make graph to find answer : 
adj_list = { i : [] for i in range(len(grid))}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            adj_list[i].append(j)
            adj_list[j].append(i)
print(adj_list)


# Back to grid form 
grid = [[0]*6 for _ in range(6)]
for node,neighbors in adj_list.items():
    for neighbor in neighbors:
        grid[node][neighbor] = 1
    
print(grid)

grid = [[0,1,0,1,1,0],[2,2,2,1,1,2],[2,1,2,1,1,2],[2,1,2,2,2,2],[2,1,1,1,1,1],[2,2,2,2,2,0]]
game_output(grid,[250,250],[250,0])