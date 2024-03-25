import streamlit as st
import pandas as pd

cnx=st.connection("snowflake")
session = cnx.session()
if 'auth_status' not in st.session_state:
    st.session_state['auth_status'] = 'not_authed'

st.session_state

st.header('Are You Snow-A-Mazing?')
st.write('Welcome to the learn.snowflake.com Workshop Badge Management app!')

uni_id = st.text_input('Enter your learn.snowflake.com UNI ID:')
uni_uuid = st.text_input('Enter the secret UUID displayed on the DORA is Listening Page:')
find_my_uni_record = st.button("Find my UNI User Info")

if find_my_uni_record:
    this_user_sql =  "select badge_given_name, badge_middle_name, badge_family_name, badge_email from UNI_USER_BADGENAME_BADGEEMAIL where UNI_ID='" + uni_id + "' and UNI_UUID='"+ uni_uuid +"'"
    this_user_df = session.sql(this_user_sql)
    user_results = this_user_df.to_pandas()                          
    user_rows = user_results.shape[0]
        
    if user_rows>=1:
        st.session_state['auth_status'] = 'authed'
        if 'uni_id' not in st.session_state:
            st.session_state['uni_id'] = uni_id
            
        if 'given_name' not in st.session_state:
            st.session_state['given_name'] = user_results['BADGE_GIVEN_NAME'].iloc[0]
        
        if 'middle_name' not in st.session_state:
            st.session_state['middle_name'] = user_results['BADGE_MIDDLE_NAME'].iloc[0]
        
        if 'family_name' not in st.session_state:
            st.session_state['family_name'] = user_results['BADGE_FAMILY_NAME'].iloc[0]
            
        if 'badge_email' not in st.session_state:
            st.session_state['badge_email'] = user_results['BADGE_EMAIL'].iloc[0]
    else:
        st.write("There is no record of the UNI_ID/UUID combination you entered. Please double-check the info you entered, read the tips on the FINDING INFO tab, and try again") 

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["View Your Name and Email", "Edit Your Name and Email","Finding Your Information", "Name Entry Rules"])

with tab1:
    st.subheader("Your Name and Email - Currently Stored in Our System")
    if st.session_state.auth_status == 'authed':
        st.markdown("**GIVEN NAME:** " + st.session_state.given_name)
        st.markdown("**MIDDLE/ALTERNATE NAME:** "+ st.session_state.middle_name) 
        st.markdown("**FAMILY NAME:** " + st.session_state.family_name)
        st.markdown("**EMAIL:**" + st.session_state.badge_email)
        st.write("-----")
        st.markdown("*If you would like to make changed, edit your information on the next tab*")
    else:
        st.write("Please sign in using your UNI_ID and UUID in the section above.")

with tab2:
    st.subheader("Edit or Confirm Your Name for Your Badge(s)")

    if st.session_state.auth_status == 'authed':
        with st.form("badge_name_and_email"):
            st.write("Confirm Your Name for Any Badges That Might Be Issued")     
            edited_given = st.text_input("Given Name (Name used to greet you)", st.session_state.given_name)
            edited_middle = st.text_input('Middle Name/Nickname/Alternate-Spelling (Optional)', st.session_state.middle_name)
            edited_family = st.text_input('Family Name', st.session_state.family_name)
            name_has_nobiliary = st.checkbox("My family name has a nobiliary particle. No changes should be made to lower-case parts of my last name (e.g. von, von de, von der, de, da, de la etc)")
            
            badge_name_order = st.radio("Name Display Order You Prefer:",                            
                                   ["[Given] [Middle] [Family]","[FAMILY] [Alternate-Spelling] [Given]", "[FAMILY] [Given] [Middle]", "[Given] [Middle] [FAMILY]"],
                                   captions = ["Common in Anglo Traditions", "Good for including alternate script names", "East Asian Standard Order", "Common for French and Francophonic"]
                                   )
            submit_edits = st.form_submit_button("Show My Badge Name")

            if submit_edits:
                if badge_name_order == "[Given] [Middle] [Family]" and name_has_nobiliary==True:
                    name_test = edited_given.capitalize() + " " + edited_middle.capitalize() + " " + edited_family
                    st.markdown("Your name will appear on your badge as: **" + name_test + "**")
                elif badge_name_order == "[Given] [Middle] [Family]" and name_has_nobiliary==False: 
                    name_test = edited_given.capitalize() + " " + edited_middle.capitalize() + " " + edited_family.capitalize() 
                    st.markdown("Your name will appear on your badge as: " + name_test)
                elif badge_name_order == "[FAMILY] [Alternate-Spelling] [Given]": 
                    name_test = edited_family.upper() + " " + edited_middle + " " + edited_given.capitalize() 
                    st.markdown("Your name will appear on your badge as: " + name_test)
                elif badge_name_order == "[FAMILY] [Given] [Middle]": 
                    name_test = edited_family.upper() + " " + edited_given.capitalize() + " " +  edited_middle.capitalize() 
                    st.markdown("Your name will appear on your badge as: " + name_test)
                elif badge_name_order == "[Given] [Middle] [FAMILY]":
                    name_test = edited_given.capitalize() + " " +  edited_middle.capitalize() + " " + edited_family.upper()
                    st.markdown("Your name will appear on your badge as: " + name_test)
                else: 
                    st.write('Choose a format for your name')
               
        if submit_edits:
            #session.call('amazing.app.UPDATE_BADGE_INFO_SP',firstname, middlename, lastname )
            #st.success('Badge Info Updates', icon='🚀')
            #st.experimental_rerun()
            st.markdown("""---""")         
    else:
        st.write("Please sign in using your UNI_ID and UUID in the section above.")

with tab3:
    st.subheader("Finding Your Login Information:")
    st.write("In order to make edits, you must enter the correct combination of your UNI ID and the UUID we have assigned to you.")
    st.write("Your UNI ID can be found in the top-right corner of the workshop page. It begins with 053 and is a string of letters and numbers.")
    st.write("Your learn.snowflake.com UNI_UUID is displayed on the page of the workshop that linked you to this app.")

with tab4:
    st.subheader("Our Very Nit-picky Name Rules")
    st.write("We want your name to look nice on your badge(s). We want your badge(s) to accurately represent your name and securely represent your accomplishments.")
    st.write("Because of this, we have rules around what names can and should be used. If your entries fail, read over these rules until you figure out what went wrong.")
    st.write("-----")

    st.write("WHAT IS A MIDDLE NAME?")
    st.write("In US culture, a middle name is a name that appears on official documents but is often NOT used in more casual settings.")
    st.write("Not every US citizen is given a middle name by their parents, so it can be left blank. Do NOT put an X to represent the lack of a middle name. This looks ugly on a badge.")
    st.write("For badge purposes, the middle name field can be used for a given middle name, a nickname, or an alternate script version of the family and given names.")
    st.write("* NICKNAME Example: Harold (Harry) Simpson. Using quotes or parenthesis in the middle name is a common way to display a nickname in the US.")
    st.write("* KOREAN Example: 전 Jeon Joon-kook 정국  (with Roman script used in Middle Name field. Hangul used in Given and Family name fields)" )
    st.write("* UKRANIAN Example: Volodymyr Володимир Зеленський Zelenskyy (with Cyrillic script used in Middle Name field, Roman script in Given and Family name fields.)")
    st.write("-----")
    st.write("CHARACTER CASE RULES:")
    st.write("* Proper Mixed Case is required for given names and middle names. (Initial-letter capitalization except for Nobiliary particles.)")
    st.write("* ALL UPPER CASE is allowed for Family names.")
    st.write("* All lower case is NOT allowed for Given or Middle name parts.")
    st.write("-----")
    st.write("NAME LENGTH RULES:")
    st.write("We recognize that East Asian names can sometimes be very few characters. Southeast Asian and Spanish names can sometimes be many, many characters.")
    st.write("We do not like the recent Southeast Asian trend of using a few initials as a last name. e.g. Kumar KS is not a good badge name because there are too many Kumar KS\'s in the world.")
    st.write("If you are Southeast Asian (eg Indian or Pakistani), please use the longer version of your name - not a given name followed by initials for the family names.")
    st.write("We check for name length so please use name that is long enough to be distinctive. Imagine that someone wants to challenge you by claiming your badge as theirs. You will want a name distinctive enough that you can prove the badge belongs to you, and not some one else with a similar name")
    st.write("-----")
    starts_right = uni_id[:3]

    if starts_right == '005' and len(uni_id)<20 and len(uni_id)>17:
        st.write('Seems Legit')

        badge_options = ('Badge 1: DWW', 'Badge 2: CMCW', 'Badge 3: DABW', 'Badge 4: DLKW', 'Badge 5: DNGW')

        workshop = st.selectbox("Choose Workshop/Badge", options=badge_options, key=1)





  
  
             
