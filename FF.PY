import tkinter as tk
import random as r
h=[]

def captcha():
    global h
    c.delete("all")
    h = []
    q = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in range(5):
        x =r.randint(0,len(q)-1)
        h.append(q[x])

    color = ["black", "red", "yellow", "blue", "brown", "grey", "pink", "cyan"]
    font = ['lucida', 'verdana', 'helvetica', 'papyrus', 'Arial', 'calibri']

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
        label2 = tk.Label(root, text="   CAPTCHA EMPTY   ")
        label2.place(x=80, y=300)
        return

    if(len(st.get())==0):
        label2 = tk.Label(root, text="    INPUT EMPTY   ")
        label2.place(x=80, y=300)
        return

    s = ''
    for i in h:
        s+=i

    if(st.get() == s):
        label = tk.Label(root, text="             YES             ")
    else:
        label = tk.Label(root, text="             NO              ")

    label.place(x=80, y=300)

root = tk.Tk()

# window size
root.geometry("300x400")

# window background color
root.configure(background="#808080")
st = tk.StringVar();

c = tk.Canvas(root, width=280, height=100, bg="white")
b = tk.Button(root, text="Captcha", width=15, font="Helvetica 13", command=captcha)
t = tk.Entry(root,textvariable=st)
bt = tk.Button(root, text="Check", width=15, font="Helvetica 13", command=check)

b.place(x=80, y=120)
c.place(x=10, y=10)
t.place(x=90, y=200)
bt.place(x=80, y=250)

root.mainloop()