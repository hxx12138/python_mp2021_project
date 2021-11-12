import pickle

'''def init_node(path):
    #邻接表的字典存储
    with open(path,'r',encoding='utf-8') as f:
        file = f.read()
        info_list = file.split('\n')
        #print(len(node_list))
        count = 0
        for i in info_list:
            count += 1
            if i == '*Edges':
                break
        #print(count)
        #edges = info_list[count:]
        node_list = node[:count-1]
        #for i in range(len(edges)):
            #edges[i] = edges[i].split('\t')
    return node_list'''

def init_graph(path):
    #邻接表的字典存储
    with open(path,'r',encoding='utf-8') as f:
        file = f.read()
        info_list = file.split('\n')
        count = 0
        for i in info_list:
            count += 1
            if i == '*Edges':
                break
        print(count)
        edges = info_list[count:]
        #node_list = node[:count-1]
        for i in range(len(edges)):
            edges[i] = edges[i].split('\t')

    #邻接表初始化
    connect_dict = {}
    for i in range(count-2):
        connect_dict[i] = {}
    #print(connect_dict)

    #构件图结构
    for i in range(len(edges)):
        n1 = int(edges[i][0])
        n2 = int(edges[i][1])
        if n1 not in connect_dict[n2]:
            connect_dict[n2][n1] = 1
        if n2 not in connect_dict[n1]:
            connect_dict[n1][n2] = 1
    return edges,connect_dict

def save_graph(connect_dict):
    print("正在保存")
    with open('graph.pkl','wb') as f:
        pickle.dump(connect_dict, f)

def load_graph(path):
    print('正在加载')
    with open(path,'rb')as f:
        connect_dict = pickle.load(f)
    return connect_dict

'''def print_node(node_list):
    print(node_list[0])
    for i in range(1,len(node_list)):
    #for i in range(1,10):
        node_content = node_list[i].split('\t')
        #print(len(node_content))
        print('id:{}\tname:{}\tweight:{}\ttype:{}others:{}'.format(node_content[0],node_content[1],node_content[2],node_content[3],node_content[4]))
'''

'''edges, connect_dict = init_graph(r'/Volumes/HIKVISION/何熙1908/大三上课程/现代程序设计/第三次作业/newmovies.txt')
print(connect_dict)'''
'''save_graph(connect_dict)
connect_dict = load_graph('graph.pkl')
print(connect_dict[0])'''
#print(edges[0:10])
