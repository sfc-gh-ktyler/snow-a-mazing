import streamlit as st

st.header('Are You Snow-A-Mazing?')
st.write('We think you are! Someone likely sent you to this page to register for a BADGE. You\'re here to introduce yourself so that we\'ll know who to send your badge to, once you\'ve shown us that you are, in fact, Snow-A-Mazing!')

st.write('Begin by telling us who sent you...')
referred_by = st.selectbox('Who sent you to this app?', ('<choose one>','DORA', 'BUILD Event Moderator', 'Josh'))
time_for_step_2 = st.button ('Submit')
                           

  
  
             
