import os, sys
from tkinter import *

imgdir = 'images'
imgfile ='motion-david-szakaly-01.gif'

if len(sys.argv) > 1:
    imgfile= sys.argv[1]

imgpath= os.path.join(imgdir,imgfile )
win=Tk()
win.title(imgfile)
imgobj= PhotoImage(file=imgpath)
Label(win, image=imgobj).pack()
print(imgobj.width(), imgobj.height())
win.mainloop()


