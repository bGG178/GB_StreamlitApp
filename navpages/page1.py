import streamlit as st
import matplotlib.pyplot as plt
from main.downloadandformat import download_data, formatdata
from matplotlib.ticker import FuncFormatter



def show():
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

    selected_attributes = st.selectbox(
        "Select An Attribute to Compare Data",
        ["Population", "Owned Homes", "Rented Homes", "Vacant Homes", "Vacant Rate"]
    )

    if st.button("Generate Graph"):
        data2000 = download_data("2000")
        state2000, population2000, ownedhomes2000, rentedhomes2000, vacanthomes2000, vacancyrate2000 = formatdata(data2000, selected_options)
        data2010 = download_data("2010")
        state2010, population2010, ownedhomes2010, rentedhomes2010, vacanthomes2010, vacancyrate2010 = formatdata(data2010, selected_options)
        data2020 = download_data("2020")
        state2020, population2020, ownedhomes2020, rentedhomes2020, vacanthomes2020, vacancyrate2020 = formatdata(data2020, selected_options)

        if selected_attributes != None:

            population20number = []
            population10number = []
            population00number = []

            ownedhomes20number = []
            ownedhomes10number = []
            ownedhomes00number = []

            rentedhomes20number = []
            rentedhomes10number = []
            rentedhomes00number = []

            vacanthomes20number = []
            vacanthomes10number = []
            vacanthomes00number = []

            vacantrate20number = []
            vacantrate10number = []
            vacantrate00number = []

            for i in population2020:
                population20number.append(int(i.replace(",", "")))
            for i in population2010:
                population10number.append(int(i.replace(",", "")))
            for i in population2000:
                population00number.append(int(i.replace(",", "")))

            for i in ownedhomes2020:
                ownedhomes20number.append(int(i.replace(",", "")))
            for i in ownedhomes2010:
                ownedhomes10number.append(int(i.replace(",", "")))
            for i in ownedhomes2000:
                ownedhomes00number.append(int(i.replace(",", "")))

            for i in rentedhomes2020:
                rentedhomes20number.append(int(i.replace(",", "")))
            for i in rentedhomes2010:
                rentedhomes10number.append(int(i.replace(",", "")))
            for i in rentedhomes2000:
                rentedhomes00number.append(int(i.replace(",", "")))

            for i in vacanthomes2020:
                vacanthomes20number.append(int(i.replace(",", "")))
            for i in vacanthomes2010:
                vacanthomes10number.append(int(i.replace(",", "")))
            for i in vacanthomes2000:
                vacanthomes00number.append(int(i.replace(",", "")))

            for i in vacancyrate2020:
                vacantrate20number.append(float(i.replace("%", "")))
            for i in vacancyrate2010:
                vacantrate10number.append(float(i.replace("%", "")))
            for i in vacancyrate2000:
                vacantrate00number.append(float(i.replace("%", "")))

            coloroptions = [
                'blue', 'red', 'brown', 'green', 'purple', 'orange', 'pink', 'gray',
                'cyan', 'magenta', 'lime', 'teal', 'navy', 'gold', 'violet', 'indigo',
                'crimson', 'olive', 'maroon', 'turquoise', 'orchid', 'darkgreen', 'royalblue',
                'sienna', 'chocolate', 'slateblue', 'mediumseagreen', 'tomato', 'deepskyblue',
                'firebrick', 'dodgerblue', 'chartreuse', 'darkviolet', 'peru', 'mediumturquoise',
                'lawngreen', 'mediumorchid', 'forestgreen', 'darkorange', 'cadetblue', 'hotpink',
                'plum', 'lightseagreen', 'midnightblue', 'goldenrod', 'salmon', 'darkred',
                'powderblue', 'darkslategray', 'mediumspringgreen', 'lightcoral', 'steelblue',
                'darkcyan', 'royalpurple', 'lightgoldenrodyellow', 'seagreen', 'darkkhaki',
                'mistyrose', 'orangered'
            ]

            if selected_attributes == 'Population':
                formatter = FuncFormatter(lambda x, _: f'{x * 1e-6:.1f}M')
                plt.gca().yaxis.set_major_formatter(formatter)
                for i in range(len(selected_options)):
                    plt.plot(["2000","2010","2020"],[population00number[i],population10number[i],population20number[i]],marker='x',linestyle='-',label=state2000[i],color=coloroptions[i])

            if selected_attributes == 'Owned Homes':
                formatter = FuncFormatter(lambda x, _: f'{x * 1e-6:.1f}M')
                plt.gca().yaxis.set_major_formatter(formatter)
                for i in range(len(selected_options)):
                    plt.plot(["2000","2010","2020"],[ownedhomes00number[i],ownedhomes10number[i],ownedhomes20number[i]],marker='x',linestyle='-',label=state2000[i],color=coloroptions[i])

            if selected_attributes == 'Rented Homes':
                formatter = FuncFormatter(lambda x, _: f'{x * 1e-6:.1f}M')
                plt.gca().yaxis.set_major_formatter(formatter)
                for i in range(len(selected_options)):
                    plt.plot(["2000","2010","2020"],[rentedhomes00number[i],rentedhomes10number[i],rentedhomes20number[i]],marker='x',linestyle='-',label=state2000[i],color=coloroptions[i])

            if selected_attributes == 'Vacant Homes':
                formatter = FuncFormatter(lambda x, _: f'{x * 1e-6:.1f}M')
                plt.gca().yaxis.set_major_formatter(formatter)
                for i in range(len(selected_options)):
                    plt.plot(["2000","2010","2020"],[vacanthomes00number[i],vacanthomes10number[i],vacanthomes20number[i]],marker='x',linestyle='-',label=state2000[i],color=coloroptions[i])

            if selected_attributes == 'Vacant Rate':
                formatter = FuncFormatter(lambda x, _: f'{x:.2f}%')
                plt.gca().yaxis.set_major_formatter(formatter)

                for i in range(len(selected_options)):
                    plt.plot(["2000","2010","2020"],[vacantrate00number[i],vacantrate10number[i],vacantrate20number[i]],marker='x',linestyle='-',label=state2000[i],color=coloroptions[i])




            plt.title(f"Comparison of {selected_attributes} over time")
            plt.xlabel("Census Year")
            plt.ylabel("Values")



            plt.grid(True)

            plt.legend()

            st.pyplot(plt)