def list_all_nodes(root):

	my_stack = []
	my_stack_map = {}
	final = []
	my_stack.append(root)
	my_stack_map[root] = True

	while my_stack:
		last = len(my_stack) -1
		top_node = my_stack[last]
		if top_node.first and top_node.first not in my_stack_map:
			my_stack.append(top_node.first)
			my_stack_map[top_node.first] = True
		elif top_node.second and top_node.second not in my_stack_map:
			my_stack.append(top_node.second)
			my_stack_map[top_node.second] = True
		elif top_node.third and top_node.third not in my_stack_map:
			my_stack.append(top_node.third)
			my_stack_map[top_node.third] = True
		else:
			final.append(top_node.val)
			my_stack.pop()

	return final

class Node:
	def __init__(self,val,first,second,third):
		self.val = val
		self.first = first
		self.second = second
		self.third = third



s = Node('s',None,None,None)
a = Node('a',None,None,None)
b = Node('b',None,None,None)
c = Node('c',None,None,None)
d = Node('d',None,None,None)
e = Node('e',None,None,None)
f = Node('f',None,None,None)
g = Node('g',None,None,None)

s.first = a
s.second = b
s.third = c

a.first = s
a.second = d

b.first = s
b.second = e

c.first = s
c.second = f

d.first = a
d.second = g

e.first = b
e.second = g

f.first = c
f.second = g

g.first = d
g.second = e
g.third = f


data = list_all_nodes(s)
print(data)