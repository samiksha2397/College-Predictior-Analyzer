from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import os


def fun18():

    #home uni pie
    
    df=pd.read_csv("analysis_data.csv");
    
    df_seat_type=df.iloc[:,-3]
    seat_list=list(df_seat_type)
    seat_array =  np.array(seat_list)
    
    OPENH = np.where(np.logical_or(seat_array=="GOPENH",seat_array=="LOPENH"))
    OBCH = np.where(np.logical_or(seat_array=="GOBCH",seat_array=="LOBCH"))
    NT1H = np.where(np.logical_or(seat_array=="GNT1H",seat_list=="LNT1H"))
    NT2H = np.where(np.logical_or(seat_array=="GNT2H",seat_array=="LNT2H"))
    NT3H = np.where(np.logical_or(seat_array=="GNT3H",seat_array=="LNT3H"))
    SCH = np.where(np.logical_or(seat_array=="GSCH",seat_array=="LSCH"))
    STH = np.where(np.logical_or(seat_array=="GSTH",seat_array=="LSTH"))
    VJH = np.where(np.logical_or(seat_array=="GVJH",seat_array=="LVJH"))
    
    OPENH_LEN = len(seat_array[OPENH])
    OBCH_LEN = len(seat_array[OBCH])
    NT1H_LEN = len(seat_array[NT1H])
    NT2H_LEN = len(seat_array[NT2H])
    NT3H_LEN = len(seat_array[NT3H])
    SCH_LEN = len(seat_array[SCH])
    STH_LEN = len(seat_array[STH])
    VJH_LEN = len(seat_array[VJH])
    
    
    labels = 'OPENH','OBCH','NT1H','NT2H','NT3H','SCH','STH','VJH'
    sizes =[OPENH_LEN,OBCH_LEN,NT1H_LEN,NT2H_LEN,NT3H_LEN,SCH_LEN,STH_LEN,VJH_LEN]
    explode = (0,0,0,0,0,0,0,0)
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red','lightgreen','grey','violet'] 
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
     
    plt.axis('equal')
    plt.title('Distribution of Home University Seats According to Caste')
    plt.savefig(r'C:\Users\Samiksha\Desktop\nnnn\ab.png')  
    plt.close()  
    os.system(r'C:\Users\Samiksha\Desktop\nnnn\ab.png')