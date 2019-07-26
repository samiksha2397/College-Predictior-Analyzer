from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import os


def fun17():

    df=pd.read_csv("analysis_data.csv");
    
    #caste
    
    df_caste_type=df.iloc[:,7]
    caste_list=list(df_caste_type)
    caste_array =  np.array(caste_list)
    
    OPEN = np.where(caste_array=="OPEN")
    OBC = np.where(caste_array=="OBC")
    NT1 = np.where(caste_array=="NT1")
    NT2 = np.where(caste_array=="NT2")
    NT3 = np.where(caste_array=="NT3")
    VJ = np.where(caste_array=="VJ")
    SC = np.where(caste_array=="SC")
    ST = np.where(caste_array=="ST")
    
    OPEN_LEN = len(caste_array[OPEN])
    OBC_LEN = len(caste_array[OBC])
    NT1_LEN = len(caste_array[NT1])
    NT2_LEN = len(caste_array[NT2])
    NT3_LEN = len(caste_array[NT3])
    SC_LEN = len(caste_array[SC])
    ST_LEN = len(caste_array[ST])
    VJ_LEN = len(caste_array[VJ])
    
    labels = 'OPEN','OBC','NT1','NT2','NT3','SC','ST','VJ'
    sizes =[OPEN_LEN,OBC_LEN,NT1_LEN,NT2_LEN,NT3_LEN,SC_LEN,ST_LEN,VJ_LEN]
    explode = (0,0,0,0,0,0,0,0)
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red','lightgreen','grey','violet'] 
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
     
    





    plt.axis('equal')
    plt.title('Distribution of Seats According to Caste')
    plt.savefig(r'C:\Users\Samiksha\Desktop\nnnn\abc.png')  
    plt.close()  
    os.system(r'C:\Users\Samiksha\Desktop\nnnn\abc.png')
    


   
