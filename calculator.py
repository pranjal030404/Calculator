from tkinter import *
from tkinter import messagebox
from math import pi, e, sin, cos, tan, log

window = Tk()
screenSize = "279x442"
window.geometry(screenSize)
window.resizable(0, 0)
window.title("Calcualtor")
#function
def about():
    messagebox.showinfo('About')

def clickButton(item):
    global expression
    inputText.set(inputText.get()+(str(item)))

def clearButton():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])

def clearAll():
    inputText.set("")

def expand():
    if screenSize=="350x700":
        window.geometry("350x755")
    else:
        window.geometry("350x755")
def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "ERROR..."
        inputText.set(result)
#menubar
menubar = Menu(window,bg="black",fg="white")
filemenu = Menu(menubar, tearoff=0,bg="black",fg="white")
filemenu.add_command(label="Copy")
filemenu.add_command(label="Paste")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Edit", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0,bg="black",fg="white")
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

expression = ""
inputText = StringVar()

inputFrame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="gray",
                    highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 25, ), textvariable=inputText, width=50,fg="white", bg="black", bd=0,
                    justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=13)

mainFrame = Frame(window, width=312, height=272.5, bg="black")
mainFrame.pack()

ac = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\ac.png")
acimage = ac.subsample(4,4)
ac = Button(mainFrame, text="AC", fg="black", image=acimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clearAll()).grid(row=0, column=0, padx=1, pady=1)

clear = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\clear.png")
clearimage = clear.subsample(4,4)
clear = Button(mainFrame, text="AC", fg="black", image=clearimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clearButton()).grid(row=0, column=1, padx=1, pady=1)

expan_btn = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\expan_btn.png")
expan_btnimage = expan_btn.subsample(4,4)
percentage = Button(mainFrame, fg="black", image=expan_btnimage, bd=0, bg="black", cursor="hand2",
               command=lambda: expand()).grid(row=0, column=2, padx=1, pady=1)

divide = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\divide.png")
divideimage = divide.subsample(4,4)
divide = Button(mainFrame, text="/", fg="white",image=divideimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("/")).grid(row=0, column=3, padx=1, pady=1)


seven = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\seven.png")
sevenimage = seven.subsample(4,4)
seven = Button(mainFrame, text="7", fg="black", image=sevenimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(7)).grid(row=1, column=0, padx=1, pady=1)

eight = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\eight.png")
eightimage = eight.subsample(4,4)
eight = Button(mainFrame, text="8", fg="black", image=eightimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(8)).grid(row=1, column=1, padx=1, pady=1)

nine = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\nine.png")
nineimage = nine.subsample(4,4)
nine = Button(mainFrame, text="9", fg="black", image=nineimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(9)).grid(row=1, column=2, padx=1, pady=1)

multi = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\multi.png")
multiimage = multi.subsample(4,4)
multiply = Button(mainFrame, text="*", fg="white",image=multiimage, bd=0, bg="black", cursor="hand2",
                  command=lambda: clickButton("*")).grid(row=1, column=3, padx=1, pady=1)

four = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\four.png")
fourimage = four.subsample(4,4)
four = Button(mainFrame, text="4", fg="black", image=fourimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(4)).grid(row=2, column=0, padx=1, pady=1)

five = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\five.png")
fiveimage = five.subsample(4,4)
five = Button(mainFrame, text="5", fg="black", image=fiveimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(5)).grid(row=2, column=1, padx=1, pady=1)

six = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\six.png")
siximage = six.subsample(4,4)
six = Button(mainFrame, text="6", fg="black", image=siximage, bd=0, bg="black", cursor="hand2",
             command=lambda: clickButton(6)).grid(row=2, column=2, padx=1, pady=1)

minus = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\minus.png")
minusimage = minus.subsample(4,4)
minus = Button(mainFrame, text="-", fg="white",image=minusimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("-")).grid(row=2, column=3, padx=1, pady=1)

one = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\one.png")
oneimage = one.subsample(4,4)
one = Button(mainFrame, text="1", fg="black", image=oneimage,bd=0, bg="black", cursor="hand2",
             command=lambda: clickButton(1)).grid(row=3, column=0, padx=1, pady=1)

two = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\two.png")
twoimage = two.subsample(4,4)
two = Button(mainFrame, text="2", fg="black",image=twoimage, bd=0, bg="black", cursor="hand2",
             command=lambda: clickButton(2)).grid(row=3, column=1, padx=1, pady=1)

three = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\three.png")
threeimage = three.subsample(4,4)
three = Button(mainFrame, text="3", fg="black",image=threeimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(3)).grid(row=3, column=2, padx=1, pady=1)

plus = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\plus.png")
plusimage = plus.subsample(4,4)
plus = Button(mainFrame, text="+", fg="white",image=plusimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton("+")).grid(row=3, column=3, padx=1, pady=1)


zero = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\0.png")
zeroimage = zero.subsample(4,4)
zero = Button(mainFrame, text="0", fg="black",image=zeroimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\point.png")
pointimage = point.subsample(4,4)
point = Button(mainFrame, text=".", fg="black",image=pointimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(".")).grid(row=4, column=2, padx=1, pady=1)


equal = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\equal.png")
equalimage = equal.subsample(4,4)
equals = Button(mainFrame, text="=", image=equalimage, fg="white", bd=0, bg="black", cursor="hand2",
                command=lambda: equalButton()).grid(row=4, column=3, padx=1, pady=1)

bracket1 = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\bracket1.png")
bracket1image = bracket1.subsample(4,4)
bracket1 = Button(mainFrame, text="pi", fg="black",image=bracket1image, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("(")).grid(row=5, column=0, padx=1, pady=1)

bracket2 = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\bracket2.png")
bracket2image = bracket2.subsample(4,4)
bracket2 = Button(mainFrame, text="pi", fg="black",image=bracket2image, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(")")).grid(row=5, column=1, padx=1, pady=1)

pie=3.1415
pi = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\pi.png")
piimage = pi.subsample(4,4)
pi = Button(mainFrame, text="pi", fg="black",image=piimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(pie)).grid(row=5, column=2, padx=1, pady=1)

eie = 2.7182
ee = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\eie.png")
eeimage = ee.subsample(4,4)
ee = Button(mainFrame, text="pi", fg="black",image=eeimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(eie)).grid(row=5, column=3, padx=1, pady=1)

sin_btn = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\sin_btn.png")
sin_btnimage = sin_btn.subsample(4,4)
sin_btn = Button(mainFrame, text="sin", fg="black",image=sin_btnimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("sin(")).grid(row=6, column=0, padx=1, pady=1)

cos_btn = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\cos_btn.png")
cos_btnimage = cos_btn.subsample(4,4)
cos_btn = Button(mainFrame, text="cos", fg="black",image=cos_btnimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("cos(")).grid(row=6, column=1, padx=1, pady=1)

tan_btn = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\tan_btn.png")
tan_btnimage = tan_btn.subsample(4,4)
tan_btn = Button(mainFrame, text="tan", fg="black",image=tan_btnimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("tan(")).grid(row=6, column=2, padx=1, pady=1)

log_btn = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\log_btn.png")
log_btnimage = log_btn.subsample(4,4)
log_btn = Button(mainFrame, text="log", fg="black",image=log_btnimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("log(")).grid(row=6, column=3, padx=1, pady=1)

expan = PhotoImage(file = r"C:\Users\mygam\OneDrive\Documents\advance-calculator-with-UI-in-python-master\advance-calculator-with-UI-in-python-master\images\expan_btn.png")
expanimage = expan.subsample(4,4)
expan = Label(window, text="pi", fg="black",image=expanimage, bg="black").pack(side=BOTTOM)

window.config(bg="black",menu=menubar)
window.mainloop()

#Thanks for giving the opportunity 
#               PRANJAL TIWARI