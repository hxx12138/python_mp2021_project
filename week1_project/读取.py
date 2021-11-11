import jieba
import jieba.analyse
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import collections
import numpy as np
from PIL import Image

def draw_cloud(read_name):
    #image = Image.open('')
    wc = WordCloud(font_path = 'Arial Unicode.ttf',background_color = 'black',max_words=100)
    dic = words_count
    wc.generate_from_frequencies(dic)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    wc.to_file('词云.png')


def dist_matrix(vs_list, content):
    length = len(vs_list)
    distance = []
    vector1 = np.array(vs_list)
    for i in range(length):
        vector2 = vs_list[i]
        dis = np.sqrt(np.sum(np.square(vector1 - vector2)))
        distance.append(dis)
        print("第%d个评论与重心的距离为：%f" %((i+1), distance[i]) )
    pos = distance.index(min(distance))
    print("第%d个评论为评论重心" %(pos+1))
    print("评论内容为：" + content[pos])


if __name__ == '__main__':
    with open(r'jd_comments/stopwords_list.txt','r',encoding='utf-8') as s:
        stopwords = s.read()
        stopwords_list = stopwords.split('\n')

    with open(r'jd_comments/jd_comments.txt','r',encoding='utf-8') as f:
        text_line = f.read()
        text_list = text_line.split('\n')
        print(text_list[0])

    words_count = {}
    for i in range(len(text_list)):
        words = jieba.analyse.textrank(text_list[i],topK=20,withWeight=False,allowPOS=('n','v','a','d'))
        #words = jieba.analyse.textrank(text_list[i], topK=20, withWeight=False)
        for word in words:
            if word not in stopwords_list:
                if word not in words_count:
                    words_count[word] = 1
                else:
                    words_count[word] +=1

    words_count_sorted = collections.OrderedDict(sorted(words_count.items(), key=lambda dc:dc[1],reverse=True))


    words_count_list = []
    for key in words_count_sorted:
        if words_count_sorted[key] >= 30:
            words_count_list.append({'word': key, 'count': words_count_sorted[key]})
    print(words_count_list)

    words_sorted_list = []
    for j in range(len(words_count_list)):
        words_sorted_list.append(words_count_list[j]['word'])
    print(words_sorted_list)

    print('text_list 长度',len(text_list))


    feature_vector_list = []
    for i in range(len(text_list)):
        feature_vector = np.zeros(len(words_count_list))
        for j in range(len(words_count_list)):
            if words_count_list[j]['word'] in text_list[i]:
                feature_vector[j] = 1
        feature_vector_list.append(feature_vector)
    print(feature_vector_list[0])

    dist_matrix(feature_vector_list,text_list)

    core_vector = np.zeros(len(words_count_list))
    for i in range(len(text_list)):
        core_vector+=feature_vector_list[i]
    core_vector/=[len(text_list)]
    print(core_vector)

    words_df = pd.DataFrame(words_count_list)
    print(words_df.head())
    words_df.to_csv('keyword.csv',encoding='utf-8')

    draw_cloud('keyword.csv')

