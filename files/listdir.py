import os
totalsize=0
for name in os.listdir('/home/Python/'):
    totalsize=totalsize+os.path.getsize(os.path.join('/home/Python/',name))
    print(totalsize)
