from multiprocessing import Process,Queue
import time
import jieba
import jieba.analyse

# 作业要求

# MapReduce是利用多进程并行处理文件数据的典型场景。
# 作为一种编程模型，其甚至被称为Google的”三驾马车“之一(尽管目前由于内存计算等的普及已经被逐渐淘汰)。
# 在编程模型中，Map进行任务处理，Reduce进行结果归约。
# 本周作业要求利用Python多进程实现MapReduce模型下的文档库（搜狐新闻数据(SogouCS)，
# 下载地址：https://www.sogou.com/labs/resource/cs.php），注意仅使用页面内容，即新闻正文）词频统计功能。


# 1. Map进程读取文档并进行词频统计，返回该文本的词频统计结果。

class Map(Process):

    def __init__(self, num, text_list, map_task, q):
        super().__init__()
        self.num = num
        self.text_list = text_list
        self.map_task = map_task
        self.q = q

    def run(self):
        map_start = time.time()
        with open(r'stopwords_list.txt','r',encoding='utf-8') as s:
            stopwords = s.read()
            stopwords_list = stopwords.split('\n')

        words_count = {}
        for i in range(self.map_task[self.num][0],self.map_task[self.num][1]):
            words = jieba.lcut(self.text_list[i])
            #words = jieba.analyse.textrank(text_list[i], topK=20, withWeight=False)
            for word in words:
                if word not in stopwords_list:
                    if word not in words_count:
                        words_count[word] = 1
                    else:
                        words_count[word] +=1
        map_end = time.time()
        print(f"the no.{self.num} process use {map_end-map_start}s")
        self.q.put(words_count)
        #return words_count


# 2. Reduce进程收集所有Map进程提供的文档词频统计，更新总的文档库词频，并在所有map完成后保存总的词频到文件。

class Reduce(Process):

    def __init__(self):
        super().__init__()

    def run(self):
        return


# 3. 主进程可提前读入所有的文档的路径列表，供多个Map进程竞争获取文档路径；或由主进程根据Map进程的数目进行分发；或者单独实现一个分发进程，与多个MAP进程通信。 

def read(path):
    with open(path,'rb') as f:
        sentences = f.readlines()
        #print(len(sentences))
        text_list = []
        for sentence in sentences:
            #print(sentence[2:11])
            if str(sentence[:9],encoding='gb18030') == '<content>':
                text_list.append(str(sentence[9:-9],encoding='gb18030'))
    return text_list


if __name__ == '__main__':

    text_list = read('news_sohusite_xml.dat')
    total_text = len(text_list)
    print(len(text_list))

    map_count = 8
    map_task=[[] for i in range(map_count)]
    for i in range(map_count-1):
        start = int((i/8)*total_text)
        end = int(((i+1)/8)*total_text)
        map_task[i].append(start)
        map_task[i].append(end)
    map_task[map_count-1].append(end)
    map_task[map_count-1].append(total_text)

    #print(map_task)
    # global word_count_queue
    word_count_queue = Queue()
    
    map_process = []
    reduce_process = []

    for i in range(map_count):
        p = Map(i,text_list,map_task,word_count_queue)
        map_process.append(p)
    
    main_start = time.time()

    for p in map_process:
        p.start()
    for p in map_process:
        p.join()

    main_end = time.time()
    print(f"The whole process use {main_end-main_start}s")


    




# 4. 记录程序运行时间，比较不同Map进程数量对运行时间的影响，可以做出运行时间-进程数目的曲线并进行简要分析。






