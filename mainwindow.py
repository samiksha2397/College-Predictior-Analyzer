from tkinter import *
import PIL
from PIL import Image,ImageTk
from homeother_bar import *
from marks_line import *
from homeuni_pie import *
from caste_pie import *
from mhcetpredict import *
from jeepredict import *

def fun5():

    val=jeeEntry.get()
    val5=jeeMerit.get()
    if(val==None):
      print(" ")
    else:
        print((val))
        fun9(int(val),int(val5))

def fun7():
    val1 = mhcetEntry.get()
    val2=mhtmerit.get()
    if (val1 == None):
        print(" ")
    else:
        print((val1))
        fun6(int(val1),int(val2))

def fun():
    fun15()

def fun2():
    fun16()

def fun3():
    fun17()

def fun4():
    fun18()
    
def analysisWindow():
    root1 = Tk()
    root1.title("Analysis")
    root1.configure(highlightbackground="black", highlightcolor="black", highlightthickness=3,bg='grey')
    root1.geometry("600x600")
    
    seats=Button(root1,text="TYPES OF UNIVERSITIES(BAR GRAPH)",font=("Comic Sans MS",15,"bold"),fg="blue", bd=3,relief=RAISED,command=fun)
    seats.config(height=2, width=77)
    seats.pack(pady=30)

    marks= Button(root1, text="MHCET & JEE MARKS(LINE GRAPH)", font=("Comic Sans MS",15,"bold"),fg="blue", bd=3,relief=RAISED,command=fun2)
    marks.config(height=2, width=77)
    marks.pack(pady=30)

    caste = Button(root1, text="DISTRIBUTION OF SEATS ACCORDING TO THE CASTE(PIE CHART)", font=("Comic Sans MS",15,"bold"),fg="blue",bd=3,relief=RAISED, command=fun3)
    caste.config(height=2, width=77)
    caste.pack(pady=30)

    homeuni = Button(root1, text="DISTRIBUTION OF HOME UNIVERSITY SEATS ACCORDING TO THE CASTE(PIE CHART)", font=("Comic Sans MS",15,"bold"),fg="blue",bd=3,relief=RAISED, command=fun4)
    homeuni.config(height=2, width=77)
    homeuni.pack(pady=30)
    
    buttonA1 = Button(root1,text = "Go Back",font=("Comic Sans MS",13,"bold"),bg='grey',fg='white',command =root1.destroy)
    buttonA1.pack(pady=10)
    

    root1.mainloop()

def predictorWindow():
        global jeeEntry,mhcetEntry,mhtmerit,jeeMerit,g1,g2,g3,g4
        
        root2 = Tk()
        root2.title("Predictor")
        root2.geometry("600x600")
        
       
        Frame2 = Frame(root2,highlightbackground="black", highlightcolor="black", highlightthickness=3,height=300,width=300)
        Frame2.grid(row = 0, column = 0, sticky = W+E+N+S)
        
        mhcet=Label(Frame2,text="MHCET",font=("Comic Sans MS",42,"bold"),fg="blue")
        mhcet.pack(padx=20, pady=30)

        l1=Label(Frame2,text="Enter Your marks here:",font=("Comic Sans MS",15))
        l1.pack(pady=10)
        mhcetEntry=Entry(Frame2)
        mhcetEntry.pack(pady=10)
        mhcetEntry.insert(END, 'Range 0-200')
        
        l2=Label(Frame2,text="Enter Your merit here:",font=("Comic Sans MS",15))
        l2.pack()
        mhtmerit=Entry(Frame2)
        mhtmerit.pack(pady=10)
        
        mhcetSubmit=Button(Frame2,text="SUBMIT",font=("Comic Sans MS",15,"bold"),fg="yellow",bg='red',command=fun7)
        mhcetSubmit.config(height=1, width=12)
        mhcetSubmit.pack(padx=20, pady=20)
        
        buttonA1 = Button(Frame2,text = "Go Back",font=("Comic Sans MS",10,"bold"),bg='grey',fg='white',command =root2.destroy)
        buttonA1.pack(pady=10)
        
        Frame3 = Frame(root2,highlightbackground="black", highlightcolor="black", highlightthickness=3)
        Frame3.grid(row = 0, column = 1, sticky = W+E+N+S)
        
        jee = Label(Frame3, text="JEE", font=("Comic Sans MS",42,"bold"),fg="blue")
        jee.pack(padx=20, pady=30)

        l2=Label(Frame3,text="Enter Your marks here:",font=("Comic Sans MS",15))
        l2.pack(pady=10)
        jeeEntry = Entry(Frame3)
        jeeEntry.pack(padx=20)
        jeeEntry.insert(END, 'Range 0-360')
        
        l3=Label(Frame3,text="Enter Your merit here:",font=("Comic Sans MS",15))
        l3.pack(pady=10)
        jeeMerit = Entry(Frame3)
        jeeMerit.pack(pady=10)

       
        jeeSubmit=Button(Frame3,text="SUBMIT",font=("Comic Sans MS",15,"bold"),fg="yellow",bg='red',command=fun5)
        jeeSubmit.config(height=1, width=12)
        jeeSubmit.pack(padx=20, pady=20)
        
        buttonA2 = Button(Frame3,text = "Go Back",font=("Comic Sans MS",10,"bold"),bg='grey',fg='white',command =root2.destroy)
        buttonA2.pack(pady=10)
        
        root2.rowconfigure(0, weight=1)
        root2.columnconfigure(0, weight=1)
        root2.columnconfigure(1, weight=1)
        

        root2.mainloop()

def change_color():
    current_color =l.cget("foreground")
    next_color = "red" if current_color == "blue" else "blue"
    l.config(foreground=next_color)
    root3.after(1000, change_color)

def change_colora():
    current_color =analysisButton.cget("foreground")
    next_color = "white" if current_color == "black" else "black"
    analysisButton.config(foreground=next_color)
    root3.after(1000, change_colora)

def change_colorp():
    current_color =predictorButton.cget("foreground")
    next_color = "white" if current_color == "black" else "black"
    predictorButton.config(foreground=next_color)
    root3.after(1000, change_colorp)

   
root3=Tk()

root3.geometry("600x600")
root3.configure(background='grey',highlightbackground="black", highlightcolor="black", highlightthickness=3)
root3.title("College Prediction & Analysis")


viewerPane = Frame(root3)
viewerPane.grid(row=0,column=0,sticky="nsew")

im=PIL.Image.open("a.jpg").convert("RGB") 
im2 = im.resize((500, 900)) 
photo=ImageTk.PhotoImage(im2)  
cv = Canvas()  
cv.grid(row=0,column=0,sticky="nsew")  
cv.create_image(0, 0, image=photo, anchor='nw')  

actionPane = Frame(root3)
actionPane.grid(row=0,column=1,sticky="nsew")

l=Label(actionPane,text="Welcome to the College Prediction!!",font=("Comic Sans MS",34, "bold", "italic"),fg="blue")
l.pack(pady=30)
change_color()

analysisButton=Button(actionPane,text="ANALYSIS",font=("Comic Sans MS",19,"bold"),fg="black",bg="grey",command=analysisWindow)
analysisButton.config(height=2, width=10)
analysisButton.pack(pady=40)
change_colora()

predictorButton=Button(actionPane,text="PREDICTOR",font=("Comic Sans MS",19,"bold"),fg="black",bg="grey",command=predictorWindow)
predictorButton.config(height=2, width=10)
predictorButton.pack(pady=40)
change_colorp()
    
root3.rowconfigure(0, weight=1)
root3.columnconfigure(0, weight=1)
root3.columnconfigure(1, weight=1)


root3.mainloop()


