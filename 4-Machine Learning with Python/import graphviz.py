import graphviz

d = graphviz.Digraph(comment='The Round Table')
d.edge('A', 'B')
print(d)
