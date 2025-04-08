from main.downloadandformat import download_data


data = []

#Although it may not seem like much testing was done with these, the US Census API is terrible, and they have different
# codes for each census. For example, the code for 'total population' in the 2010 census is totally different than the
# 2020 census. And when there are 9,000+ codes for data, it is very easy to mess up.

def test_download2000():
    data = download_data("2000")
    assert (len(data) != 0) & (data != None)

def test_download2010():
    data = download_data("2010")
    assert (len(data) != 0) & (data != None)

def test_download2020():
    data = download_data("2020")
    assert (len(data) != 0) & (data != None)