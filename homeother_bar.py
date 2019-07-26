from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import os


def fun15():

    df=pd.read_csv("analysis_data.csv");
    
    #University
    N = 2
    df_seat_type = df.iloc[:,-3]
    seat_list = list(df_seat_type)
    seat_array = np.array(seat_list)
    
    #home uni
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
    
    #other uni
    OPENO = np.where(np.logical_or(seat_array=="GOPENO",seat_array=="LOPENO"))
    OBCO = np.where(np.logical_or(seat_array=="GOBCO",seat_array=="LOBCO"))
    NT1O = np.where(np.logical_or(seat_array=="GNT1O",seat_list=="LNT1O"))
    NT2O = np.where(np.logical_or(seat_array=="GNT2O",seat_array=="LNT2O"))
    NT3O = np.where(np.logical_or(seat_array=="GNT3O",seat_array=="LNT3O"))
    SCO = np.where(np.logical_or(seat_array=="GSCO",seat_array=="LSCO"))
    STO = np.where(np.logical_or(seat_array=="GSTO",seat_array=="LSTO"))
    VJO = np.where(np.logical_or(seat_array=="GVJO",seat_array=="LVJO"))
    
    OPENO_LEN = len(seat_array[OPENO])
    OBCO_LEN = len(seat_array[OBCO])
    NT1O_LEN = len(seat_array[NT1O])
    NT2O_LEN = len(seat_array[NT2O])
    NT3O_LEN = len(seat_array[NT3O])
    SCO_LEN = len(seat_array[SCO])
    STO_LEN = len(seat_array[STO])
    VJO_LEN = len(seat_array[VJO])
    
    OPENB = []
    OBCB = []
    NT1B = []
    NT2B = []
    NT3B = []
    SCB = []
    STB = []
    VJB = []
    
    OPENB.append(OPENH_LEN)
    OBCB.append(OBCH_LEN)
    NT1B.append(NT1H_LEN)
    NT2B.append(NT2H_LEN)
    NT3B.append(NT3H_LEN)
    SCB.append(SCH_LEN)
    STB.append(STH_LEN)
    VJB.append(VJH_LEN)
    
    OPENB.append(OPENO_LEN)
    OBCB.append(OBCO_LEN)
    NT1B.append(NT1O_LEN)
    NT2B.append(NT2O_LEN)
    NT3B.append(NT3O_LEN)
    SCB.append(SCO_LEN)
    STB.append(STO_LEN)
    VJB.append(VJO_LEN)
    
    ind = np.arange(N)
    width = 0.1
    
    fig, ax = plt.subplots()
    rect1 = ax.bar(ind,OPENB,width,color='red')
    rect2 = ax.bar(ind+width,OBCB,width,color='lightgreen')
    rect3 = ax.bar(ind+width*2,NT1B,width,color='green')
    rect4 = ax.bar(ind+width*3,NT2B,width,color='yellow')
    rect5 = ax.bar(ind+width*4,NT3B,width,color='lightblue')
    rect6 = ax.bar(ind+width*5,SCB,width,color='lightcoral')
    rect7 = ax.bar(ind+width*6,STB,width,color='gold')
    rect8 = ax.bar(ind+width*7,VJB,width,color='pink')
    
    ax.set_xlabel('University')
    ax.set_ylabel('No. of Students')
    ax.set_title('Types Of Universities')
    ax.set_xticks((ind+width*4))
    ax.set_xticklabels(('Home University','Other University'))
    
    ax.legend((rect1[0], rect2[0], rect3[0], rect4[0], rect5[0], rect6[0], rect7[0], rect8[0]), ('OPEN', 'OBC','NT1','NT2','NT3','SC','ST','VJ'))
    
    def autolabel(rect):
        """
        Attach a text label above each bar displaying its height
        """
        for r in rect:
            height = r.get_height()
            ax.text(r.get_x() + r.get_width()/2., height,
                    '%d' % int(height),
                    ha='center', va='bottom')
    
    autolabel(rect1)
    autolabel(rect2)
    autolabel(rect3)
    autolabel(rect4)
    autolabel(rect5)
    autolabel(rect6)
    autolabel(rect7)
    autolabel(rect8)


    plt.savefig(r'C:\Users\Samiksha\Desktop\nnnn\aaa.png')  
    plt.close()  
    os.system(r'C:\Users\Samiksha\Desktop\nnnn\aaa.png')
   
        