import concurrent.futures
from multiprocessing import current_process
import math

PRIMES = [
    1112272535095293,
    1112582705942171,
    1112272535095291,
    1115280095190773,
    1115797848077099,
    11099726899285419]

def is_prime(n):
    print(f"{current_process().pid}")
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main_submit():
    results=[]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number in PRIMES:
            n_future=executor.submit(is_prime,number)
            #print(n_future.result())#block
            results.append(n_future)
            #这里要注意，如果马上在主进程里获取结果，即n_future.result()，即主进程会阻塞，无法并行
            #因此建议先将n_future搁进list,等启动所有进程后再获取结果。
        for number, res in zip(PRIMES,results):
            print("%d is prime: %s" % (number,res.result()))

def main_map():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime_or_not in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime_or_not))

if __name__ == '__main__':
    main_submit()
    #main_map()
    