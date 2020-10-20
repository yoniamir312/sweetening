import os
import pandas as pd
import numpy as np

'''
This function gets a data frame of all the NPOs rated the same in the general question. 
it iterates all the NPOs in this data frame and checks of each pair has the same dimensions (e.g
the differences in all dimensions ratings are not above 1) or has different dimensions (e.g. at least
one dimention has a difference above 2) 

The function returns 2 lists of tuples.
The first list contains tuples of same dimensions NPOs
The second list contains tuples of different dimensions NPOs
'''

def dimensions_check(df_to_donate):
    GS_DS=[]
    GS_DD=[]
    tup_DS=()
    tup_DD=()

    for i in np.arange(0,(len(df_to_donate.index)-1)):
        row_1=df_to_donate.iloc[i]
        for j in np.arange((i+1),len(df_to_donate.index)):
            row_2=df_to_donate.iloc[j]
            if abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-Local_community']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-Local_community']))<2:
                if abs ((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-animal_rights']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-animal_rights']))<2:
                    if abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-culture']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-culture']))<2:
                        if abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-environmental']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-environmental']))<2:
                            if abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-gender']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-gender']))<2:
                                if abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-health_care ']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-health_care ']))<2:
                                    if abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-human_rights']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-human_rights']))<2:
                                        if abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-religion']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-religion']))<2:
                                            pair_DS=[row_1['sender'],row_2['sender']]
                                            GS_DS.append(pair_DS)

            if abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-religion']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-religion']))>2:
                pair_DD=[row_1['sender'],row_2['sender']]
                GS_DD.append(pair_DD)
            elif abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-human_rights']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-human_rights']))>2:
                pair_DD=[row_1['sender'],row_2['sender']]
                GS_DD.append(pair_DD)
            elif abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-health_care ']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-health_care ']))>2:
                pair_DD=[row_1['sender'],row_2['sender']]
                GS_DD.append(pair_DD)
            elif abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-gender']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-gender']))>2:
                pair_DD=[row_1['sender'],row_2['sender']]
                GS_DD.append(pair_DD)
            elif abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-environmental']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-environmental']))>2:
                pair_DD=[row_1['sender'],row_2['sender']]
                GS_DD.append(pair_DD)
            elif abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-culture']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-culture']))>2:
                pair_DD=[row_1['sender'],row_2['sender']]
                GS_DD.append(pair_DD)                              
            elif abs ((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-animal_rights']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-animal_rights']))>2:
                pair_DD=[row_1['sender'],row_2['sender']]
                GS_DD.append(pair_DD)
            elif abs((row_1['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-Local_community']-row_2['2.-to-what-extent-was-your-decision-in-question-1-influenced-by-the-approach-of-this-organization-to-the-following-issues:-Local_community']))>2:
                pair_DD=[row_1['sender'],row_2['sender']]
                GS_DD.append(pair_DD)
    
    return GS_DS, GS_DD;