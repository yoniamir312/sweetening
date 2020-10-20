import pandas as pd
import numpy as np
import random

def make_first_block_df(all_DS,all_DD):
    N_of_pairs = 20 #the number of pairs in each condition- if we decided otherwise it should be changed
    
    left_NPO_1=[]
    right_NPO_1=[]
    amount_left_1= [50] * (N_of_pairs*3)
    amount_right_1= [50] * (N_of_pairs*3)
    NPO_relation=[]
    if len(all_DS)<N_of_pairs: 
        return "There are not enough NPOs' pairs for this subject"
    if len(all_DD)<N_of_pairs:
        return "There are not enough NPOs' pairs for this subject"
    else:
        chosen_DS= random.sample(all_DS,k=N_of_pairs)
        chosen_DD= random.sample(all_DD,k=N_of_pairs)
        all_NPOs= chosen_DS+chosen_DD
        NPO_list=[]
        for item in all_NPOs:
            NPO_list.append(item[0])
            NPO_list.append(item[1])
        

        NPO_list=set(NPO_list) # I wanted to add this so in the inedtical condition we will have 20 
        #different NPOs... but maybe there isnt 20 different among the pairs
        #so we can have few dubles...?
        random_NPO=random.sample(NPO_list,k=N_of_pairs) #if there isn't 20 20 different paris it wont work... and there
        #is a need to try again the chose random NPOS

        for item in chosen_DS:
            if random.random() < 0.5:
                left_NPO_1.append(item[0][:-14])
                right_NPO_1.append(item[1][:-14])
            else:
                left_NPO_1.append(item[1][:-14])
                right_NPO_1.append(item[0][:-14])
            NPO_relation.append('DS')
        for item in chosen_DD:
            if random.random() < 0.5:
                left_NPO_1.append(item[0][:-14])
                right_NPO_1.append(item[1][:-14])
            else:
                left_NPO_1.append(item[1][:-14])
                right_NPO_1.append(item[0][:-14])
            NPO_relation.append('DD')
        for item in random_NPO:
            left_NPO_1.append(item[:-14])
            right_NPO_1.append(item[:-14])
            NPO_relation.append('IN')

        data={'left_NPO': left_NPO_1,'right_NPO': right_NPO_1,'amount_left':amount_left_1,'amoumt_right':amount_right_1,"NPOs_relation": NPO_relation}

        first_block_df=pd.DataFrame(data)
        first_block_df=first_block_df.sample(frac=1)

        #second block (not really but the trials with 0.5$ sweetening)
        left_NPO_2=[]
        right_NPO_2=[]
        amount_left_2=[]
        amount_right_2=[]
        NPO_relation_2=[]

        for i in np.arange(0,(N_of_pairs*3)):
            if random.random() < 0.5:
                amount_left_2.append(50)
                amount_right_2.append(50.5)
            else:
                amount_left_2.append(50.5)
                amount_right_2.append(50)


        for item in chosen_DS:
            if random.random() < 0.5:
                left_NPO_2.append(item[0][:-14])
                right_NPO_2.append(item[1][:-14])
            else:
                left_NPO_2.append(item[1][:-14])
                right_NPO_2.append(item[0][:-14])
            NPO_relation_2.append('DS')
        for item in chosen_DD:
            if random.random() < 0.5:
                left_NPO_2.append(item[0][:-14])
                right_NPO_2.append(item[1][:-14])
            else:
                left_NPO_2.append(item[1][:-14])
                right_NPO_2.append(item[0][:-14])
            NPO_relation_2.append('DD')
        for item in random_NPO:
            left_NPO_2.append(item[:-14])
            right_NPO_2.append(item[:-14])
            NPO_relation_2.append('IN')

        data2={'left_NPO': left_NPO_2,'right_NPO': right_NPO_2,'amount_left':amount_left_2,'amoumt_right':amount_right_2,"NPOs_relation": NPO_relation_2}
        second_block_df=pd.DataFrame(data2)
        second_block_df=second_block_df.sample(frac=1)

        #third block (not really but the trials with 1$ sweetening)
        left_NPO_3=[]
        right_NPO_3=[]
        amount_left_3=[]
        amount_right_3=[]
        NPO_relation_3=[]

        for i in np.arange(0,(N_of_pairs*3)):
            if random.random() < 0.5:
                amount_left_3.append(50)
                amount_right_3.append(51)
            else:
                amount_left_3.append(51)
                amount_right_3.append(50)


        for item in chosen_DS:
            if random.random() < 0.5:
                left_NPO_3.append(item[0][:-14])
                right_NPO_3.append(item[1][:-14])
            else:
                left_NPO_3.append(item[1][:-14])
                right_NPO_3.append(item[0][:-14])
            NPO_relation_3.append('DS')
        for item in chosen_DD:
            if random.random() < 0.5:
                left_NPO_3.append(item[0][:-14])
                right_NPO_3.append(item[1][:-14])
            else:
                left_NPO_3.append(item[1][:-14])
                right_NPO_3.append(item[0][:-14])
            NPO_relation_3.append('DD')
        for item in random_NPO:
            left_NPO_3.append(item[:-14])
            right_NPO_3.append(item[:-14])
            NPO_relation_3.append('IN')

        data3={'left_NPO': left_NPO_3,'right_NPO': right_NPO_3,'amount_left':amount_left_3,'amoumt_right':amount_right_3,"NPOs_relation": NPO_relation_3}
        third_block_df=pd.DataFrame(data3)
        third_block_df=third_block_df.sample(frac=1)

        #fourth block (not really but the trials with 2$ sweetening)
        left_NPO_4=[]
        right_NPO_4=[]
        amount_left_4=[]
        amount_right_4=[]
        NPO_relation_4=[]

        for i in np.arange(0,(N_of_pairs*3)):
            if random.random() < 0.5:
                amount_left_4.append(50)
                amount_right_4.append(52)
            else:
                amount_left_4.append(52)
                amount_right_4.append(50)


        for item in chosen_DS:
            if random.random() < 0.5:
                left_NPO_4.append(item[0][:-14])
                right_NPO_4.append(item[1][:-14])
            else:
                left_NPO_4.append(item[1][:-14])
                right_NPO_4.append(item[0][:-14])
            NPO_relation_4.append('DS')
        for item in chosen_DD:
            if random.random() < 0.5:
                left_NPO_4.append(item[0][:-14])
                right_NPO_4.append(item[1][:-14])
            else:
                left_NPO_4.append(item[1][:-14])
                right_NPO_4.append(item[0][:-14])
            NPO_relation_4.append('DD')
        for item in random_NPO:
            left_NPO_4.append(item[:-14])
            right_NPO_4.append(item[:-14])
            NPO_relation_4.append('IN')

        data4={'left_NPO': left_NPO_4,'right_NPO': right_NPO_4,'amount_left':amount_left_4,'amoumt_right':amount_right_4,"NPOs_relation": NPO_relation_4}
        fourth_block_df=pd.DataFrame(data4)
        #fourth_block_df=fourth_block_df.sample(frac=1)

        df_sweeten= pd.concat([second_block_df,third_block_df,fourth_block_df],ignore_index=True)
        df_sweeten=df_sweeten.sample(frac=1)

        experiment_order_df=pd.concat([first_block_df,df_sweeten,],ignore_index=True)

        break_vector= [0]*(4*3*N_of_pairs)
        for i in np.arange(0,len(break_vector)):
            if (i+1)%30==0:
                break_vector[i]=1

        experiment_order_df['break']=break_vector

    #arrnage the name of long name NPOs so labjs will presernt it right
        left_NPO_A= [" "]*(4*3*N_of_pairs)
        left_NPO_B=[" "]*(4*3*N_of_pairs)
        right_NPO_A=[" "]*(4*3*N_of_pairs)
        right_NPO_B=[" "]*(4*3*N_of_pairs)

        experiment_order_df['left_NPO_A']=left_NPO_A
        experiment_order_df['left_NPO_B']=left_NPO_B
        experiment_order_df['right_NPO_A']=right_NPO_A
        experiment_order_df['right_NPO_B']=right_NPO_B

        for index, row in experiment_order_df.iterrows():
            if len(row['left_NPO'].split())>3:                
                experiment_order_df.iloc[index,experiment_order_df.columns.get_loc('left_NPO_A')]=" ".join(row['left_NPO'].split()[0:3])
                experiment_order_df.iloc[index,experiment_order_df.columns.get_loc('left_NPO_B')]=" ".join(row['left_NPO'].split()[3:len(row['left_NPO'].split())])
                experiment_order_df.iloc[index,experiment_order_df.columns.get_loc('left_NPO')]=" "
            if len(row['right_NPO'].split())>3:                
                experiment_order_df.iloc[index,experiment_order_df.columns.get_loc('right_NPO_A')]=" ".join(row['right_NPO'].split()[0:3])
                experiment_order_df.iloc[index,experiment_order_df.columns.get_loc('right_NPO_B')]=" ".join(row['right_NPO'].split()[3:len(row['right_NPO'].split())])
                experiment_order_df.iloc[index,experiment_order_df.columns.get_loc('right_NPO')]=" "

        
        return experiment_order_df



