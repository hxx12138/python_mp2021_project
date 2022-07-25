from tqdm import tqdm
import time
import  pandas as pd
import numpy as  np

alist = list('letters')
bar = tqdm(alist)
for letter in bar:
    bar.set_description("Now get "+str(letter))
    time.sleep(1)

df = pd.DataFrame(np.random.randint(0, 100, (10000000, 60)))
#print(df.shape)
tqdm.pandas(desc="Processing...")
df.progress_apply(lambda x: x**2)