import matplotlib.pyplot as plt
import jieba
import numpy as np
jieba.load_userdict(r'Anger makes fake news viral online-data&code/data/emotion_lexicon/anger.txt')
jieba.load_userdict(r'Anger makes fake news viral online-data&code/data/emotion_lexicon/disgust.txt')
jieba.load_userdict(r'Anger makes fake news viral online-data&code/data/emotion_lexicon/fear.txt')
jieba.load_userdict(r'Anger makes fake news viral online-data&code/data/emotion_lexicon/joy.txt')
jieba.load_userdict(r'Anger makes fake news viral online-data&code/data/emotion_lexicon/sadness.txt')
import jieba.analyse
import re

def get_path(file_path):
    file_path = r'Anger makes fake news viral online-data&code/data/emotion_lexicon/'
    def read_exact(emotion):
        nonlocal file_path
        file_path += emotion
        return file_path
    return read_exact


def read_emotion(file):
    with open(file,'r',encoding='utf-8') as f:
        words = f.read()
        words_list = words.split('\n')
    return words_list


def read_txt(file):
    with open(file,'r',encoding='utf-8') as f:
        sentences = f.read()
        text_list = sentences.split('\n')
    return text_list

def read_stopwords(file):
    with open(file,'r',encoding='utf-8') as f:
        stopwords = f.read()
        stopwords_list = stopwords.split('\n')
    return stopwords_list

def clean(text_list):
    for i in range(len(text_list)):
        text_list[i] = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", text_list[i])  # 去除正文中的@和回复/转发中的用户名
        text_list[i] = re.sub(r"\[\S+\]", "", text_list[i])  # 去除表情符号
        text_list[i] = re.sub(r"#\S+#", "", text_list[i])      # 保留话题内容
        URL_REGEX = re.compile(
            r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
            re.IGNORECASE)
        text_list[i] = re.sub(URL_REGEX, "", text_list[i])  # 去除网址
        text_list[i] = text_list[i].replace("转发微博", "")  # 去除无意义的词语
        text_list[i] = re.sub(r"\s+", " ", text_list[i])  # 合并正文中过多的空格
    return text_list

def word_cut(text_list):
    text_cut_list = []
    for i in range(len(text_list)):
        text_cut = jieba.lcut(text_list[i])
        text_cut_list.append(text_cut)
    return text_cut_list

def stop_words(text_cut_list,stopwords_list):
    text_stop_list = []
    for i in range(len(text_cut_list)):
        text_stop = []
        for j in range(len(text_cut_list[i])):
            if (text_cut_list[i][j] in stopwords_list) or text_cut_list[i][j] == ' ':
                pass
            else:
                text_stop.append(text_cut_list[i][j])
        text_stop_list.append(text_stop)
    return text_stop_list

def get_time(text_list):
    time_list = []
    location_list = []
    for i in range(len(text_list)):
    #for i in range(6):
        #length = len(text_list[i])
        mark = text_list[i].rfind('[')
        location_list.append(text_list[i][mark:])
        time_list.append(text_list[i][mark - 31:mark])
        text_list[i] = text_list[i][0:mark - 31]
    #print(location_list)
    #print(time_list)
    #print(text_list[0])

    return text_list,time_list, location_list

def emotion_analsis(text_stop_list,emotion_list):
    emotion_vector_list = []
    emotion_value_list = []
    for i in range(len(text_stop_list)):
        emotion_vector = {'anger': 0, 'disgust': 0, 'fear': 0, 'joy': 0, 'sadness': 0}
        for word in text_stop_list[i]:
            if word in emotion_list[0]:
                emotion_vector['anger'] += 1
            elif word in emotion_list[1]:
                emotion_vector['disgust'] += 1
            elif word in emotion_list[2]:
                emotion_vector['fear'] += 1
            elif word in emotion_list[3]:
                emotion_vector['joy'] += 1
            elif word in emotion_list[4]:
                emotion_vector['sadness'] += 1
            else:
                pass
        max = 0
        emotion_value = 'none'
        for key in emotion_vector:
            if emotion_vector[key] > max:
                max = emotion_vector[key]
                emotion_value = key
        emotion_vector_list.append(emotion_vector)
        emotion_value_list.append(emotion_value)
    return emotion_vector_list,emotion_value_list

def emotion_hourmode(time_list,emotion_value_list):
    emotion_hour_list = [{'anger': 0, 'disgust': 0, 'fear': 0, 'joy': 0, 'sadness': 0} for i in range(24)]
    #print(emotion_hour_list)
    emotion_value_list.pop()
    for i in range(len(emotion_value_list)):
        hour = int(time_list[i][11:13])
        #print(emotion_value_list[hour])
        if emotion_value_list[i] in emotion_hour_list[hour]:
            emotion_hour_list[hour][emotion_value_list[i]]+=1
    return emotion_hour_list

def emotion_locationmode(location_list, emotion_value_list):
    location_x_list = []
    location_y_list = []
    location_emotion = []
    color_list = ['coral','khaki','aquamarine','deepskyblue','violet']
    emotion_list = ['anger','disgust','fear','joy','sadness']
    #print(location_list)
    for i in range(len(emotion_value_list)-1):
        location_x_list.append(eval(location_list[i])[0])
        location_y_list.append(eval(location_list[i])[1])
        location_emotion.append(emotion_value_list[i])
    for i in range(5):
        x = []
        y = []
        for j in range(len(emotion_value_list)-1):
            if emotion_list[i] == location_emotion[j]:
                x.append(location_x_list[j])
                y.append(location_y_list[j])
        plt.scatter(x, y, s=None, c=color_list[i], marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None, plotnonfinite=False, data=None)
        plt.title('the location mode of '+emotion_list[i])
        plt.show()

def count(emotion_value_list):
    ans = {}
    for i in emotion_value_list:
        if i in ans:
            ans[i]+=1
        else:
            ans[i]=1
    return ans

def main():
    text_list = read_txt('weibo.txt')
    stopwords_list = read_stopwords('stopwords_list.txt')
    #print(stopwords_list)
    text_list = clean(text_list)
    text_list, time_list ,location_list = get_time(text_list)
    text_cut_list = word_cut(text_list)
    text_stop_list = stop_words(text_cut_list,stopwords_list)


    emotion_list = []
    emotion_list.append(read_emotion(get_path('')('anger.txt')))
    emotion_list.append(read_emotion(get_path('')('disgust.txt')))
    emotion_list.append(read_emotion(get_path('')('fear.txt')))
    emotion_list.append(read_emotion(get_path('')('joy.txt')))
    emotion_list.append(read_emotion(get_path('')('sadness.txt')))
    emotion_vector_list,emotion_value_list = emotion_analsis(text_stop_list,emotion_list)

    ans = count(emotion_value_list)
    print(ans)

    #for i in range(len(text_list)):
    for i in range(1):
        print('-----------------------------------------------------------------------------------------------')
        print('num:',i)
        print('微博原文：',text_list[i])
        print('提取分词：',text_stop_list[i])
        print('情绪词向量：',emotion_vector_list[i])
        print('主要情绪类型：',emotion_value_list[i])
        print('微博发送时间：',time_list[i])
        print('微博发送地点',location_list[i])
        print('-----------------------------------------------------------------------------------------------')

    emotion_hour_list = emotion_hourmode(time_list,emotion_value_list)
    print(emotion_hour_list)

    x = np.arange(24)
    type_list = ['anger','disgust','fear','joy','sadness']
    for i in range(5):
        hour_draw_list = [0 for i in range(24)]
        for j in range(24):
            hour_draw_list[j] = emotion_hour_list[j][type_list[i]]
        plt.figure(figsize=(10, 5))
        plt.plot(x,hour_draw_list,'black',label=type_list[i])
        plt.title(f'the time about {type_list[i]}')
        plt.grid()
        plt.show()

    emotion_locationmode(location_list, emotion_value_list)

main()








