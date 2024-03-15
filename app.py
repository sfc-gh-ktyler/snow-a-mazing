import streamlit as st
import pandas as pd

st.header('Are You Snow-A-Mazing?')
st.write('You\'re here to introduce yourself so that we\'ll know who to send your badge to, once you\'ve shown us that you are, in fact, Snow-A-Mazing!')

badge_options = {"DORA": ['Badge 1: DWW', 'Badge 2: CMCW', 'Badge 3: DABW', 'Badge 4: DLKW', 'Badge 5: DNGW'], 
                "BUILD": ['Warsaw: 25 Mar 2024', 'Bay Area: 11 Apr 2024', 'Dallas: 25 Apr 2024'],
                 "SE": ['College 1', 'College 2', 'College 3']
                }


col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    name = st.selectbox("Choose Course Type", options=('<choose one>','DORA', 'BUILD', 'SE'), key=1)
with col2:
    prop = st.selectbox("Choose Workshop or Badge", options=badge_options.keys(), key=2)
with col3:
    unit = st.selectbox("Choose Unit", options=('Yes','No'), key=3)

if time_for_step_2:
  step = 2
  if referred_by == '<choose one>' and step ==2:
    st.write('Dude? Seriously? You were supposed to choose a value from the list before you clicked the button.')
  elif referred_by == 'DORA' and step ==2::
    st.write('Yay DORA!')
    workshop = st.selectbox('Which workshop/badge are you currently working on?', ())
    step_3_dora = st.button ('Submit Workshop Name')
    st.write('DORA Says: I love that workshop!' + workshop + 'is my FAVORITE of the Hands On Essentials Workshops!!')
  elif referred_by == 'BUILD Event Moderator':
    st.write('Yay BUILD!')
    build_local = st.selectbox('Which event are you currently attending?', ())
    step_3_build = st.button ('Submit Build Event')
  else:
    st.write('Yay Josh!')
    build_local = st.selectbox('Which SE College Course are you currently working on?', ('College A', 'College B', 'College C'))
    step_3_se_college = st.button ('Submit SE College')


  
  
             
