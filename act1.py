import numpy as np
d_t=[('name','S100'),('grade',int),('rn',int)]
sdetail=[('kauhsik',8,7),('jhayesh',8,6),('ashvith',8,10)]

st=np.array(sdetail,dtype=d_t)
print ('orginal array:')

print (st)

print("sort by name:")

print(np.sort(st,order='name'))




