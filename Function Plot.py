import matplotlib.pyplot as plt
import numpy as np
import regex as re
from PIL import Image

inp=input("Enter the Function\n-> ")
inp=inp.lower()
c=1
ix,iy=0,0
if inp.find('^x')>0:c=20
if inp[-1]!='x':
    last=re.findall(r'\D\d+$',inp)[0]
    c=int(last[1:])
    if '-' in last:
        ix,iy=c,0
    elif '+' in last:
        ix,iy=0,c
    c=2*c
x=np.linspace(-c,c,10000)
plt.figure(figsize=(8,8)) 
expinp=inp
y=[]
expinp=expinp.replace('^','**',expinp.count("^"))
for s in re.findall(r'\D\d+\D',inp):
    if s[-1]!="*":
        expinp=expinp.replace(s,'{}{}*{}'.format(s[0],s[1:-1],s[-1]),1)
expinp=expinp.replace('x','np.array(x)',expinp.count("x"))
exec(expinp)
plt.plot(x,y,label=inp)

if '^' in inp:
    plt.xlim([-max(x)*2,max(x)*2])
    ix,iy=0,int(last)
else:
    plt.xlim([-max(x),max(x)]) 
plt.ylim([-max(y),max(y)]) 
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
# plt.savefig("fnplot.png",bbox_inches='tight')
# im = Image.open('fnplot.png').show()
