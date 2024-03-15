import streamlit as st

st.header('Are You Snow-A-Mazing?')
st.write('We think you are! Someone likely sent you to this page to register for a BADGE. You\'re here to introduce yourself so that we\'ll know who to send your badge to, once you\'ve shown us that you are, in fact, Snow-A-Mazing!')

st.write('Begin by telling us who sent you...')
referred_by = st.selectbox('Who sent you to this app?', ('<choose one>','DORA', 'BUILD Event Moderator', 'Josh'))
time_for_step_2 = st.button ('Submit')

if time_for_step_2:
  st.write('They chose', referred_by)
  if referred_by == '<choose one>':
    st.write('You were supposed to choose a value from the list before you clicked the button.')
  elif referred_by == 'DORA':
    st.write('Yay DORA!')
  elif referred_by == 'BUILD Event Moderator':
    st.write('Yay BUILD!')
  else referred_by == 'Josh':
    st.write('Yay Josh!')
    
  
  
             
