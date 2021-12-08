import concurrent.futures
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

URLS = ['http://www.buaa.edu.cn',
        'https://www.163.com',
        'https://www.baidu.com',
        'https://www.qq.com',
        'https://www.cnbeta.com',
        'https://www.bilibili.com',
        'https://www.mi.com']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    fs = [executor.submit(load_url, url, 60) for url in URLS]
    for url, future in zip(URLS, concurrent.futures.as_completed(fs)):
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d KB' % (url, (len(data)//8)//1024))