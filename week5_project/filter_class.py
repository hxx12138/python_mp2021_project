from PIL import Image
from PIL import ImageFilter
from matplotlib import pyplot as plt

class Filter:
    # 实现基类Filter，至少包括两个数据属性，一个属性是待处理的图片实例，即PIL库的Image实例，
    # 另一个是参数列表，用以存储可能使用参数的滤波器的参数；至少包括一个方法属性，即filter()方法，
    # 能够对Image实例的特定处理。但在该类中并不需要进行实现，其实现细节应该交给子类。
    def __init__(self,path):
        self.image = Image.open(path).convert(mode='RGB')
        self.path = path
        self.plist = []
    def filter(self,image):
        return image

# 实现Filter类的多个子类，分别实现对图片的一些滤波处理，至少应进行边缘提取，锐化，模糊及大小调整四类操作，
# 也即应实现至少4个子类，分别对基类中的filter()方法进行实现。注意，并不需要真正实现对应的操作，
# 可简单地通过PIL中的Image和ImageFilter模块来实现。

class FIND_EDGES_Filter(Filter):
    def __init__(self,path):
        Filter.__init__(self,path)
    def filter(self,image):
        image_filter = self.image.filter(ImageFilter.FIND_EDGES)
        return image_filter

class EDGE_ENHANCE_Filter(Filter):
    def __init__(self,path):
        Filter.__init__(self,path)
    def filter(self,image):
        image_filter = self.image.filter(ImageFilter.EDGE_ENHANCE)
        return image_filter

class GaussianBlur_Filter(Filter):
    def __init__(self,path):
        Filter.__init__(self,path)
    def filter(self,image):
        image_filter = self.image.filter(ImageFilter.GaussianBlur)
        return image_filter

class new_Filter(Filter):
    def __init__(self,path,w_rate,h_rate):
        Filter.__init__(self,path)
        self.w_rate = w_rate
        self.h_rate = h_rate
    def filter(self,image):
        w,h = self.image.size
        #print(w,h)
        image_filter = self.image.resize((int(w*self.w_rate),int(h*self.h_rate)))
        return image_filter

# 实现类ImageShop，其至少包含四个数据属性，分别是图片格式，图片文件（应该支持目录），存储图片实例(Image实例)的列表以及存储处理过的图片（如果需要的话）
# 。至少包含如下方法属性，分别是从路径加载特定格式的图片（load_images()，应加载文件或目录中的所有特定格式图片）；
# 处理图片的内部方法__batch_ps(Filter),利有某个过滤器对所有图片进行处理；
# 批量处理图片的对外公开方法（batch_ps()），注意该方法要至少有一个操作参数，
# 且该参数可以不定长，即可以同时进行若干操作（如调整大小并模糊等），其参数可定义成一种特定格式的tuple输入，比如（操作名，参数），
# 根据操作名生成对应的Filter子类并调用 __batch_ps来完成批处理；处理效果显示（display（））
# ，注意该方法应该有参数，如考虑多图片呈现可能需要行，列以及每张图片的大小，以及最多显示多少张等，可
# 通过matplotlib中的subplot等来实现；处理结果输出（save()），该方法应该有输出路径或输出格式等参数。

class ImageShop(Filter):
    def __init__(self,path,formation,path_list,Image_list,Image_process):
        Filter.__init__(self, path)
        self.formation = formation
        self.path_list = path_list
        self.Image_list = Image_list
        self.Image_process = Image_process

    def load_images(self,path):
        for i in self.path_list:
            if 'png' in i.split('.'):
                Image_temp = Filter(i)
                self.Image_list.append(Image_temp)

    def __batch_ps(self):
        for i in self.Image_list:
            Image_p = FIND_EDGES_Filter(self.path)
            Image_p = Image_p.filter(i)
            self.Image_process.append(Image_p)

    def batch_ps(self,w_rate,h_rate,*args):
        for i in range(len(self.Image_list)):
            if args[0] == '1':
                Image_t = FIND_EDGES_Filter(self.path_list[i])
                Image_t = Image_t.filter(Image_list[i])
                self.Image_process.append(Image_t)
            if args[0] == '2':
                Image_t = EDGE_ENHANCE_Filter(self.path_list[i])
                Image_t = Image_t.filter(Image_list[i])
                self.Image_process.append(Image_t)
            if args[0] == '3':
                Image_t = GaussianBlur_Filter(self.path_list[i])
                Image_t = Image_t.filter(Image_list[i])
                self.Image_process.append(Image_t)
            if args[0] == '4':
                Image_t = new_Filter(self.path_list[i],w_rate,h_rate)
                Image_t = Image_t.filter(Image_list[i])
                self.Image_process.append(Image_t)

    def display(self,row,col):
        num = len(self.Image_process)
        for i in range(num):
            plt.subplot(row,col,i+1)
            plt.imshow(self.Image_process[i])
        plt.show()

    def save(self,path,formation):
        for i in range(len(self.Image_process)):
            self.Image_process[i].save(path+str(i+1)+'p'+'.'+formation)

# 实现测试类TestImageShop，对该类进行测试，指定图片路径，指定要进行的操作（如有参数也可应提供），并对执行结果进行呈现和存储。

class TestImageShop:
    def __init__(self,path_list):
        self.path_list = path_list

    def text_imageshop(self,formation,path_list,Image_list,Image_process):
        ImageShop_init = ImageShop(path,formation,self.path_list,Image_list,Image_process)
        ImageShop_init.load_images(path)
        print(Image_list)
        ImageShop_init.batch_ps(0.5,0.5,'1','png')
        print(Image_process)
        ImageShop_init.display(3,3)
        ImageShop_init.save('/Volumes/HIKVISION/何熙1908/大三上课程/现代程序设计/第五次作业/','png')

path = '3.png'
path_list = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png']
formation = 'png'
Image_list = []
Image_process = []

text_class = TestImageShop(path_list)
text_class.text_imageshop(formation,path_list,Image_list,Image_process)
# 5. 附加：观察一些经过过滤后图片的变化，思考这些处理对图片本身的一些相关的计算，如图片的相似性等有无影响，并进行简单的实验验证。
# 6. 附加：进一步了解深度卷积网络及其在计算机视觉中的应用现状。