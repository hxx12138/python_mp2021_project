import pickle

def cal_average_degree(graph):
    total = 0
    for key in graph:
        total += len(graph['key'])
    ans = total/len(graph)
    return ans

def cal_degree_distribution(graph):
    degree_dict = {}
    for key in graph:
        degree_dict[key] = len(graph[key])
    return degree_dict