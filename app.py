import streamlit as st
import pandas as pd

st.header('Are You Snow-A-Mazing?')
st.write('You\'re here to introduce yourself so that we\'ll know who to send your badge to, once you\'ve shown us that you are, in fact, Snow-A-Mazing!')

badge_options = {"Essentials/DORA": ['Badge 1: DWW', 'Badge 2: CMCW', 'Badge 3: DABW', 'Badge 4: DLKW', 'Badge 5: DNGW'], 
                "BUILD Workshop": ['Warsaw: 25 Mar 2024', 'Bay Area: 11 Apr 2024', 'Dallas: 25 Apr 2024'],
                 "SE College": ['College 1', 'College 2', 'College 3']
                }


col1, col2 = st.columns([1, 1])
with col1:
    type = st.selectbox("Choose Course Type", options=badge_options.keys(), key=1)
with col2:
    course = st.selectbox("Choose Workshop or Badge", options=badge_options[type], key=2)

email = st.text_input('Enter your email address:')




  
  
             
