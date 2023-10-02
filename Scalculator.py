from tkinter import *

root = Tk()
# ----------------------------------------------------------------------------------------------------------------------
# main window settings
titlever = "S CALC"
root.geometry("390x545")
root.minsize(390, 545)
root.maxsize(390, 550)
root.title(titlever)
root.configure(bg="light yellow")
showcommands = False  # set to true to see all events in the console window
# ----------------------------------------------------------------------------------------------------------------------
# other attributes settings
bgcl = "light yellow"
btcl = "orange"
fgcl = "black"
ftst = "comisanms 15 bold"
ftst2 = "comisanms 12"
btst1f = FLAT
btst2s = GROOVE
bfont = "comisanms 26 bold"
# ----------------------------------------------------------------------------------------------------------------------
# functions of app main logic
dver = " "  # it is screen variable
themesel = True


def updatel1():
    if themesel is True:
        l1.configure(text=titlever, fg="black")
    else:
        l1.configure(text=titlever, fg="white")


def themechange():  # function for theme change
    # shivraj singh amritsar campus 2023693
    global themesel, btcl, bgcl, fgcl
    if themesel is True:  # DARK THEME
        root.configure(bg="black")
        btcl = "black"
        bgcl = "black"
        fgcl = "white"
        # frames
        topbar.configure(bg=bgcl)
        display.configure(bg="black", fg="white")
        f789add.configure(bg=bgcl)
        f456sub.configure(bg=bgcl)
        f123mul.configure(bg=bgcl)
        fdev_0_dot_eval.configure(bg=bgcl)
        statusbar.configure(bg=bgcl)
        # labels
        l1.configure(bg=bgcl, fg=fgcl)

        # buttons
        # topbar
        b1th.configure(
            bg=bgcl, text="☀", fg=fgcl, activebackground=bgcl, activeforeground="white"
        )
        b2th.configure(
            bg=bgcl, font=ftst, activebackground=bgcl, activeforeground="red"
        )
        about1.configure(
            bg=bgcl, fg="lime", activebackground=bgcl, activeforeground="white"
        )

        # calculator main
        cls0 = "grey"
        cl1 = "light blue"
        b7.configure(bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground=cl1)
        b8.configure(bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground=cl1)
        b9.configure(bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground=cl1)
        badd.configure(
            bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground="orange"
        )
        b4.configure(bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground=cl1)
        b5.configure(bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground=cl1)
        b6.configure(bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground=cl1)
        bsub.configure(
            bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground="orange"
        )
        b1.configure(bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground=cl1)
        b2.configure(bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground=cl1)
        # shivraj singh amritsar campus 2023693
        b3.configure(bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground=cl1)
        bmul.configure(
            bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground="orange"
        )
        bdev.configure(
            bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground="orange"
        )
        b0.configure(bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground=cl1)
        bdot.configure(
            bg=bgcl, fg=fgcl, activebackground=cls0, activeforeground="orange"
        )
        bequl.configure(bg=bgcl, activebackground="grey", activeforeground="orange")

        # statusbar
        lS1.configure(bg=bgcl, fg=fgcl)
        bs1th.configure(
            bg=bgcl, fg="yellow", activebackground=bgcl, activeforeground="white"
        )
        themesel = False
        l1.configure(text="DARK THEME")
    else:  # DEFAULT THEME
        root.configure(bg="light yellow")
        btcl = "light yellow"
        bgcl = "light yellow"
        fgcl = "black"
        # frames
        topbar.configure(bg=bgcl)
        display.configure(bg="white", fg="black")
        f789add.configure(bg=bgcl)
        f456sub.configure(bg=bgcl)
        f123mul.configure(bg=bgcl)
        fdev_0_dot_eval.configure(bg=bgcl)
        statusbar.configure(bg=bgcl)
        # labels
        l1.configure(bg=bgcl, fg=fgcl)
        # buttons
        # topbar
        b1th.configure(
            bg=bgcl, text="🌛", fg=fgcl, activebackground=bgcl, activeforeground="black"
        )
        b2th.configure(
            bg=bgcl, font=ftst2, activebackground=bgcl, activeforeground="red"
        )
        about1.configure(
            bg=bgcl, fg="black", activebackground=bgcl, activeforeground="orange"
        )
        # calculator main
        cls00 = "#fffac7"
        cl11 = "black"
        b7.configure(bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground=cl11)
        # shivraj singh amritsar campus 2023693
        b8.configure(bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground=cl11)
        b9.configure(bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground=cl11)
        badd.configure(
            bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground="green"
        )
        b4.configure(bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground=cl11)
        b5.configure(bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground=cl11)
        b6.configure(bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground=cl11)
        bsub.configure(
            bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground="green"
        )
        b1.configure(bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground=cl11)
        b2.configure(bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground=cl11)
        b3.configure(bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground=cl11)
        bmul.configure(
            bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground="green"
        )
        bdev.configure(
            bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground="green"
        )
        b0.configure(bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground=cl11)
        bdot.configure(
            bg=bgcl, fg=fgcl, activebackground=cls00, activeforeground="green"
        )
        bequl.configure(bg=bgcl, activebackground=cls00, activeforeground="lime")
        # statusbar
        lS1.configure(bg=bgcl, fg=fgcl)
        bs1th.configure(
            bg=bgcl, fg="black", activebackground=bgcl, activeforeground="orange"
        )
        themesel = True
        l1.configure(text="LIGHT THEME")
    if showcommands is True:
        if themesel is False:
            print(f"DONE theme applied dark ")
        else:
            print(f"DONE theme applied light")

    root.after(4000, updatel1)


previousdata = " "
temp = StringVar()


# shivraj singh amritsar campus 2023693
def inp(ver):  # screen heandling
    global previousdata, temp
    ver = str(ver)
    previousdata = display.get()  # INSERT PREVIOUS DATA FROM DISPLAY
    temp = previousdata + ver  # SAVE PREVIOUS DATA AND INPUT IN THE TEMP VARIABLE
    display.delete(0, 100)  # CLEAR PREVIOUS SCREEN
    display.insert(0, temp)  # INSERT THE TEMP SAVED DATA IN THE SCREEN
    if showcommands is True:
        print("DONE you enter ", ver)


temp2 = StringVar()
result = " "


def resulting():
    global temp2, reentery, result
    temp2 = display.get()
    if temp2 == "":
        l1.configure(text=" NO EXPRESSION ", fg="red")
        root.after(3000, updatel1)
        if showcommands is True:
            print("HAVE NOT ANY ENTRY IN THE CONSOLE OR DISPLAY")
    else:
        try:  # error handled 26-11-2021
            result = eval(temp2)
        except SyntaxError:
            l1.configure(text="WRONG EXPRESSION !", fg="red")
            result = ""
        root.after(4500, updatel1)
        result = str(result)
        display.delete(0, 100)
        display.insert(0, result)
        lS1.configure(text=result)
        reentery = result
        if showcommands is True:
            print("DONE YOUR ANSWER IS ", result)


reentery = " "


def reenter():
    global reentery
    if reentery == " ":  # if reentery is empty
        if themesel is True:
            l1.configure(text=" EMPTY HISTORY ", fg="blue")
        else:
            # shivraj singh amritsar campus 2023693
            l1.configure(text=" EMPTY HISTORY ", fg="yellow")
        if showcommands is True:
            print("reenter variable is empty")
        root.after(3000, updatel1)
    else:  # if it has some values
        if showcommands is True:
            print("reentery is done ", reentery)
        reentery = display.get() + reentery
        display.delete(0, 100)
        display.insert(0, reentery)


def cls():
    global dver, result, reentery
    dver = " "
    result = " "
    reentery = " "
    display.delete(0, 50)
    lS1.configure(text=" ")
    l1.configure(text="CLEAR DONE", fg="lime")
    if showcommands is True:
        print("DONE clear screen")
    root.after(2000, updatel1)


def aboutt():
    l1.configure(text="BY SHIVRAJ SINGH", fg="orange")
    root.after(3000, updatel1)


# ----------------------------------------------------------------------------------------------------------------------
# top bar elements
topbar = Frame(root, bg=bgcl, pady=2, padx=2)
topbar.pack(fill=X)
b1th = Button(
    topbar,
    bg=bgcl,
    font=ftst,
    text="🌛",
    border=3,
    relief=btst1f,
    command=themechange,
    activebackground=bgcl,
    activeforeground="black",
)
b1th.pack(side=LEFT)
l1 = Label(topbar, bg=bgcl, font=ftst, text=titlever, pady=2)
l1.pack(side=LEFT, pady=2, padx=2)
# shivraj singh amritsar campus 2023693
b2th = Button(
    topbar,
    bg=bgcl,
    font=ftst2,
    text="CLS ALL",
    fg="red",
    border=3,
    relief=btst1f,
    activebackground=bgcl,
    activeforeground="red",
    command=cls,
)
b2th.pack(side=RIGHT)
about1 = Button(
    topbar,
    bg=bgcl,
    fg="black",
    font="comisanms 14",
    text="?",
    activebackground=bgcl,
    activeforeground="orange",
    command=aboutt,
    bd=0,
)
about1.pack(side=RIGHT, padx=6)
# ----------------------------------------------------------------------------------------------------------------------
# main interface of calculator
# padding control
x = 13
y = 4
ex = 10
ey = 3
fy = 3.5
# display of the calculator
# noinspection PyTypeChecker
display = Entry(
    root,
    textvariable=dver,
    bg="WHITE",
    font="comisanms 25 ",
    justify=RIGHT,
    bd=8,
    relief=SUNKEN,
)
display.pack(side=TOP)
# BUTTONS FOR 7 8 9 AND + ............................................
cldef = "#fffac7"
cl1def = "black"
f789add = Frame(root, bg=bgcl, pady=2, padx=2)
f789add.pack(pady=fy)
b7 = Button(
    f789add,
    bg=bgcl,
    font=bfont,
    text="7",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    activeforeground=cl1def,
    command=lambda: inp(7),
)
b7.pack(side=LEFT, padx=ex, pady=ey)
b8 = Button(
    f789add,
    bg=bgcl,
    font=bfont,
    text="8",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    activeforeground=cl1def,
    command=lambda: inp(8),
)
b8.pack(side=LEFT, padx=ex, pady=ey)
b9 = Button(
    f789add,
    bg=bgcl,
    font=bfont,
    text="9",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    # shivraj singh amritsar campus 2023693
    activeforeground=cl1def,
    command=lambda: inp(9),
)
b9.pack(side=LEFT, padx=ex, pady=ey)
badd = Button(
    f789add,
    bg=bgcl,
    font=bfont,
    text="+",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    activeforeground="green",
    command=lambda: inp("+"),
)
badd.pack(side=LEFT, padx=ex, pady=ey)
# BUTTONS FOR 4 5 6 AND - ............................................
f456sub = Frame(root, bg=bgcl, pady=2, padx=2)
f456sub.pack(pady=fy)
b4 = Button(
    f456sub,
    bg=bgcl,
    font=bfont,
    text="4",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    activeforeground=cl1def,
    command=lambda: inp(4),
)
b4.pack(side=LEFT, padx=ex, pady=ey)
b5 = Button(
    f456sub,
    bg=bgcl,
    font=bfont,
    text="5",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    activeforeground=cl1def,
    command=lambda: inp(5),
)
b5.pack(side=LEFT, padx=ex, pady=ey)
b6 = Button(
    f456sub,
    bg=bgcl,
    font=bfont,
    text="6",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    activeforeground=cl1def,
    command=lambda: inp(6),
)
b6.pack(side=LEFT, padx=ex, pady=ey)
bsub = Button(
    f456sub,
    bg=bgcl,
    font=bfont,
    text="-",
    border=3,
    relief=btst2s,
    padx=16.5,
    pady=y,
    activebackground=cldef,
    activeforeground="green",
    command=lambda: inp("-"),
)
bsub.pack(side=LEFT, padx=ex, pady=ey)
# BUTTONS FOR 1 2 3 AND * ............................................
f123mul = Frame(root, bg=bgcl, pady=2, padx=2)
f123mul.pack(pady=fy)
b1 = Button(
    f123mul,
    bg=bgcl,
    font=bfont,
    text="1",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    activeforeground=cl1def,
    command=lambda: inp(1),
)
b1.pack(side=LEFT, padx=ex, pady=ey)
b2 = Button(
    f123mul,
    bg=bgcl,
    font=bfont,
    text="2",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    activeforeground=cl1def,
    command=lambda: inp(2),
)
b2.pack(side=LEFT, padx=ex, pady=ey)
b3 = Button(
    f123mul,
    bg=bgcl,
    font=bfont,
    text="3",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    # shivraj singh amritsar campus 2023693
    activeforeground=cl1def,
    command=lambda: inp(3),
)
b3.pack(side=LEFT, padx=ex, pady=ey)
bmul = Button(
    f123mul,
    bg=bgcl,
    font=bfont,
    text="*",
    border=3,
    relief=btst2s,
    padx=16,
    pady=y,
    activebackground=cldef,
    activeforeground="green",
    command=lambda: inp("*"),
)
bmul.pack(side=LEFT, padx=ex, pady=ey)
# BUTTONS FOR / 0 . AND equl ............................................
fdev_0_dot_eval = Frame(root, bg=bgcl, pady=2, padx=2)
fdev_0_dot_eval.pack(pady=fy)
bdev = Button(
    fdev_0_dot_eval,
    bg=bgcl,
    font=bfont,
    text="/",
    border=3,
    relief=btst2s,
    padx=16.5,
    pady=y,
    activebackground=cldef,
    activeforeground="green",
    command=lambda: inp("/"),
)
bdev.pack(side=LEFT, padx=ex, pady=ey)
b0 = Button(
    fdev_0_dot_eval,
    bg=bgcl,
    font=bfont,
    text="0",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    activeforeground=cl1def,
    command=lambda: inp(0),
)
b0.pack(side=LEFT, padx=ex, pady=ey)
bdot = Button(
    fdev_0_dot_eval,
    bg=bgcl,
    font=bfont,
    text=".",
    border=3,
    relief=btst2s,
    padx=16.5,
    pady=y,
    activebackground=cldef,
    activeforeground="green",
    command=lambda: inp("."),
)
bdot.pack(side=LEFT, padx=ex, pady=ey)
bequl = Button(
    fdev_0_dot_eval,
    bg=bgcl,
    fg="green",
    font=bfont,
    text="=",
    border=3,
    relief=btst2s,
    padx=x,
    pady=y,
    activebackground=cldef,
    activeforeground="lime",
    command=resulting,
)
bequl.pack(side=LEFT, padx=ex, pady=ey)
# ----------------------------------------------------------------------------------------------------------------------
# status bar elements
statusbar = Frame(root, bg=bgcl, pady=2, padx=2)
statusbar.pack(side=BOTTOM, fill=X)
bs1th = Button(
    statusbar,
    bg=bgcl,
    font=ftst2,
    text="REENTER",
    border=3,
    relief=btst1f,
    fg="green",
    activebackground=cldef,
    activeforeground="orange",
    command=reenter,
)
bs1th.pack(side=LEFT)
# shivraj singh amritsar campus 2023693
lS1 = Label(
    statusbar, bg=bgcl, font=ftst2, text=" [ " + " VERSION 1.2.41 SE+" + " ]", pady=2
)
lS1.pack(side=LEFT, pady=3, padx=2)
# ----------------------------------------------------------------------------------------------------------------------
root.mainloop()
