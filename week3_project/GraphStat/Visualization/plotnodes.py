import GraphStat.NetworkBuilder.stat as st
import networkx as nx
import matplotlib.pyplot as plt
import GraphStat.NetworkBuilder.graph as gh

def plot_nodes_attr(graph, feature):
    G = nx.Graph()

    # count = 0

    nodes = []
    for key in graph:
        nodes.append(key)
        # count+=1
        # if count>1000:
        # break
    G.add_nodes_from(nodes)

    edges = []
    for key in graph:
        # count+=1
        # if count>1000:
        # break
        for node in graph[key]:
            edges.append((key, node))
    # print(edges)
    G.add_edges_from(edges)

    count = 0
    degree = []
    for key in feature:
        # count+=1
        # if count>1000:
        # break
        degree.append(feature[key])
    print(degree)
    nx.draw(G, nodelist = nodes, node_size = [(i * 100) for i in degree])
    plt.show()



'''path = '/Volumes/HIKVISION/何熙1908/大三上课程/现代程序设计/第三次作业/GraphStat/NetworkBuilder/graph.pkl'
graph = gh.load_graph(path)
feather = st.cal_degree_distribution(graph)
plot_nodes_attr(graph, feather)'''