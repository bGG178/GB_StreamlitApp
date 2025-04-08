from requests import get
def download_data(year: str) -> dict:
    """
    Purpose:
        To retrieve US Census information
    Parameters:
        year: controls which Census to gather data from
    Returns:
        dictionary -> data or None to throw an error
    """

    additionalparms= {
        "Renter Occupied":"H10_010N",
        "Owner Occupied":"H10_002N",
        "Housing Units":"H1_001N",
    }



    if year == "2020":
        parms = "?get=NAME,P1_001N,H10_002N,H10_010N,H3_003N&for=state:*"
    elif year == "2010":
        parms = "?get=NAME,P001001,H014002,H004004,H003003&for=state:*"
    elif year == "2000":
        parms = "?get=NAME,P001001,H004002,H004003,H003003&for=state:*"


    yeartolink = {
        "2000" : "http://api.census.gov/data/2000/dec/cd110h",
        "2010" : "http://api.census.gov/data/2010/dec/cd115",
        "2020" : "http://api.census.gov/data/2020/dec/cd118"

    }

    print(yeartolink[year])
    link = yeartolink[year]
    #Setting up requests and returning the retrieved data
    try:
        print(link+parms)
        data = get(link+parms, headers={"User-Agent": "Mozilla/5.0"})
        data = data.json()
        return data

    #Passes exception if there is an error and returns None
    except Exception as e:
        print(f"Exception encountered {e}")
        return None

def formatdata(data,selected_options):
    """
    Purpose:
        To format data to look more visually appealing for page 3
    Parameters:
        :param data: Input data from the download_data function
        :param selected_options: Limits the states/regions that will be processed and returned
    Returns:
        :return: All the information, formatted in a way that it can be used to be displayed, reversing this is needed to
                display on graphs
    """
    print(data)
    population = []
    state = []
    rentedhomes = []
    ownedhomes =[]
    vacanthomes=[]
    vacancyrate= []
    data.pop(0) # Gets rid of uneccessary 'title' data
    for i in data:
        if i[0] in selected_options:
            i.pop()
            formatted = "{:,}".format(int(i[1]))
            population.append(formatted)
            state.append(i[0])
            formatted = "{:,}".format(int(i[2]))
            rentedhomes.append(formatted)
            formatted = "{:,}".format(int(i[3]))
            ownedhomes.append(formatted)
            formatted = "{:,}".format(int(i[4]))
            vacanthomes.append(formatted)
            vacancypercent=(((int(i[4])/(int(i[2])+int(i[3])))))
            vacancyrate.append("{:.2%}".format(vacancypercent))

    return state, population,ownedhomes,rentedhomes,vacanthomes,vacancyrate