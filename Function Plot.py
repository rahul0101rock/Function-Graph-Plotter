import matplotlib.pyplot as plt
import numpy as np
inp=input("Enter the Function: ")
if '+' not in inp:
    b=0
else:
    b=int(inp[inp.index('+')+1:])
if '=x' not in inp:
    m=int(inp[inp.index('=')+1:inp.index('x')])
else:
    m=1
x = [-(2*b),2*b]
plt.figure(figsize=(7,7)) 
y = m*np.array(x)+b
plt.plot(x,y,label=inp)
plt.xlim(x) 
plt.ylim(x) 
axis = plt.gca()
plt.plot(axis.get_xlim(),[0,0],'--')
plt.plot([0,0],axis.get_ylim(),'--')
plt.ylabel('Y')
plt.xlabel('X')
plt.title("Function Plot")
plt.grid()
plt.legend()
plt.show()
