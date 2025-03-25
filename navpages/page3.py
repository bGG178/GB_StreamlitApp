import os

import json
from datetime import date
import sys
import streamlit as st
import pandas as pd
from downloadandformat import download_data, formatdata

def show():

    option = st.selectbox(
        "Choose which census to gather data from",
        ["2000","2010","2020"]
    )

    stateoption = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
        "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
        "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
        "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
        "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
        "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming",
        "District of Columbia", "Puerto Rico"
        ]

    select_all = st.checkbox("Select All Regions to Gather Data")

    if select_all:
        selected_options = stateoption
    else:
        selected_options = st.multiselect("Choose States:",stateoption)

    if st.button("Generate Data"):
        if option != None:
            data = download_data(option)

            state,population,ownedhomes,rentedhomes,vacanthomes,vacancyrate = formatdata(data,selected_options)

            df = pd.DataFrame({
                'Region': state,
                'Population': population,
                'Owned Homes': ownedhomes,
                'Rented Out Homes': rentedhomes,
                'Vacant Homes':vacanthomes,
                'Vacancy Rate': vacancyrate
            })

            st.table(df)  # Static table
