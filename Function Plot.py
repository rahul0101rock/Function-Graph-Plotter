import matplotlib.pyplot as plt
import numpy as np
import regex as re

inp=input("Enter the Function\n-> ")
inp=inp.lower()
c=1
point=0
if inp.find('+')>0:
    if 'x' not in inp[inp.rindex('+'):]:
        c=int(inp[inp.rindex('+'):])
        point=c
x=np.linspace(-c,c,10000)
plt.figure(figsize=(8,8)) 
expinp=inp
y=[]
expinp=expinp.replace('^','**',expinp.count("^"))
for s in re.findall(r'\D\d+\D',inp):
    expinp=expinp.replace(s,'{}{}*{}'.format(s[0],s[1:-1],s[-1]),1)
expinp=expinp.replace('x','np.array(x)',expinp.count("x"))
exec(expinp)
plt.plot(x,y,label=inp)
plt.plot(0,point,'ro')
plt.annotate('  (0,{})'.format(point), (0, point))
if '^' in inp:
    plt.xlim([-max(x)*2,max(x)*2]) 
else:
    plt.xlim([-max(x),max(x)]) 
plt.ylim([-max(y),max(y)]) 
axis = plt.gca()
plt.plot(axis.get_xlim(),[0,0],'--')
plt.plot([0,0],axis.get_ylim(),'--')
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.title("Function Plot")
plt.grid()
plt.legend()
plt.show()
