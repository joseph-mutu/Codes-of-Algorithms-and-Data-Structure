import os
import numpy as np

class node:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def dist(cur_node,want_node):
	return np.sqrt(np.power((cur_node.x - want_node.x),2) + np.power((cur_node.y - want_node.y),2))

def init_graph():
	for i in range(num_nodes):
		for j in range(num_nodes):
			tem_dis = dist(nodes[i],nodes[j])
			if tem_dis <= max_step:
				check_dis[i,j] = 1
				check_dis[j,i] = 1
		check_dis[i,i] = 0

	for i in range(num_nodes):
		if check_dis[0,i] > 0:
			dis[i] = 1
	
def choose_start():
	tem_dis = []
	for i in range(num_nodes):
		if check_dis[0,i] > 0:
			path[i] = 0
			tem_dis.append((dist(nodes[0],nodes[i]),i))
	sorted(tem_dis,key = lambda x:x[1])
	for i in range(len(tem_dis)):
		que.append(tem_dis[i][1])

def check_start_edge():
	cur_node = nodes[0]
	if (cur_node.x + max_step >= 42.5) or (cur_node.y + max_step >= 42.5):
		return True
	elif (cur_node.x - max_step <= -42.5) or (cur_node.y - max_step <= -42.5):
		return True
	else:
		return False

def safe(cur_node):
	if (cur_node.x + max_step >= 50) or (cur_node.y + max_step >= 50):
		return True
	elif (cur_node.x - max_step <= -50) or (cur_node.y - max_step <= -50):
		return True
	else:
		return False

def print_result(end):
	ans = []
	while 1:
		ans.append(end)
		end = path[end]
		if end < 0:
			break

	for i in range(len(ans)-2,-1,-1):
		print(nodes[ans[i]].x,nodes[ans[i]].y)
	return 


def dijkstra():
	init_graph()
	choose_start()
	flag_start = 1
	while 1:
		if len(que) == 0:
			break
		min_index = que.pop(0)
		if safe(nodes[min_index]):
			global mini_dis,flag_safe
			mini_dis = min_index
			flag_safe = True
			returne 
		for i in range(num_nodes):
			if check_dis[min_index,i] > 0 and dis[i] < -1:
				dis[i] = dis[min_index] + 1
				path[i] = min_index
				que.append(i)


flag_safe = False
in_data = list(map(int,input().split()))
tem_count = num_nodes = in_data[0]
max_step = in_data[1]
nodes = []
nodes.append(node(0,0))

while tem_count :
	tem_count -= 1
	tem_data = list(map(int,input().split()))
	tem_node = node(tem_data[0],tem_data[1])
	if dist(nodes[0],tem_node) < 7.5 or tem_data[0] > 50 or tem_data[0] < -50 or tem_data[1] > 50 or tem_data[1] < -50:
		num_nodes -= 1
		continue
	else:
		nodes.append(tem_node)


mini_dis = -1
dis = [-2 for i in range(num_nodes+1)]
dis[0] = -1
path = [-2 for i in range(num_nodes + 1)]
path[0] = -1
que = []
nodes_check = [i for i in range(num_nodes)]
check_dis = np.full((num_nodes,num_nodes),-1,dtype = int)


if check_start_edge():
	print(1)	
else:
	dijkstra()
	if flag_safe:
		print(dis[mini_dis] + 1)
		print_result(mini_dis)
	else:
		print(0)
