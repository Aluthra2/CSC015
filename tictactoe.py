from graphics import *
import random

def createWin():
	win = GraphWin("tictac", 500, 500)
	win.setCoords(0, 0, 3, 3)
	for x in range(3):
		for y in range(3):
			Rectangle(Point(x, y), Point(x+1, y+1)).draw(win)
	return win

def getMax(arr):
	max = arr[0][0];
	counter = 0;
	idx = 0;
	for x in arr:
		counter = counter + 1;
		if x[0] > max:
			max = x[0];
			idx = counter - 1;
	return idx;

def eval(grids, color, x, y, steps):
	score = 0;
	if color == "red":
		opp = "yellow";
	else:
		opp = "red";
	grids[x][y] = color;
	if getWinner(grids) == color:
		grids[x][y] = "_";
		return 1;
	if steps == 0:
		if getWinner(grids) == color:
			grids[x][y] = "_";
			return 1;
		elif getWinner(grids) == opp:
			grids[x][y];
			return -1;
		else:
			grids[x][y] = "_";
			return 0;
	else:
		for a in range(0,3):
			for b in range(0,3):
				if grids[a][b] == "_":
					score = score - eval(grids,opp,a,b,steps-1);
	grids[x][y] = "_";
	return score;

def empty(grid):
	counter = 0;
	for x in range(0,3):
		for y in range(0,3):
			if grid[x][y] == "_":
				counter = counter + 1;
	return counter;

def computerChooseLocation(grid):
	steps = empty(grid);
	arrScores = [];
	if steps == 9:
		return random.randint(0,2), random.randint(0,2);
	else:
		for x in range(3):
			for y in range(3):
				if grid[x][y] == "_":
					score = eval(grid, "red", x, y, steps);
					scores = [score, x, y];
					arrScores.append(scores);
	idx = getMax(arrScores);
	x, y = arrScores[idx][1], arrScores[idx][2];
	return x, y;

def userChooseLocation(win):
	p = win.getMouse()
	x, y = int(p.getX()),int(p.getY())
	return x,y

def canPlaceToken(grid, x, y):
	if grid[x][y]=="_": return True
	else: return False

def placeToken(win, grid,x, y, color):
	grid[x][y] = color
	circ = Circle(Point(x+0.5, y+0.5), 0.5)
	circ.setFill(color)
	circ.draw(win)
	


def getWinner(grids):
	#1. check rows
	for x in range(3):
		if grids[x][0] == grids[x][1]==grids[x][2] and grids[x][0]!="_":
			return grids[x][0]

	#2. check columns
	for x in range(3):
		if grids[0][x] == grids[1][x]==grids[2][x] and grids[0][x]!="_":
			return grids[0][x]

	#3. check the two diagnals
	if grids[0][0]==grids[1][1]==grids[2][2] and grids[0][0]!="_":
		return grids[0][0]

	if grids[2][0]==grids[1][1]==grids[0][2] and grids[2][0]!="_":
		return grids[2][0]
	
	return "_"

def reportWinner(win, winner):
	lbl = Text(Point(1.5, 1.5), "Winner is " + winner)
	lbl.setSize(24)
	lbl.draw(win)


def main():
#1. create window and grids
	win = createWin()

# turn = red; //alternates between red/yellow
	turn = "yellow";

# grids is 3 X 3 array to store information
	grid = [
		[ "_", "_", "_"],
		[ "_", "_", "_"],
		[ "_", "_", "_"]
		]

#2. repeat up to 9 times
	for x in range(9):

   #          wait for user to place a token
		if turn=="red":
			x, y = computerChooseLocation(grid)
		else:
			x, y = userChooseLocation(win)
		if canPlaceToken(grid, x, y):
			placeToken(win, grid, x, y, turn)
		else:
			print "User", turn, "places token in the wrong place!"
			print "User", turn, "loses the game!"
			break

   #	    if someone wins, display msg, AND break
		winner = getWinner(grid)
		if winner!="_":
			reportWinner(win, winner)
			break

   # 		Switch color
		if turn=="red":
			turn= "yellow"
		else:
			turn= "red"

	win.getMouse()

main()
