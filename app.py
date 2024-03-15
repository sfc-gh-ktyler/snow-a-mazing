import streamlit as st

st.header('Are You Snow-A-Mazing?')
st.write('We think you are! Someone likely sent you to this page to register for a BADGE. Maybe you came from learn.snowflake.com? Or from a Snowflake BUILD event? In any case, you\'re here to introduce yourself so that we\'ll know who to send your badge to, once you\'ve shown us that you are, in fact, Snow-A-Mazing!')

st.write("Begin by telling us who sent you...")
referred_by = st.selectbox("Who sent you to this app?", ("DORA", "BUILD Event Moderator", "Josh")
st.write(referred_by)
                           
st.stop()
if referred_by == "BUILD Event Moderator":
  my_event = st.selectbox("What event are you attending?", ("Warsaw -  25 Mar 2024", "Bay Area - 11 Apr 2024","Dallas - 25 Apr 2024"))
else if referred_by == "DORA":
  my_workshop = st.selectbox("Which workshop/badge are you working on?", ("Badge 1: DWW", "Badge 2: CMCW", "Badge 3: DABW", "Badge 4: DLKW", "Badge 5:DNGW"))
  
             
