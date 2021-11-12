import GraphStat.NetworkBuilder.graph as gh
import matplotlib.pyplot as plt
import networkx as nx

def plotdgree_distribution(graph):
    G = nx.Graph()

    #count = 0

    nodes = []
    for key in graph:
        nodes.append(key)
        #count+=1
        #if count>1000:
            #break
    G.add_nodes_from(nodes)

    count = 0
    edges = []
    for key in graph:
        #count+=1
        #if count>1000:
            #break
        for node in graph[key]:
            edges.append((key,node))
    #print(edges)
    G.add_edges_from(edges)

    nx.draw_networkx(G)
    plt.show()


'''path = '/Volumes/HIKVISION/何熙1908/大三上课程/现代程序设计/第三次作业/GraphStat/NetworkBuilder/graph.pkl'
graph = gh.load_graph(path)
plotdgree_distribution(graph)'''