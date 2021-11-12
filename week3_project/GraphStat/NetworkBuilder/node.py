# coding = utf-8




def init_node(path):
    with open(path,'r',encoding='utf-8') as f:
        file = f.read()
        node_list = file.split('\n')
        #print(len(node_list))
        count = 0
        for i in node_list:
            count+=1
            if i == '*Edges':
                break
        #print(count)
        node_list = node_list[:count-1]
    return node_list

def get_node(path):
    return

def print_node(node_list):
    print(node_list[0])
    for i in range(1,len(node_list)):
    #for i in range(1,10):
        node_content = node_list[i].split('\t')
        #print(len(node_content))
        print('id:{}\tname:{}\tweight:{}\ttype:{}others:{}'.format(node_content[0],node_content[1],node_content[2],node_content[3],node_content[4]))

'''node_list = init_node(r'/Volumes/HIKVISION/何熙1908/大三上课程/现代程序设计/第三次作业/newmovies.txt')
print_node(node_list)'''