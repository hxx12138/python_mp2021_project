#coding:utf-8

import abc
import numpy as np
from matplotlib import pyplot as plt
import collections
import jieba
import jieba.analyse
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import imageio

# 作业要求
# 在使用python时，我们经常会用到许多工具库，它们提供了较为方便的函数调用。
# 但是仍然会有一些情况，例如数据类型或格式不符合函数要求，参数存在差异等，使得调用前需要对数据进行额外处理。
# 本次作业要求基于matplotlib，wordcloud，PIL, imageio等绘图库的绘制函数，设计并实现适配器抽象类和不同的适配类，
# 以实现不同类型数据的多样化可视，并在不同类型的数据上进行充分测试。


# 1. 要求设计抽象类Plotter，至少包含抽象方法plot(data, *args, **kwargs)方法，
# 以期通过不同子类的具体实现来支持多类型数据的绘制，至少包括数值型数据，文本，图片等。

class Plotter(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def plot(self, data, *args, **kwargs):
        pass

# 2. 实现类PointPlotter, 实现数据点型数据的绘制，即输入数据为[(x,y)...]型，每个元素为一个Point类的实例。

class PointPlotter(Plotter):

    def plot(self, data, *args, **kwargs):
        x = []
        y = []
        for point in data:
            #print(point)
            x.append(point[0])
            y.append(point[1])
        x = np.array(x)
        y = np.array(y)
        #print(x)
        #print(y)

        plt.scatter(x,y)
        plt.show()

# 3. 实现类ArrayPlotter, 实现，即输入数据可能是[[x1,x2...]多维数组型数据的绘制,[y1,y2...]]或者[[x1,x2...],[y1,y2...],[z1,z2...]]。

class ArrayPlotter(Plotter):

    def plot(self, data, *args, **kwargs):
        if len(data)==2:
            x = np.array(data[0])
            y = np.array(data[1])
            plt.scatter(x,y)
            plt.show()
        elif len(data)==3:
            x = np.array(data[0])
            y = np.array(data[1])
            z = np.array(data[2])
            fig = plt.figure()
            ax = fig.add_subplot(projection = '3d')
            ax.scatter(x,y,z)
            plt.show()

# 4. 实现类TextPlotter，实现文本型数据的绘制，即输入数据为一段或多段文本，应进行切词，关键词选择（根据频率或tf-idf)，继而生成词云。

class TextPlotter(Plotter):

    def plot(self, data, *args, **kwargs):

        with open(r'stopwords_list.txt','r',encoding='utf-8') as s:
            stopwords = s.read()
            stopwords_list = stopwords.split('\n')

        words_count = {'吉昌':100,'祝好':100}
        for i in range(len(data)):
            #words = jieba.analyse.textrank(data[i],topK=20,withWeight=False,allowPOS=('n','v','a','d'))
            words = jieba.analyse.textrank(data[i], topK=20, withWeight=False)
            for word in words:
                if word not in stopwords_list:
                    if word not in words_count:
                        words_count[word] = 1
                    else:
                        words_count[word] +=1
        words_count_sorted = collections.OrderedDict(sorted(words_count.items(), key=lambda dc:dc[1],reverse=True))

        words_count_list = []
        for key in words_count_sorted:
            if words_count_sorted[key] >= 0:
                words_count_list.append({'word': key, 'count': words_count_sorted[key]})
        print(words_count_list)

        wc = WordCloud(font_path = 'Arial Unicode.ttf',background_color = 'black',max_words=100)
        dic = words_count
        wc.generate_from_frequencies(dic)
        plt.imshow(wc)
        plt.axis('off')
        plt.show()
        wc.to_file('词云.png')

# 5. 实现类ImagePlotter，实现图片型数据的绘制，即输入数据为图片的路径或者图片内容（可以是多张图片），呈现图片并按某种布局组织（如2x2等)。

class ImagePlotter(Plotter):

    def plot(self, data, *args, **kwargs):
        x = args[0]
        y = args[1]
        Image_list = []
        path = 'picture/'
        for item in data:
            if type(item) == str:
                Image_temp = Image.open(path+item).convert(mode='RGB')
                Image_list.append(Image_temp)
            else:
                Image_list.append(item)
        for i in range(len(Image_list)):
            plt.subplot(x,y,i+1)
            plt.imshow(Image_list[i])
        plt.show()

# 6. 实现类GifPlotter, 支持一组图片序列的可视化（通过文件路径或图片内容输入），但输出是gif格式的动态图。

class GifPlotter(Plotter):

    def plot(self, data, *args, **kwargs):
        Image_list = []
        path = 'picture/'
        for item in data:
            if type(item) == str:
                Image_temp = imageio.imread(path+item)
                Image_list.append(Image_temp)
            else:
                Image_list.append(item)
        imageio.mimsave('masterpiece.gif',Image_list,fps=1)

# 附加9：在6中，如果输入是一段落视频的话，能否通过帧采样，将视频绘制为gif并输出为微信表情包？（了解cv2)

class VideoPlotter(Plotter):

    def plot(self, data, *args, **kwargs):
        reader = imageio.get_reader(data)
        for i,im in enumerate(reader):
            print(i,im.mean())


def main():
    
    '''data_point = [(1,2),(2,3),(4,5)]
    draw_point = PointPlotter()
    draw_point.plot(data_point)'''

    '''data_array = [[1,2,3],[1,4,9],[1,8,27]]
    draw_array = ArrayPlotter()
    draw_array.plot(data_array)'''

    '''data_text = ['赵吉昌能让月色温柔，让流星闪烁。眨一眨眼睛，便能让银河坠落。','如果这世界是我的遗嘱，那么赵吉昌，就是我唯一的遗物。','风儿轻，月儿明。赵吉昌的笑貌音容，萦绕在我心中。','给赵吉昌一个人的彩虹屁❤你总是给我这样的感觉，我有句话想说很久了，想让你当我心里的常驻居民，在我的星球里做尽白日梦,这些感情可以说无时无刻不在折磨我。说老实话，来日方长 细水长流爱和感动 我都慢慢给你 。赵吉昌，遇上你的感觉就像走了很远的路终于回到家了 。我的爱意乘着飞驰的地铁，终点是你，赵吉昌，这就是我对你的感觉。小宝贝，你是夜夜的月圆，你就是我的一切了。说老实话，寄你一封情书，以岁月为笔，以心跳为字迹。赵吉昌！睡不着无非两个原因手里有部手机心里有个你 ，这都是我的心里话。我觉得我有点花心 你每天的样子我都好喜欢 。赵吉昌，喜欢上你这件事 我想用一生说给你听 ，赵吉昌，这就是我对你的感觉。小宝贝，所有的坏心情，都在看到你的一刻就瞬间清零,这些感情可以说无时无刻不在折磨我。我要变成一颗小奶糖 夜深了提着星星灯 悄悄的溜进你梦里 说晚安 。赵吉昌！今晚我就是个疯狂存图的机器，你一定不能想象。除了窒息，我没有什么要表演的。土豆会变成土豆泥 猜猜我会变成泥 我爱泥 。赵吉昌，是不是当思念汇集成了一条河 你就可以乘舟而来吖 。我变成仙女棒，你攥在手里，给你带来完美防御，走到哪里都不会下雨。小宝贝，你猜猜我的心在那边？ 在左边？ 不不不，在你那边。 ，这都是我的心里话。赵吉昌，我是太阳 你是苹果 因为太阳喜欢苹果 ，你就是我的一切了。不管现在网络多么发达 但是喜欢你这句 我还是想在你耳边对你说 ，你一定不能想象。赵吉昌,一辈子那么长，没想到，我真的只喜欢你一个人。天上已经有月亮了，请你留在人间当我的月亮吧。赵吉昌，快早些睡，明天还要忙着可爱。赵吉昌，人生即画报。说老实话，月亮预谋了这场温柔，心跳声回响在这宇宙太空中。你是 无力抗拒不停追逐的磁场，这都是我的心里话。我仰望遥远耀眼的明月，却不及过分可爱发光的你。这是我的手背 这是我的脚背 你是我的宝贝 。真诚感谢仙子来到这平凡的人间。我有句话想说很久了，今天的小宝贝也帅到封神了，你就是我的一切了。赵吉昌，我房租到期了 我可以去你心里住嘛？ ,这些感情可以说无时无刻不在折磨我。我在人间贩卖黄昏只为收集世间温柔去见你 。赵吉昌，人都是会变的 从一开始的有点喜欢你 到后来的越来越喜欢你 。你总是给我这样的感觉，赵吉昌！我不看月亮，也不说想你，这样，月亮和你就都蒙在鼓里。我要请你喝酒 什么酒 我们的喜酒 。说老实话，不好意思呐刚刚一不小心就在你心里安了个家 ，这都是我的心里话。说老实话，生命诚可贵，小宝贝的美颜价更高。我有句话想说很久了，拉响心空注意警报，你一定不能想象。想牵着你的手走遍春夏秋冬也尝过油盐酱醋 。赵吉昌，不管现在网络多么发达 但是喜欢你这句 我还是想在你耳边对你说 。你的出现让我发觉世界不无聊，你一定不能想象。我最近要换个发型 什么发型 没你不行 ,这些感情可以说无时无刻不在折磨我。我有句话想说很久了，今天的心也被赵吉昌偷走了。你知道我最喜欢什么神嘛？ 你的眼神 ,这些感情可以说无时无刻不在折磨我。你只是从我心房路过，我却一见钟情开了心门，赵吉昌，这就是我对你的感觉。赵吉昌！不悔梦归处是你。女孩抬抬眼，就收割万千男孩心。我尖叫到地动山摇，整层楼都拉起警报，只因为你过分可爱，赵吉昌，这就是我对你的感觉。赵吉昌，这是什么绝世小甜豆。我的灵魂已经被美貌砸晕，你就是我的一切了。倘若你是晚夏遗留下的最后一声蝉鸣，那我便是穿梭于天地间的捕声之人。本不想多依赖你 只是没有你的日子 太难熬 ，你就是我的一切了。时间总是把对你最好的人留在最后 毕竟喜欢就像一阵风而爱是细水长流 ，你就是我的一切了。说老实话，别看我不动声色，其实我动了心，赵吉昌，这就是我对你的感觉。我有句话想说很久了，今天的小宝贝是舞台教科书了,这些感情可以说无时无刻不在折磨我。赵吉昌，绝了，今日份的小宝贝让人心动到仿佛来了一场800米的田径赛跑。想在小宝贝的睫毛上荡秋千。赵吉昌, 我有很多情话 只想说给你听 。','给赵吉昌一个人的彩虹屁❤你听着，我有一句话想对你说，小宝贝，我在人间贩卖黄昏只为收集世间温柔去见你 。你以为我经常跟你聊天就是喜欢你？ 你以为的很对，我就是喜欢你 ，你就是我的一切了。赵吉昌，我觉得你特别像一款游戏 什么游戏 我的世界 。说老实话，我有点怕你 因为我怕老婆 ，赵吉昌，这就是我对你的感觉。今天的小宝贝也帅到封神了,这些感情可以说无时无刻不在折磨我。赵吉昌！鹤归孤山，你归我。一屋两人三餐四季 只想和你 。我不仅可爱还可爱你了呢 ,这些感情可以说无时无刻不在折磨我。小宝贝，晚秋傍晚清凉的风，冬季彻夜好冷的雪，你一定不能想象。这是什么令人心跳加速的定情现场。没有你，时间都是缓慢的米勒行星，赵吉昌，这就是我对你的感觉。赵吉昌！我是太阳 你是苹果 因为太阳喜欢苹果 ，你就是我的一切了。小宝贝，喜欢上你这件事 我想用一生说给你听 。这种程度的颜值真的是合理的吗，你就是我的一切了。像这样的话，我给你讲一年都不会腻。小宝贝，我在人间贩卖黄昏只为收集世间温柔去见你 ，赵吉昌，这就是我对你的感觉。穿过人海 我还是会脱口而出你的名字 就好像现在遇到的人都有你的影子 ​​​，你一定不能想象。赵吉昌！你说你长的好看我也就忍了 还偏偏长成我喜欢的样子 你要我怎么办 ,这些感情可以说无时无刻不在折磨我。赵吉昌！上了我的贼船就必须和我返航 。赵吉昌，女孩抬抬眼，就收割万千男孩心。你是 傍晚落日余晖的方向，这都是我的心里话。想路过你生命中所有落满金色叶子的秋天，赵吉昌，这就是我对你的感觉。赵吉昌！原来真正漂亮的人是360°无死角的。赵吉昌！你的出现让我发觉世界不无聊。你是我的众星捧月 所有的温柔都只为你 ，你一定不能想象。不知道什么是引力波没关系 只要记住喜欢的人就要抱起来转几圈呀 那样很多万亿年以后 这个宇宙所有星球存活过的生命都会知道 我们曾经爱过 ，赵吉昌，这就是我对你的感觉。你是破晓清晨，灿烂眼中的光景，你一定不能想象。即便沿途处处可见迷雾、断崖，你还是要往远方去。我有句话想说很久了，五月的天，刚诞生的夏天,这些感情可以说无时无刻不在折磨我。赵吉昌！我要请你喝酒 什么酒 我们的喜酒 ，你一定不能想象。说老实话，所有晦暗都留给过往，从遇见你开始，凛冬散尽，星河长眠。说老实话，你是我枕边的书 字字珍贵 句句入心 。赵吉昌！不好意思呐刚刚一不小心就在你心里安了个家 ，你就是我的一切了。小宝贝，千山万水就当伏笔 总会遇到姗姗来迟的你 ,这些感情可以说无时无刻不在折磨我。说老实话，不好意思呐刚刚一不小心就在你心里安了个家 ，你就是我的一切了。小宝贝，我要变成一颗小奶糖 夜深了提着星星灯 悄悄的溜进你梦里 说晚安 ，赵吉昌，这就是我对你的感觉。赵吉昌！我喜欢你 想成为你的大圣 护你周全，保你欢喜 。你是 整夜白雪茫茫的路旁。说老实话，万星沉入目，一眼已相惜，赵吉昌，这就是我对你的感觉。我有句话想说很久了，申请成为您爱里的永久居民 ​​​，赵吉昌，这就是我对你的感觉。喜欢呀 是清风 是朝露 是脸颊红红 是千万万人里 再也装不下其他 ，赵吉昌，这就是我对你的感觉。说老实话，以这样的脸蛋每天生活着是什么感受，真想体验一下，你就是我的一切了。赵吉昌,一辈子那么长，没想到，我真的只喜欢你一个人。每天一个人的时候，我就在想，小宝贝，我不仅可爱还可爱你了呢 ，这都是我的心里话。赵吉昌，你要和我在一起吗？ 允许我用一枚戒指绑住你， 在法律规定下， 把余生分一半给我的那种。 ，赵吉昌，这就是我对你的感觉。说老实话，愿你的每次流泪都是喜极而泣，你一定不能想象。你现在不珍惜我我告诉你过了这个村我下个村等你 。世间万物 唯你最入我心 。世界上好人不少不过你是最重要的一个你要是愿意我就永远爱你你要不愿意我就永远相思 。赵吉昌！我是个小无赖呀会一直赖在你心里嗷 。赵吉昌！除了窒息，我没有什么要表演的，你就是我的一切了。我连人带心都是小宝贝的了，你就是我的一切了。想起细碎温柔的好事时，刚好也想起你。说老实话，你现在不珍惜我我告诉你过了这个村我下个村等你 。赵吉昌，今天也被小宝贝甜到方圆十里都能闻到糖果味。我对你可是有图谋的 想图你一辈子 。这是什么历代top级别的美貌，你就是我的一切了。赵吉昌，一生太短暂，遇到喜欢的人就要认真喜欢 ​​​。你说你长的好看我也就忍了 还偏偏长成我喜欢的样子 你要我怎么办 ，赵吉昌，这就是我对你的感觉。为小宝贝原地360度跳起爱的华尔兹。我是个小无赖呀会一直赖在你心里嗷 。赵吉昌，千山万水就当伏笔 总会遇到姗姗来迟的你 ，你就是我的一切了。赵吉昌，当星河都在变迁，你我却仍天各一边 但请相信，纵使万水千山 日日夜夜我对你的爱与思念从未改变 。不管现在网络多么发达 但是喜欢你这句 我还是想在你耳边对你说 。赵吉昌, 你心情不好时 一定要告诉我 我可不想别人安慰你呐 。']
    draw_text = TextPlotter()
    draw_text.plot(data_text)'''

    '''pic9 = Image.open('picture/9.png').convert(mode='RGB')
    data_picture = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png',pic9]
    draw_picture = ImagePlotter()
    draw_picture.plot(data_picture,3,3)'''

    '''pic9 = imageio.imread('picture/9.png')
    data_gif = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png',pic9]
    draw_gif = GifPlotter()
    draw_gif.plot(data_gif)'''
    
    '''data_video = 'trailer.mp4'
    draw_video = VideoPlotter()
    draw_video.plot(data_video)'''

main()