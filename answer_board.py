from board_game import game_before,game_output

grid = [[0,1,0,1,1,0],[0,0,0,1,1,0],[0,1,0,1,1,0],[0,1,0,0,0,0],[0,1,1,1,1,1],[0,0,0,0,0,0]]
game_before(grid,[250,250],[250,0])

adj_list = { i : [] for i in range(len(grid))}
print(adj_list)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            adj_list[i].append(j)
            adj_list[j].append(i)

print(adj_list)




grid = [[0,1,0,1,1,0],[2,2,2,1,1,2],[2,1,2,1,1,2],[2,1,2,2,2,2],[2,1,1,1,1,1],[2,2,2,2,2,0]]

game_output(grid,[250,250],[250,0])
