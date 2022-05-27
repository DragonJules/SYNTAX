import sys
import os

from keywords import *

path = sys.argv[1]
name = sys.argv[2]

stxlines = []
pylines = []


with open(path+name+".stx", "r") as file:
    stxlines = file.readlines()

for i in range(len(stxlines)):
    pylines.append("")

for iline in range(len(stxlines)):
    for ikeyword in range(len(stxkeywords)):
        if stxkeywords[ikeyword] in stxlines[iline]:
            vline = stxlines[iline].replace(stxkeywords[ikeyword],pykeywords[ikeyword])
            if pylines[iline]:
                pylines[iline] = pylines[iline].replace(stxkeywords[ikeyword],pykeywords[ikeyword])
            else:
                pylines[iline] = vline
                
    if not any(stxkeyword in stxlines[iline] for stxkeyword in stxkeywords):
        pylines[iline] = stxlines[iline]

with open(path+"generated/"+name+".py", "w") as pyfile:
    for line in pylines:
        pyfile.write(line)

os.system('python '+path+"generated/"+name+".py")