import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd

st.header('Are You Snow-A-Mazing?')
st.write('You\'re here to introduce yourself so that we\'ll know who to send your badge to, once you\'ve shown us that you are, in fact, Snow-A-Mazing!')

st.write("Your UNI ID can be found in the top-right corner of the workshop page. It begins with 053 and is a string of letters and numbers.")
uni_id = st.text_input('Enter your learn.snowflake.com UNI ID:')

starts_right = uni_id[:3]
st.write(starts_right)
if starts_right == '005':
  st.write('So far so good')





  
  



badge_options = ('Badge 1: DWW', 'Badge 2: CMCW', 'Badge 3: DABW', 'Badge 4: DLKW', 'Badge 5: DNGW')

workshop = st.selectbox("Choose Workshop/Badge", options=badge_options, key=1)





  
  
             
