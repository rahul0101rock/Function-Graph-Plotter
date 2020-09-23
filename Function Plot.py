import matplotlib.pyplot as plt
import numpy as np
import regex as re
from math import sqrt,log,modf
# from PIL import Image
inp=input("Enter the Function\n-> ")
inp=inp.lower()
c,ix,iy,last,y=1,0,0,0,[]
if inp.find('^x')>0:c=20
if re.search(r'.[+-]\d$',inp) is not None:
    last=re.findall(r'[+-]\d+$',inp)[0]
    c=int(last[1:])
    if '-' in last:
        ix,iy=c,0
    elif '+' in last:
        ix,iy=0,c
    c=2*c
x=np.linspace(-c,c,10000)
plt.figure(figsize=(8,8)) 
expinp=inp
for s in re.findall(r'\D\d+[x(]\b',inp):
    if s[-1]!="*":
        expinp=expinp.replace(s,'{}{}*{}'.format(s[0],s[1:-1],s[-1]),1)
expinp=expinp.replace('^','**',expinp.count("^"))
if 'log' in inp:
    x = np.arange(0.01, 20.0, 0.01)
    expinp=expinp.replace(expinp[expinp.index("log("):expinp.index(")")+1],'np.exp(-{}/10.0)'.format(expinp[expinp.index("log(")+4:expinp.index(")")]))
else:
    expinp=expinp.replace('x','np.array(x)',expinp.count("x"))

if 'y' in inp and 'x' not in inp:
    num=int(inp[inp.index("=")+1:])
    x,y=[-1,1],[num,num]
    ix,iy=0,num
    plt.xlim([-max(x),max(x)])
    plt.ylim([-abs(max(y)*2),abs(max(y)*2)])
elif 'x' in inp and 'y' not in inp:
    num=int(inp[inp.index("=")+1:])
    x,y=[num,num],[-1,1]
    ix,iy=num,0
    plt.xlim([-abs(max(x)*2),abs(max(x)*2)])
    plt.ylim([-max(y),max(y)])
else:
    exec(expinp)
    plt.plot(x,y,label='$'+inp+'$')
    plt.ylim([-max(y),max(y)]) 
    if '^' in inp:
        plt.xlim([-max(x)*2,max(x)*2])
        ix,iy=0,int(last)
    else:
        plt.xlim([-max(x),max(x)])

plt.plot(ix,iy,'ro')
plt.annotate('  ({},{})'.format(ix,iy), (ix, iy))
axis = plt.gca()
plt.plot(axis.get_xlim(),[0,0],'--')
plt.plot([0,0],axis.get_ylim(),'--')
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.title("Function Plot")
plt.grid()
plt.legend()
plt.show()
# plt.savefig("fnplot.png", dpi=400)
# im = Image.open('fnplot.png').show()
