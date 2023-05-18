from tkinter import *


font = 'lucida 30 bold'
bfont = 'lucida 15 bold'


def click(event):
    global scvalue
    text = event.widget.cget("text")
    # print(text)

    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value=eval(scvalue.get())

        scvalue.set(value)
        screen.update()

    elif text == 'C':
        scvalue.set('')
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()



wd = Tk()

wd.geometry("450x600")
wd.title("Calculator By MoStOfA")
# wd.wm_iconbitmap("")    # set icon 

scvalue = StringVar()
scvalue.set("")

screen = Entry(wd, textvar=scvalue, font=font)
screen.pack(fill=X, ipadx=8 , pady=10 , padx= 10)


f = Frame(wd, bg='gray')
b = Button(f,text='7', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='8', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='9', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='C', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(wd, bg='gray')
b = Button(f,text='4', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='5', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='6', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='+', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(wd, bg='gray')
b = Button(f,text='1', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='2', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='3', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='-', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(wd, bg='gray')
b = Button(f,text='/', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='0', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='*', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text='=', padx=15,pady=10,font=bfont)
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f.pack()



wd.mainloop()
