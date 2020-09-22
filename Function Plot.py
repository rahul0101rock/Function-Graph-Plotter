import matplotlib.pyplot as plt
import numpy as np

inp=input("Enter the Function (In y=mx+c format)\n-> ")
if '+' not in inp:
    c=0
else:
    c=int(inp[inp.index('+')+1:])
if '=x' not in inp:
    m=int(inp[inp.index('=')+1:inp.index('x')])
else:
    m=1
if c==0:
    x=[-10,10]
else:
    x = [-(2*c),2*c]
plt.figure(figsize=(8,8)) 
y = c*np.array(x)+c
plt.plot(x,y,label=inp)
plt.xlim(x) 
plt.ylim(x) 
axis = plt.gca()
plt.plot(axis.get_xlim(),[0,0],'--')
plt.plot([0,0],axis.get_ylim(),'--')
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.title("Function Plot")
plt.grid()
plt.legend()
plt.show()
