def move(x, y, direction):
	if direction==0: #north
		y += 1
	elif direction==1: #east
		x += 1
	elif direction==2: #south
		y -= 1
	else:
		x -= 1

	return x, y

def turn_right(direction):
	return (direction+1)%4

def turn_left(direction):
	return (direction-1)%4

actions = input()
direction = 0
x, y = 0, 0

for a in actions*4:
	if a=='G':
		x, y = move(x, y, direction)
	elif a=='L':
		direction = turn_left(direction)
	elif a=='R':
		direction = turn_right(direction)

if (x, y) == (0, 0):
	print(1)
else:
	print(0)