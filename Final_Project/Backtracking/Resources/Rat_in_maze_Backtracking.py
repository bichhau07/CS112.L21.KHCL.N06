ref: https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/
		
N = 4

# Hàm in ma trận đường đi
def printSolution( sol ):
	
	for i in sol:
		for j in i:
			print(str(j) + " ", end ="")
		print("")

# Hàm check nếu trong phạm vi của ma trận
def isSafe( maze, x, y ):
	
	if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
		return True
	
	return False

def solveMaze( maze ):
	
	# Tạo ra ma trận đường đi với giá trị False
	sol = [ [ 0 for j in range(4) ] for i in range(4) ]
	
	if solveMazeUtil(maze, 0, 0, sol) == False:
		print("Solution doesn't exist");
		return False
	
	printSolution(sol)
	return True
	
# Hàm đệ qui để giải quyết bài toán
def solveMazeUtil(maze, x, y, sol):
	
	# Nếu tới đích -> return True
	if x == N - 1 and y == N - 1 and maze[x][y]== 1:
		sol[x][y] = 1
		return True
		
	# Kiểm tra nếu vị trí (x,y) có trong phạm vi
	if isSafe(maze, x, y) == True:
		# Kiểm tra tại vị trí đó có trong danh sách được thăm hay không
		if sol[x][y] == 1:
			return False
		
		# Nếu không có, đánh dấu vị trí đó trong danh sách thăm
		sol[x][y] = 1
		
		# Tiến về chiều x
		if solveMazeUtil(maze, x + 1, y, sol) == True:
			return True
			
		# Nếu tiến về chiều x không được
		# Tiến xuống chiều y
		if solveMazeUtil(maze, x, y + 1, sol) == True:
			return True
		
		# Nếu tiến về chiều y không được
		# Lùi về chiều x-1
		if solveMazeUtil(maze, x - 1, y, sol) == True:
			return True
			
		# Nếu theo chiều x-1 không được
		# Lùi về chiều y-1
		if solveMazeUtil(maze, x, y - 1, sol) == True:
			return True
		
		# Nếu 4 chiều đều không khả thi
		# BACKTRACK: bỏ đánh dấu vị trí đó khỏi danh sách thăm
		sol[x][y] = 0
		return False


maze = [ [1, 0, 0, 0],
		[1, 1, 0, 1],
    	[0, 1, 0, 0],
		[1, 1, 1, 1] ]
			
solveMaze(maze)

