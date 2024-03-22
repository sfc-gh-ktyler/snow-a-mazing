import streamlit as st
import pandas as pd

# Load the table as a dataframe using the Snowpark Session.
@st.cache_data
def load_uni_users():
    session = cnx.session()
    return session.table("UNI_USER_UUID").to_pandas()

uni_users_df = load_uni_users()

st.header('Are You Snow-A-Mazing?')
st.write('Welcome to the learn.snowflake.com Workshop Badge Management app!')

uni_id = st.text_input('Enter your learn.snowflake.com UNI ID:')
uni_uuid = st.text_input('Enter the secret UUID displayed on the DORA is Listening Page:')
find_my_uni_record = st.button("Find my UNI User Info")

if find_my_uni_record:
    #this_user_df =  uni_users_df.query('UNI_ID=="005VI0000052bmzYAA" & =="femke.van.verseveld@inergy.nl" ')
    this_user_df =  uni_users_df.query('UNI_ID=="' + uni_id + '" & UNI_UUID=="'+ uni_uuid +'" ')
    user_rows = this_user_df.shape[0]
    
    if user_rows>=1:
        st.dataframe(this_user_df)
    else:
        st.write("There is no record of the UNI_ID/EMAIL combination you entered. Please double-check the info you entered, read the tips below, and try again") 

st.write("-----")
st.subheader("TIPS:")
st.write("Your UNI ID can be found in the top-right corner of the workshop page. It begins with 053 and is a string of letters and numbers.")
st.write("Your learn.snowflake.com UNI_ID and EMAIL can be found at https://learn.snowflake.com/account/settings")
st.write("-----")


st.write("You're too legit to quit!")

starts_right = uni_id[:3]

if starts_right == '005' and len(uni_id)<20 and len(uni_id)>17:
    st.write('Seems Legit')




  
  



badge_options = ('Badge 1: DWW', 'Badge 2: CMCW', 'Badge 3: DABW', 'Badge 4: DLKW', 'Badge 5: DNGW')

workshop = st.selectbox("Choose Workshop/Badge", options=badge_options, key=1)





  
  
             
