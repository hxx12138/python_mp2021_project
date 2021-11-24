class Numbers:
    def __init__(self,start=1,step=1,max=100):
        self._start=start
        self._step=step
        self._max=max
        self._a=self._start
        #self._list=[]

    def __iter__(self):
        
        return self
        #return iter(self._list)

    def __next__(self):
        if self._a <= self._max:
            x = self._a
            self._a += self._step
            return x
        else:
            raise StopIteration('大于max:{}'.format(self._max))

num=Numbers(start=2,step=2,max=100)
#myiter=iter(num)
for x in num:
    print(x)