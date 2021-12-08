from multiprocessing import Queue
from mp_qm import QueueManager
import json
import sys

# 收发队列
task_queue = Queue()
result_queue = Queue()

def get_task():
    return task_queue

def get_result():
    return result_queue

def load_image_urls(filepath):
    image_urls=set()
    with open(filepath) as f:
        for line in f:
            product=json.loads(line.strip())
            for comment in product['comments']:
                image_urls.add(comment['userImageUrl'])
    print('load {} image urls'.format(len(image_urls)))
    return image_urls

def run(ip,port,pwd,url_filepath):
    # 注册, callable 关联Queue
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)
    # 绑定端口和设置验证口令
    manager = QueueManager(address=(ip, port), authkey=pwd.encode())
    # 启动管理，监听信息通道
    manager.start()
    try:
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        # 添加任务
        images=load_image_urls(url_filepath)
        for image in images:
            task.put(image)
            #print(image)
        print('try get result')
        for i in images:
            print(result.get(timeout=100))
    except:
        print('Manager error')
    finally:
        manager.shutdown()

if __name__ == '__main__':
    ip='127.0.0.1'
    port=int(sys.argv[1])
    pwd='admin'
    filepath='./305262.json'
    run(ip,port,pwd,filepath)