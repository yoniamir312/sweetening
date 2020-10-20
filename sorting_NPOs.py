import os
import pandas as pd
import numpy as np
import random
from dimensions_check import *
from make_experiment_order import *

directory = os.getcwd()

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        df = pd.read_csv (os.path.join(directory, filename))
        #df is the Data frame of one subject from all the subjects saved in the directory
        #during the loop the NPOs will be sorted as Generally-Similar if they have the same answer "to_dunate"
        donate_1 = df[df['to_donate'] ==1]
        DS1,DD1 = dimensions_check(donate_1)
        donate_2 = df[df['to_donate'] ==2]
        DS2,DD2 = dimensions_check(donate_2) 
        donate_3 = df[df['to_donate'] ==3]
        DS3,DD3 = dimensions_check(donate_3)
        donate_4 = df[df['to_donate'] ==4]
        DS4,DD4 = dimensions_check(donate_4)  
        donate_5 = df[df['to_donate'] ==5]
        DS5,DD5 = dimensions_check(donate_5)  
        donate_6 = df[df['to_donate'] ==6]
        DS6,DD6 = dimensions_check(donate_6)
        donate_7 = df[df['to_donate'] ==7] 
        DS7,DD7 = dimensions_check(donate_7)

        all_DS = DS1+DS2+DS3+DS4+DS5+DS6+DS7
        all_DD = DD1+DD2+DD3+DD4+DD5+DD6+DD7
        subject_experiment_order=make_first_block_df(all_DS,all_DD)
        

        subject_experiment_order.to_csv("input_"+filename)
        
        print(subject_experiment_order)
        
        '''
        for index, row in subject_experiment_order.iterrows():
            if len(row['left_NPO'].split())>3:
                print(row['left_NPO'])
                row['left_NPO_A']=" ".join(row['left_NPO'].split()[0:3])
                row['left_NPO_B']=" ".join(row['left_NPO'].split()[3:len(row['left_NPO'].split())])
                subject_experiment_order.iloc[index,subject_experiment_order.columns.get_loc('left_NPO_B')]=" ".join(row['left_NPO'].split()[3:len(row['left_NPO'].split())])
                print(row['left_NPO_B'])
        print(subject_experiment_order)
        '''