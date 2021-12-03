from multiprocessing import Pool,Process

def f(x):
    return x*x

def f(name):
    print('hello', name)

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

    p = Process(target=f, args=('bob',))
    p.start()
    p.join()