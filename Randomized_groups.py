import math
import numpy as np 
import random
from math import trunc
import streamlit as st
from streamlit import session_state as session




list_of_names=['Andrew','Arjun','Carol','Deven',\
   'Godzilla', 'Kelly','Steven','Michael','Oun','Roman','Ross','Stephanie','Suraqa','Thao','Tiago',]

list_of_names2=['none','Andrew','Arjun','Carol','Deven',\
    'Godzilla','Kelly','Steven','Michael','Oun','Roman','Ross','Stephanie','Suraqa','Thao','Tiago',]

def group_selector(num_of_groups):
    random.shuffle(list_of_names)
    group_size = len(list_of_names)/num_of_groups
    smallest_group=math.trunc(group_size)
    
    group_dict={}
    for i in range(0,num_of_groups):
        group_dict["group{0}".format(i)]=[]
        for k in range(int(i*group_size),int(group_size*(i+1))):
            if k > len(list_of_names):
                break
            else:
                group_dict["group{0}".format(i)].append(list_of_names[k])
    if len(list_of_names)%num_of_groups!=0:
    
        for group in group_dict.values():
            if len(group)== smallest_group:
                group.append('N/A')
    
                
    return group_dict

def remove_names(names):
    if names!=['none']:
        for i in names:
            list_of_names.remove(i)


st.set_page_config(
    page_title="Randomized Groups",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
col4,col5 = st.columns(2)
with col4:
    st.title("""
    Your Random Group Generator :open_hands:
    """)
    
with col5:
    st.header('This will generate your random groups. :sparkles:')
    


col2, col3 = st.columns(2)
with col2:
    st.subheader('This is where you input any missing students. :exclamation:')
    session.options = st.multiselect(label="Select student",options=list_of_names2)
    num_recs = st.slider('How many groups would you like?', 2, 10, 3)
buffer1, col1, buffer2 = st.columns([0.5, 1, 1])
is_clicked = col1.button(label="Group")


if is_clicked:

    remove_names(session.options)

    groups=group_selector(num_recs)
    with col3:
        st.subheader("These are your groups")
        st.table(groups)