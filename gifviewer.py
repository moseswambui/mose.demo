import os, sys
from tkinter import *

imgdir='images'
imgfile='Lava_Burst.gif'

if len(sys.argv)>1:
    imgfile=sys.argv[1]
imgpath=os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)
Label(win, image=imgobj)
print(imgobj.height(), imgobj.width())
win.mainloop()