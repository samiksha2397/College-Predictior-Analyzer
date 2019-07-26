from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import os
import pylab

df=pd.read_csv("analysis_data.csv");
def fun16():


#Marks

    df.fillna(value=0,inplace=True)
    x=np.arange(10)
    
    df_college=df.iloc[:,9]
    college_list=list(df_college)
    college_array =  np.array(college_list)
    
    df_m=df.iloc[:,1]
    m_list=list(df_m)
    m_array =  np.array(m_list)
    
    df_j=df.iloc[:,2]
    j_list=list(df_j)
    j_array =  np.array(j_list)
    
    
    COEPM = np.logical_and(m_array ,college_array == 'COEP').mean()
    CUMMINSM =np.logical_and(m_array ,college_array ==  'CUMMINS').mean()
    MITM =np.logical_and(m_array ,college_array == 'MIT').mean()
    NBNM= np.logical_and(m_array ,college_array ==  'NBN').mean()
    PCCOEM=np.logical_and(m_array ,college_array ==  'PCCOE').mean()
    PICTM=np.logical_and(m_array ,college_array ==  'PICT').mean()
    SCOEM = np.logical_and(m_array ,college_array ==  'SCOE').mean()
    SITM =np.logical_and(m_array ,college_array ==  'SIT').mean()
    SKNCOEM =np.logical_and(m_array ,college_array == 'SKNCOE').mean()
    VITM=np.logical_and(m_array ,college_array =='VIT').mean()
    
    college1 = []
    college1.append(COEPM)
    college1.append(CUMMINSM)
    college1.append(MITM)
    college1.append(NBNM)
    college1.append(PCCOEM)
    college1.append(PICTM)
    college1.append(SCOEM)
    college1.append(SITM)
    college1.append(SKNCOEM)
    college1.append(VITM)
    
    COEPJ = np.logical_and(j_array ,college_array == 'COEP').mean()
    CUMMINSJ =np.logical_and(j_array ,college_array ==  'CUMMINS').mean()
    MITJ =np.logical_and(j_array ,college_array == 'MIT').mean()
    NBNJ= np.logical_and(j_array ,college_array ==  'NBN').mean()
    PCCOEJ=np.logical_and(j_array ,college_array ==  'PCCOE').mean()
    PICTJ=np.logical_and(j_array ,college_array ==  'PICT').mean()
    SCOEJ = np.logical_and(j_array ,college_array ==  'SCOE').mean()
    SITJ =np.logical_and(j_array ,college_array ==  'SIT').mean()
    SKNCOEJ =np.logical_and(j_array ,college_array == 'SKNCOE').mean()
    VITJ=np.logical_and(j_array ,college_array =='VIT').mean()
    
    college2 = []
    college2.append(COEPJ)
    college2.append(CUMMINSJ)
    college2.append(MITJ)
    college2.append(NBNJ)
    college2.append(PCCOEJ)
    college2.append(PICTJ)
    college2.append(SCOEJ)
    college2.append(SITJ)
    college2.append(SKNCOEJ)
    college2.append(VITJ)
    
    y1=np.array(college1)
    y2=np.array(college2)
    
    plt.plot(x,y1,linewidth=2.0)
    plt.plot(x,y2,linewidth=2.0)
    ax = plt.subplot(111)
    
    ax.set_xlabel('COLLEGES')
    ax.set_ylabel('MARKS')
    pylab.xticks(range(10),rotation='vertical')
    ax.set_xticklabels(['COEP','CUMMINS','MIT','NBN','PCCOE','PICT','SCOE','SIT','SKNCOE','VIT'])
    ax.set_yticklabels([20,40,60,80,100,120,140,160,180,200])
    plt.title('Collegewise Analysis  of Marks in MHT CET and JEE(Main) ')
    
    plt.legend()
    plt.savefig(r'C:\Users\Samiksha\Desktop\nnnn\neww.png')  
    plt.close()  
    os.system(r'C:\Users\Samiksha\Desktop\nnnn\neww.png')
