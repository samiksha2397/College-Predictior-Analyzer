

#Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from tkinter import messagebox
from tkinter import *

daf = pd.read_csv("merged.csv")

def fun6(v,v1):



        root = Tk()
        root.title("MHCET Colleges")
        root.geometry("600x600")
       
        ll=Label(root,text='Total No. of Available seats',font=("Comic Sans MS",22,"bold"),fg="red")
        ll.pack()
        temp1 = daf['COLLEGE'].value_counts(ascending=False).to_frame()
        l=Label(root,text=temp1,font=("Comic Sans MS",12,"bold"),fg="blue")
        l.pack()
        print (temp1)


        X = daf.iloc[:,[0,1]].values
        y= daf.iloc[:,9].values

        from sklearn.cross_validation import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        X_test[np.isnan(X_test)] = np.median(X_test[~np.isnan(X_test)])
        X_train[np.isnan(X_train)] = np.median(X_train[~np.isnan(X_train)])




        if v<=0 or v>200 and v1<0:
            messagebox.showerror("Error", "Not Applicable!!")
            print("not applicable")

        else:
            s=[v1,v]
            arrs=np.array(s)
            model = svm.LinearSVC(multi_class='ovr')
            model.fit(X_train, y_train)
            y_pred=model.predict(X_test)
            y_pred1=model.predict(arrs)

        yy=np.unique(y_pred)
        

        N = Label(root, text="Predicted Colleges are:",font=("Comic Sans MS",22,"bold"), fg="red")
        N.pack(pady=30)
        for word in yy:
            L=Label(root,text=word,font=("Comic Sans MS",12,"bold"),fg="blue")
            L.pack()
            print(word)
            
        yw=np.unique(y_pred1)
        

        N = Label(root, text="Most Probable College:",font=("Comic Sans MS",22,"bold"), fg="red")
        N.pack(pady=30)
        for word in yw:
            L=Label(root,text=word,font=("Comic Sans MS",12,"bold"),fg="blue")
            L.pack()
            print(word)

        buttonA1 = Button(root,text = "Go Back",font=("Comic Sans MS",10,"bold"),bg='grey',fg='white',command =root.destroy)
        buttonA1.pack(pady=10)

       
        root.mainloop()





