import pathlib
import numpy as np
import math
from pathlib import Path
from PIL import Image
from numpy.core.fromnumeric import shape

# 一. 后项需要前项导出，且无法通过列表推导式生成。
# 例如，时间序列中的“随机游走”便是一种满足上述条件的序列数据。
# 其公式为$$X_t = \mu + X_{t-1} + w_t$$，其中$\mu$为漂移量，
# $w_{t}$是满足某种条件的独立同分布的随机变量，这里假设其服从正态分布N(0, $\sigma^2$)。
# 本题要求写出实现该功能的迭代器函数。具体要求如下：


# 1. 实现random_walk生成器，输入参数$\mu$, $X_0$, $\sigma^2$，$N$，
# 函数将迭代返回N个随机游走生成的变量。

def random_walk(u,X0,sigma_square,N):
    for i in range(N):
        X = X0
        vector = []
        for j in range(10):
            vector.append(X)
            random_value = np.random.normal(0,math.sqrt(sigma_square))
            X = X0 + u + random_value
        yield vector



# 2. 利用zip，实现拼合多个random_walk的生成器，以生成一组时间上对齐的多维随机游走序列。 

def merge_random_walk(generate_vector):
    merge_vector = list(zip(next(generate_vector),next(generate_vector),next(generate_vector),next(generate_vector),next(generate_vector)))
    return merge_vector



# 二. 需要迭代的内容数据量过大，无法一次性加载。
# 例如，在图像相关的深度学习任务中，由于数据总量过大，一次性加载全部数据耗时过长、内存占用过大，
# 因此一般会采用批量加载数据的方法。
#（注：实际应用中由于需要进行采样等操作，通常数据加载类的实现原理更接近字典，
# 例如pytorch中的Dataset类。）
# 现提供文件FaceImages.zip(http://vis-www.cs.umass.edu/fddb/originalPics.tar.gz，
# 其中包含5000余张人脸图片。
# 要求设计FaceDataset类，实现图片数据的加载。具体要求：


# 1. 类接收图片路径列表
# 2. 类支持将一张图片数据以ndarray的形式返回（可以利用PIL库实现）。
# 3. 实现__iter__方法。
# 4. 实现__next__方法，根据类内的图片路径列表，迭代地加载并以ndarray形式返回图片数据。
# 请实现上述生成器和迭代器并进行测试。

class FaceDataset:
    def __init__(self,path):
        path_class = Path(path)
        self.path_generate = path_class.rglob('*')
        self.path_shape()

    def path_shape(self):
        self.path = 0
        while self.path==0:
            path_init = str(next(self.path_generate))
            name = path_init.split('/')[-1]
            if name[0] != '.' and 'jpg' in name:
                self.path = path_init
        print(self.path)
        return self.path

    def image_process(self):
        image = Image.open(self.path)
        image_array = np.array(image)
        print(image_array)
        return image_array
    
    def __iter__(self):
        return self

    def __next__(self):
        self.path = self.path_shape()
        

def main():
    print("hello")
    generate_vector = random_walk(3,10,10,5)
    merge_vector = merge_random_walk(generate_vector)
    print(merge_vector)

    path = '/Users/xihe/Documents/python_mp2021_project/week8_project/originalPics'
    Image_class = FaceDataset(path)
    for i in Image_class:
    #for i in range(1):
        image_array = Image_class.image_process()
        #print(image_array)
    #print(next(Image_class.path_generate))
main()