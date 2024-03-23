import streamlit as st
import pandas as pd

cnx=st.connection("snowflake")
                                              
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
    this_user_df =  uni_users_df.query('UNI_ID=="' + uni_id + '" & UNI_UUID=="'+ uni_uuid +'" ')
    user_rows = this_user_df.shape[0]
    
    if user_rows>=1:
        st.dataframe(this_user_df)
    else:
        st.write("There is no record of the UNI_ID/UUID combination you entered. Please double-check the info you entered, read the tips on the FINDING INFO tab, and try again") 

# Tabs
tab1, tab2, tab3 = st.tabs(["Edit Badge Info", "Finding Info", "Name Entry Rules"])
with tab1:
    st.subheader("Your Badge: Your Name & Email")
    st.write("We need your name for your badge. We want it to look nice. We have rules. Please follow them.")

    with st.form("badge_name_and_email"):
        st.write("Confirm Your Name and Email for Any Badges That Might Be Issued")     
        givenname = st.text_input("Given Name")
        middlename = st.text_input('Middle Name (Optional)')
        familyname = st.text_input('Family Name')
        cultural_order = st.checkbox('My culture displays my Family Name first. (e.g. Japanese, Korean, Chinese)')
        badge_order = st.checkbox('I would like the order of my name to appear: FAMILY NAME, Middle Name, First Name')
        email = st.text_input('Email Address I want associated with my badge:')

        submitted = st.form_submit_button("Update Badge Details")
        if submitted:
            
            session.call('amazing.app.UPDATE_BADGE_INFO_SP',firstname, middlename, lastname, email )
            st.success('Badge Info Updates', icon='🚀')
            st.experimental_rerun()
        st.markdown("""---""")         

with tab2:
    st.write("-----")
    st.subheader("FINDING YOUR INFORMATION:")
    st.write("In order to make edits, you must enter the correct combination of your UNI ID and the UUID we have assigned to you.")
    st.write("Your UNI ID can be found in the top-right corner of the workshop page. It begins with 053 and is a string of letters and numbers.")
    st.write("Your learn.snowflake.com UNI_UUID is displayed on the page of the workshop that linked you to this app.")
    st.write("-----")

with tab3:
    st.subheader("Our Very Nit-picky Name Rules")
    st.write("We want your name to look nice on your badge(s). We want your badge(s) to accurately represent your name and securely represent your accomplishments.")
    st.write("Because of this, we have rules around what names can and should be used. If your entries fail, read over these rules until you figure out what went wrong.")
    st.write("-----")

    st.write("What is a middle name?")
    st.write("In US culture, a middle name is a name that appears on official documents but is often not used in more casual settings.")
    st.write("Not every US citizen is given a middle name by their parents so it can be left blank. Do NOT put an X to represent the lack of a middle name. This looks ugly on a badge."
    st.write("For badge purposes, a middle name can be used for a given middle name, or a nickname or an alternate script version of the family and given names.")
    st.write("* NICKNAME Example: Harold \"Harry\" Simpson (common way to display a nickname in the US)")
    st.write("* KOREAN Example: 전 Jeon Joon-kook 정국  (with Roman script used in Middle Name field. Hangule used in First and Family name fields)" )
    st.write("* UKRANIAN Example: Volodymyr Володимир Зеленський Zelenskyy (with Cyrillic script used in Middle Name field, Roman script in First and Family Name fields.)")

    
  
    st.write("CHARACTER CASE RULES:")
    st.write("* Proper Mixed Case is required for given names and middle names. (Initial-letter capitalization)")
    st.write("* ALL UPPER CASE is allowed for family names.")
    st.write("* All lower case is allowed for in family names for nobiliary particles like van, van der, de, de la, etc. but the other parts of the family name should be mixed case.")

    st.write("NAME LENGTH RULES:")
    st.write("We recognize that East Asian names can sometimes be very few characters. Southeast Asian and Spanish names can sometimes be many, many characters.")
    st.write("We do not like the recent Southeast Asian trend of using a few initials as a last name. e.g. Kumar KS is not a good badge name because there are too many Kumar KS\'s in the world.")
    st.write("If you are Southeast Asian, please use the longer version of your name - not a given name followed by initials for the family names.")

             
             
             

             
            
             
             

         


starts_right = uni_id[:3]

if starts_right == '005' and len(uni_id)<20 and len(uni_id)>17:
    st.write('Seems Legit')




  
  



badge_options = ('Badge 1: DWW', 'Badge 2: CMCW', 'Badge 3: DABW', 'Badge 4: DLKW', 'Badge 5: DNGW')

workshop = st.selectbox("Choose Workshop/Badge", options=badge_options, key=1)





  
  
             
