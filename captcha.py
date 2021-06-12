import tkinter
import random as r
from PIL import ImageTk,Image

h=[]

def captcha():
    global h
    c.delete("all")

    h = []
    q = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(5):
        x =r.randint(0,len(q)-1)
        h.append(q[x])

    color = ["black", "red", "yellow", "blue", "brown", "grey", "pink", "cyan"]
    font = ['lucida', 'verdana', 'helvetica', 'papyrus', 'Arial', 'calibri']

    x = r.randint(1,4)

    img = Image.open(str(x)+'.jpg')
    img = img.resize((650, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    c.create_image(0,0,image=img)
    l = tkinter.Label(root,image=img)
    l.photo = img
   # l.place(x=10,y=10)

    t1 = c.create_text(40+r.randint(0, 10), 40+r.randint(0, 10), text=h[0], font=font[r.randint(0, 5)]+" 28 bold", fill=color[r.randint(0, 7)])
    t2 = c.create_text(80+r.randint(0, 10), 40+r.randint(0, 10), text=h[1], font=font[r.randint(0, 5)]+" 28 bold", fill=color[r.randint(0, 7)])
    t3 = c.create_text(120+r.randint(0, 10), 40+r.randint(0, 10), text=h[2], font=font[r.randint(0, 5)]+" 28 bold", fill=color[r.randint(0, 7)])
    t4 = c.create_text(160+r.randint(0, 10), 40+r.randint(0, 10), text=h[3], font=font[r.randint(0, 5)]+" 28 bold", fill=color[r.randint(0, 7)])
    t5 = c.create_text(200+r.randint(0, 10), 40+r.randint(0, 10), text=h[4], font=font[r.randint(0, 5)]+" 28 bold", fill=color[r.randint(0, 7)])

    for i in range(0, 5):
        lines = c.create_line(r.randint(5, 295), r.randint(5, 195), r.randint(5, 295), r.randint(5, 195), fill=color[r.randint(0, 6)], width=r.randint(1, 3))

def check():
    global label2

    if (len(h) == 0):
        label2 = tkinter.Label(root, text="   CAPTCHA EMPTY   ")
        label2.place(x=80, y=300)
        return

    if(len(st.get())==0):
        label2 = tkinter.Label(root, text="    INPUT EMPTY     ")
        label2.place(x=80, y=300)
        return

    s = ''
    for i in h:
        s+=i

    if(st.get() == s):
        label = tkinter.Label(root, text="             YES MATCHED            ")
    else:
        label = tkinter.Label(root, text="             NOT  MATCHED            ")

    label.place(x=80, y=300)

root = tkinter.Tk()

# window size
root.geometry("300x400")

# window background color
root.configure(background="#208080")
st = tkinter.StringVar();

c = tkinter.Canvas(root, width=280, height=100, bg="white")
b = tkinter.Button(root, text="Captcha", width=15, font="Helvetica 13", command=captcha)
t = tkinter.Entry(root,textvariable=st)
bt = tkinter.Button(root, text="Check", width=15, font="Helvetica 13", command=check)


b.place(x=80, y=120)
c.place(x=10, y=10)
t.place(x=90, y=200)
bt.place(x=80, y=250)

root.mainloop()