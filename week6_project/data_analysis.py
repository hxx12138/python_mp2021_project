from typing import Text
import pandas as pd
import os
from matplotlib import pyplot as plt
import numpy as np

#windows 中文字显示问题
#plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#mac 中文字显示问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

#file_path = 'E:\何熙1908\大三上课程\现代程序设计\第六次作业\co2_demo\'

class Data_analyze:
    #  至少实现一个数据分析类，以提供数据的读取及基本的时间
    # （如某区域某类型排放随时间的变化）和空间分析（某一年全国排放的空间分布态势）方法。
    def __init__(self,path_list):
        self.df_list = []
        self.time_list = []
        for i in path_list:
            df = pd.read_excel('co2_demo/'+i,sheet_name=None)
            self.time_list.append(i[-9:-5])
            self.df_list.append(df)
        self.province_list = list(self.df_list[0]['Sum'][self.df_list[0]['Sum'].columns[0]])[0:-2]


    def time_analyze(self,province,co2_type):
        self.time_data_list = []
        for i in self.df_list:
            df_time = i['Sum']
            #print(df_time)
            province_list = list(df_time[df_time.columns[0]])
            #print(nation)
            data = df_time.loc[province_list.index(province),co2_type]
            #print(data)
            self.time_data_list.append(data)

        print(f'省份：{province}  碳排放量类型：{co2_type}')
        for i in range(len(self.time_list)):
            print(f'年份：{self.time_list[i]}  排放量：{self.time_data_list[i]}')

        return self.time_data_list


    def space_analyze(self,year,co2_type):
        df_space = self.df_list[self.time_list.index(year)]['Sum']
        #print(df_space)
        self.space_data_list = []
        province_list = list(df_space[df_space.columns[0]])
        for i in range(len(province_list)):
            data = df_space.loc[i, co2_type]
            self.space_data_list.append(data)

        print(f'年份：{year}  碳排放量类型：{co2_type}')
        for i in range(0,len(province_list)-2):
            print(f'省份：{province_list[i]}  排放量：{self.space_data_list[i]}')
        print(f'总计：{province_list[len(province_list)-1]}  排放量：{self.space_data_list[len(province_list)-1]}')

        return self.space_data_list[0:-2]

#至少实现一个数据可视化类，以提供上述时空分析结果的可视化，如以曲线、饼等形式对结果进行呈现。
class Data_view(Data_analyze):
    def __init__(self,path_list):
        Data_analyze.__init__(self,path_list)

    def time_view(self):
        time_list = self.time_list
        time_data_list = self.time_analyze('Beijing','Total')
        #print(time_data_list)
        plt.figure(figsize=(20,6.5))
        plt.bar(range(len(time_list)),time_data_list,tick_label = time_list,color = 'violet')
        plt.xlabel('年份')
        plt.ylabel('Beijing Co2 排放量')
        plt.show()

    def space_view(self):
        province_list = self.province_list
        space_data_list = np.array(self.space_analyze('1997','Total'))
        plt.pie(space_data_list,
                labels=province_list,
                autopct='%.2f%%'
                )
        plt.title("Beijing Co2 排放量 总体占比情况")
        plt.show()

# 由于数据中包含空值等异常值，在进行数据分析以及可视化前需要检查数据。因此需要实现NotNumError类，
# 继承ValueError，并加入新属性year，province，industry，type，对数据进行检测，若取到的一列数据中包含nan，则抛出该异常，
# 并提供异常相关的年份，省份，工业和排放类型等信息。
# 在此基础上，利用try except捕获该异常，打印异常信息，并对应位置的数据进行适当的填充。

class NotnumError(ValueError):
    def __init__(self,year,province,industry,type):
        self.year = year
        self.province = province
        self.industry = industry
        self.type = type
        self.message = f"the data of{province} in {year} has nan "

class NotnumberTest(Data_analyze):
    def __init__(self,path_list):
        Data_analyze.__init__(self,path_list)
        
    def read_data(self):
        doc_list = self.df_list
        year_list = self.time_list
        province_list = self.province_list
        for y in range(len(doc_list)):
            self._year = year_list[y]
            for sheet in doc_list[y]:
                if sheet != 'Sum':
                    self._province = sheet
                    df_temp = doc_list[y][sheet]
                    row_index = list(df_temp[df_temp.columns[0]])
                    col_index = list(df_temp.columns)
                    values = df_temp.values
                    
                    print(sheet)
                    break
            break
        '''
        self._industry = industry
        self._type = type'''

        print(len(doc_list))
    

# 4. 由于部分省份排放总量数据为0，要求在计算比例时进行检验，若检验发现总量为0，
# 则抛出ZeroDivisionError，并打印对应的行名等信息。


# 5. （附加）按时间分析时，注意观察不同区域随时间排放量的变化，
# 是否存在一些明显的趋势，以及趋势的空间差异，并思考这些趋势及差异的管理意义与政策启发。

def main():
    path_list = os.listdir('co2_demo')
    path_list = sorted(path_list)
    #print(path_list)

    #Data = Data_analyze(path_list)


    #Data.time_analyze('Beijing','Total')
    #print(Data.time_list)
    #print(Data.df_list)


    #Data.space_analyze('1997','Total')


    #Data_draw = Data_view(path_list)

    #ata_draw.time_view()
    #Data_draw.space_view()

    Text = NotnumberTest(path_list)
    Text.read_data()

main()