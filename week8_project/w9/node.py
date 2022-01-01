class Node:
	def __init__(self,name):
		self._name=name
		self._children=[]

	def get_name(self):
		return self._name

	def add_child(self,node):
		self._children.append(node)

	def __iter__(self):
		return iter(self._children)

	def __repr__(self):
		return 'Node({})'.format(self.get_name())

	def depth_first(self):
		yield self
		for c in self:
			yield from c.depth_first()

if __name__=='__main__':
	root=Node('root')
	lf=Node('lchild')
	rf=Node('rchild')
	root.add_child(lf)
	root.add_child(rf)
	lf.add_child(Node('lf_lf'))
	lf.add_child(Node('lf_rf'))
	rf.add_child(Node('rf_lf'))
	for ch in root.depth_first():
		print(ch)