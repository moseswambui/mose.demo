import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage
imgdir='images'
imgfile='images_me.jpeg'

if len(sys.argv) > 1 :
    imgfile=sys.argv[1]

imgpath=os.path.join(imgdir, imgfile)
root=Tk()
root.title(imgfile)
imgobj=PhotoImage(file=imgpath)
Label(root,image=imgobj).pack()
root.mainloop()
print(imgobj.height(), imgobj.width())