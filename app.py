import streamlit as st

st.header('Are You Snow-A-Mazing?')
st.write('You\'re here to introduce yourself so that we\'ll know who to send your badge to, once you\'ve shown us that you are, in fact, Snow-A-Mazing!')
step = 1

st.write('Begin by telling us who sent you...')
referred_by = st.selectbox('Who sent you to this app?', ('<choose one>','DORA', 'BUILD Event Moderator', 'Josh'))
time_for_step_2 = st.button ('Submit Referrer')

if time_for_step_2:
  step = 2
  if referred_by == '<choose one>' and step ==2:
    st.write('Dude? Seriously? You were supposed to choose a value from the list before you clicked the button.')
  elif referred_by == 'DORA' and step ==2::
    st.write('Yay DORA!')
    workshop = st.selectbox('Which workshop/badge are you currently working on?', ('Badge 1: DWW', 'Badge 2: CMCW', 'Badge 3: DABW', 'Badge 4: DLKW', 'Badge 5: DNGW'))
    step_3_dora = st.button ('Submit Workshop Name')
    st.write('DORA Says: I love that workshop!' + workshop + 'is my FAVORITE of the Hands On Essentials Workshops!!')
  elif referred_by == 'BUILD Event Moderator':
    st.write('Yay BUILD!')
    build_local = st.selectbox('Which event are you currently attending?', ('Warsaw: 25 Mar 2024', 'Bay Area: 11 Apr 2024', 'Dallas: 25 Apr 2024'))
    step_3_build = st.button ('Submit Build Event')
  else:
    st.write('Yay Josh!')
    build_local = st.selectbox('Which SE College Course are you currently working on?', ('College A', 'College B', 'College C'))
    step_3_se_college = st.button ('Submit SE College')


  
  
             
