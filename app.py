import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import 

st.header('Are You Snow-A-Mazing?')
st.write('Welcome to the learn.snowflake.com Workshop Badge Management app!')

uni_id = st.text_input('Enter your learn.snowflake.com UNI ID:')
uni_email = st.text_input('Enter your learn.snowflake.com EMAIL Address:')

st.write("TIPS:")
st.write("Your UNI ID can be found in the top-right corner of the workshop page. It begins with 053 and is a string of letters and numbers.")
st.write("Your learn.snowflake.com UNI_ID and EMAIL can be found at https://learn.snowflake.com/account/settings")
st.write("-----")

starts_right = uni_id[:3]

if starts_right == '005' and len(uni_id)<20 and len(uni_id)>17:
    st.write('Seems Legit')




  
  



badge_options = ('Badge 1: DWW', 'Badge 2: CMCW', 'Badge 3: DABW', 'Badge 4: DLKW', 'Badge 5: DNGW')

workshop = st.selectbox("Choose Workshop/Badge", options=badge_options, key=1)





  
  
             
