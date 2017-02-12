import os
import time
from collections import Counter

####    CONWAY'S GAME OF LIFE    ####

t = 0
size = 28

s = [(2,3),(2,4),(2,5),(1,5),(0,4),(7,0),(7,1),(7,2)]
s = s + [(13,13),(13,14),(14,13),(14,14)]
lifespan = [s]
k = [(17,7),(17,8),(18,8),(18,7)]
lifeplan = [k]

def display(instance):
	os.system('clear')
	print
	print instance
	board = []
	for row in range(size):
		board.append(['  ']*size)
	for spot in lifespan[instance]:
		a = spot[0]
		b = spot[1]
		board[a][b]='{}'
	print
	print '--' * size
	for c in board:
		word = ''
		for t in c:
			word = word + t
		print '|' + word + '|'

	print ' ' + '--' * size		
	print

def iterate():
	old = lifespan[-1]
	temp = []
	neighbors = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
	for a in old:
		for b in neighbors:
			x = a[0] + b[0]
			y = a[1] + b[1]
			if 0 <= x <= size - 1 and 0 <= y <= size - 1:
				temp.append((x,y))
	new = temp_to_new(old, temp)
	lifespan.append(new)
	lifeplan.append(k)

def temp_to_new(old, temp):
	new = []
	live = [2,3]
	born = [3]
	counted = Counter(temp)
	for i in counted:
		newi = (i[0],i[1])
		testes = newi in old
		if i in old:
			if counted[i] in live:
				new.append(i)			
		else:
			if counted[i] in born:
				new.append(i)
	return new


for a in range(150):
	display(a)
	if a+1 == len(lifespan):
		iterate()
	print

	time.sleep(.05)

