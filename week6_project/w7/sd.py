import copy

l1=list(range(0,10))
l1_c=l1
l1_c=l1[:]
l1_c=l1.copy()
l1_c=copy.copy(l1)
l1_c=copy.deepcopy(l1)
l1_c[0],l1_c[-1]=-1,-9
print(l1)
print(l1_c)
 
l2=list(list(range(0,i)) for i in range(1,5))
#l2_c=l2[:]
#l2_c=l2.copy()
#l2_c=copy.copy(l2)
#l2_c=copy.deepcopy(l2)
#l2_c[0][0],l2_c[-1][-1]=-1,-3
#print(l2)
#print(l2_c)