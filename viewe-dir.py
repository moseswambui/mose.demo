import os,sys
from tkinter import *
from PIL.ImageTk import PhotoImage

imgdir = 'images'
if len(sys.argv)>1:
    imgdir=sys.argv[1]

imgfiles= os.listdir(imgdir)
main = Tk()
main.title(imgdir)
quit=Button(main, text='Quit', command=main.quit, font=('courier',55))
quit.pack()
savephotos=[]
for imgfile in imgfiles:
    imgpath=os.path.join(imgdir, imgfile)
    win=Toplevel()
    win.title(imgfile)

    try:
        imgobj=PhotoImage(imgpath)
        Label(win, image=imgobj).pack()
        print(imgpath, imgobj.height(), imgobj.width())
        savephotos.append(imgobj)

    except:
        errmesg='skipping %s\n%s' %(imgfile, sys.exc_info()[1])
        Label(win, text=errmesg).pack()

main.mainloop()