"""
Grant Bowers
3/23/25
app.py
streamlit_app project

ChatGPT helped a ton with learning many of the basic functionalities of Streamlit, it also helped with many of the tedious tasks
Such as reformatting large portions of code for me
"""
import streamlit as st
import sys
import os

#Ensures app.py can run from within a main folder, instead of root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))



st.set_page_config(page_title="US Census Data Displayer", layout="wide",page_icon="🦅")

st.sidebar.title("US Census Info Camparison Method Navigator")
page = st.sidebar.radio("Go to", ["Home", "Timeline", "Data Visualization","Raw Data List"])

if page == "Home":
    st.title("US Census Information Grapher")
    st.header("Project to retrieve information from the web")
    st.header("This particular project retrieves certain aspects of US Census data")
    st.text("FUN FACT! Did you know: The US Census website has around 2,000 datasheets and aggregate reports based off of a litany of census data!")
    st.text("Each of these, especially the Decennial US Census (which this project is based on) has upwards of 9,000 variables to request with the API!")
    st.text("Fun fact part 2, each of these 2,000 documents also have almost no consistent codes, meaning the code to fetch population for the 2020 census is not related to the code used to fetch the same data in the 2010 census!😁😁😁😁😁😁")
    st.image("Images/uscensusgif.gif",caption="Thank you US gov API!")
    st.text("Heres a fun gif of me scrolling through SOME of the census data!")
    st.subheader("-GB")
elif page == "Timeline":
    from navpages import page1
    page1.show()

elif page == "Data Visualization":
    from navpages import page2
    page2.show()

elif page == "Raw Data List":
    from navpages import page3
    page3.show()
