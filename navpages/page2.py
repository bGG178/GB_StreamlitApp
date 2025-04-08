import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from main.downloadandformat import download_data, formatdata
from matplotlib.ticker import FuncFormatter

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




    attributeoption = [
        "Population","Owned Homes", "Rented Homes", "Vacant Homes"
    ]

    select_all_attributes = st.checkbox("Select All Attributes to Compare Data")

    if select_all_attributes:
        selected_attributes = attributeoption
    else:
        selected_attributes = st.multiselect("Choose Attributes:", attributeoption)

    if st.button("Show Data"):

        data = download_data(option)
        state, population, ownedhomes, rentedhomes, vacanthomes, vacancyrate = formatdata(data, selected_options)


        if selected_attributes != None:


            barwidth = 0.2
            index = np.arange(len(state))
            plt.figure(figsize=(12, 6))
            populationnumber = []
            ownedhomesnumber = []
            rentedhomesnumber = []
            vacanthomesnumber = []
            for i in population:
                populationnumber.append(int(i.replace(",","")))
            print(populationnumber)
            for i in ownedhomes:
                ownedhomesnumber.append(int(i.replace(",", "")))
            print(ownedhomesnumber)
            for i in rentedhomes:
                rentedhomesnumber.append(int(i.replace(",", "")))
            print(rentedhomesnumber)
            for i in vacanthomes:
                vacanthomesnumber.append(int(i.replace(",", "")))
            print(vacanthomesnumber)

            if "Owned Homes" in selected_attributes:

                plt.bar(index-barwidth, ownedhomesnumber,barwidth,label="Owned")

            if "Rented Homes" in selected_attributes:
                plt.bar(index, rentedhomesnumber,barwidth,label="Rented")

            if "Vacant Homes" in selected_attributes:
                plt.bar(index+barwidth, vacanthomesnumber,barwidth,label="Vacant")
            if "Population" in selected_attributes:
                plt.bar(index+barwidth+barwidth, populationnumber,barwidth,label="Population")



            plt.title("State Housing Demographics")
            plt.xlabel("States")
            plt.ylabel("Count")

            if select_all or len(selected_options)>13:
                plt.xticks(index,state,rotation=45,fontsize = 8)
            else:
                plt.xticks(index,state)

            plt.legend()

            formatter = FuncFormatter(lambda x, _: f'{x * 1e-6:.1f}M')
            plt.gca().yaxis.set_major_formatter(formatter)

            plt.grid(True)

            st.pyplot(plt)


