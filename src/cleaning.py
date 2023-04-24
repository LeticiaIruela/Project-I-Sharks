import pandas as pd
import numpy as np

def data_frame_cleaning(df):
    df = df.dropna(how='all', axis=0)
    df= df.drop_duplicates(subset = ["Case Number.1", "Case Number.2"], inplace=False, keep="last")
    df= df.drop_duplicates(subset = ["href formula", "href"], inplace=False, keep="first")
    return df


def years_cleaning(df):
    df = df.dropna(subset=["Year"])
    df = df.dropna(subset=["Date"])
    df['New_Year'] = df['Date'] # create a new column with the same values as the original "Year" column
    df["All_years"] = df["New_Year"].str.extract("(\d{4})")
    df = df.dropna(subset=["All_years"])
    df['Year'] = df['Year'].astype(int)
    df['All_years'] = df['All_years'].astype(int)
    df.loc[df['Year'] < 1542, 'Year'] = df.loc[df['Year'] < 1542, 'All_years']
    return df

def country_cleaning(df):
    df.loc[df['Country'].isnull(), 'Country'] = df['Area'] 
    df.loc[df['Country'].isnull(), 'Country'] = df['Location']
    df = df.dropna(subset=["Country"])
    df['Country'] = df['Country'].str.upper()
    df.insert(5, "Oceans", "")
    north_atlantic = ['SENEGAL','GUINEA', 'COLUMBIA', 'USA', 'SCOTLAND', 'LIBERIA', 'MEXICO', 'VENEZUELA', 'OKINAWA', 'CAPE VERDE', 'BAHAMAS','CANADA', 'DENMARK', 'FAROE ISLANDS', 'GREENLAND', 'ICELAND', 'IRELAND', 'NORWAY', 'PORTUGAL', 'SPAIN', 'UNITED KINGDOM', 'ENGLAND', 'USA', 'BELGIUM', 'FRANCE', 'GERMANY', 'NETHERLANDS']
    south_atlantic = ['ANGOLA', 'NIGERIA', 'AZORES', 'NAMIBIA', 'ARGENTINA', 'BRAZIL', 'FALKLAND ISLANDS', 'GABON', 'NAMIBIA', 'SOUTH AFRICA', 'ST HELENA, BRITISH OVERSEAS TERRITORY', 'URUGUAY', 'ASCENSION ISLAND', 'BOUVET ISLAND', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'TRISTAN DA CUNHA']
    south_pacific = ['AUSTRALIA', 'NEW BRITAIN', 'NEW GUINEA','SAMOA','NEW CALEDONIA', 'CHILE', 'NEW ZEALAND','PAPUA NEW GUINEA','JOHNSTON ISLAND', 'SOLOMON ISLANDS', 'SOLOMON ISLANDS / VANUATU', 'COOK ISLANDS', 'EASTER ISLAND', 'FIJI', 'FRENCH POLYNESIA', 'KIRIBATI', 'NAURU', 'NIUE', 'NORFOLK ISLAND', 'PALAU', 'PAPUA NEW GUINEA', 'PITCAIRN ISLANDS', 'SOLOMON', 'TOKELAU', 'TONGA', 'TUVALU', 'VANUATU', 'AMERICAN SAMOA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'CORAL SEA ISLANDS', 'FEDERATED STATES OF MICRONESIA', 'FRENCH SOUTHERN AND ANTARCTIC LANDS', 'GUAM', 'HEARD ISLAND AND MCDONALD ISLANDS', 'MARSHALL ISLANDS', 'MIDWAY ISLANDS', 'NEW CALEDONIA', 'NIUE', 'NORFOLK ISLAND', 'NORTH KOREA', 'NORTHERN MARIANA ISLANDS', 'PALMYRA ATOLL', 'PAPUA NEW GUINEA', 'PITCAIRN ISLANDS', 'TIMOR-LESTE', 'TUVALU', 'WALLIS AND FUTUNA']
    north_pacific = ['CANADA', 'SIERRA LEONE','VIETNAM', 'SINGAPORE', 'SCOTLAND,' 'CHINA', 'JAPAN', 'RUSSIA', 'CAMBODIA', 'CHILE', 'COLOMBIA', 'COSTA RICA', 'ECUADOR', 'EL SALVADOR', 'GUATEMALA', 'HONDURAS', 'INDONESIA', 'KIRIBATI', 'NORTH KOREA', 'SOUTH KOREA', 'MARSHALL ISLANDS', 'MICRONESIA', 'NICARAGUA', 'PALAU', 'PANAMA', 'PHILIPPINES', 'RUSSIA', 'TAIWAN', 'THAILAND']
    indian_ocean= ['REUNION', 'KENYA', 'TANZANIA', 'MALDIVE ISLANDS', 'MADAGASCAR', 'COMOROS', 'MOZAMBIQUE', 'SOUTH AFRICA','MALDIVES', 'MAURITIUS', 'SOMALIA', 'SEYCHELLES', 'SRI LANKA', 'TANZANIA', 'MALAYSIA', 'MADAGASCAR']
    mediterranean_sea=['SPAIN', 'CRETE','ITALY', 'GREECE','MALTA', 'TUNISIA','TURKEY','LIBYA','LEBANON']
    red_sea=['ISRAEL','YEMEN', 'EGYPT','SUDAN']
    caribbean_sea=['PUERTO RICO', 'HAITI','GRENADA','BARBADOS','ARUBA', 'ANTIGUA','NICARAGUA', 'ST. MAARTIN', 'CUBA', 'TRINIDAD & TOBAGO', 'JAMAICA', 'CAYMAN ISLANDS', 'BRITISH VIRGIN ISLANDS', 'GRAND CAYMAN', 'COLOMBIA', 'DOMINICAN REPUBLIC', 'BELIZE', 'TURKS & CAICOS','BERMUDA']
    adriatic_sea=['MONTENEGRO', 'CROATIA']
    south_china_sea=['CHINA','HONG KONG']
    persian_golf=['UNITED ARAB EMIRATES','UNITED ARAB EMIRATES (UAE)','IRAQ','IRAN', 'SAUDI ARABIA']
    Bay_bengal_andaman_sea=['BURMA','MYANMAR','SRI LANKA', 'INDIA']
    for index, row in df.iterrows():
        if row['Country'] in north_atlantic:
            df.at[index, 'Oceans'] = 'North_Atlantic'
    for index, row in df.iterrows():
        if row['Country'] in south_atlantic:
            df.at[index, 'Oceans'] = 'South_Atlantic'
    for index, row in df.iterrows():
        if row['Country'] in north_pacific:
            df.at[index, 'Oceans'] = 'North_Pacific'
    for index, row in df.iterrows():
        if row['Country'] in south_pacific:
            df.at[index, 'Oceans'] = 'South_pacific'
    for index, row in df.iterrows():
        if row['Country'] in mediterranean_sea:
            df.at[index, 'Oceans'] = 'Mediterranean_Sea'
    for index, row in df.iterrows():
        if row['Country'] in caribbean_sea:
            df.at[index, 'Oceans'] = 'Caribbean_Sea'
    for index, row in df.iterrows():
        if row['Country'] in Bay_bengal_andaman_sea:
            df.at[index, 'Oceans'] = 'Bay_bengal_andaman_sea'
    for index, row in df.iterrows():
        if row['Country'] in red_sea:
            df.at[index, 'Oceans'] = 'Red_Sea'
    for index, row in df.iterrows():
        if row['Country'] in indian_ocean:
            df.at[index, 'Oceans'] = 'Indian_Ocean'
    for index, row in df.iterrows():
        if row['Country'] in south_china_sea:
            df.at[index, 'Oceans'] = 'South_China_Sea'
    for index, row in df.iterrows():
        if row['Country'] in persian_golf:
            df.at[index, 'Oceans'] = 'persian_golf'
    for index, row in df.iterrows():
        if row['Country'] in adriatic_sea:
            df.at[index, 'Oceans'] = 'Adriatic_Sea'
    ocean_rows = df['Country'].str.contains('OCEAN')
    ocean_names = df.loc[ocean_rows, 'Country'].str.extract(r'(\w+\sOCEAN)')
    df.loc[ocean_rows, 'Oceans'] = ocean_names.values
    ocean_dict = {
    'ATLANTIC OCEAN': 'North_Atlantic',
    'PACIFIC OCEAN': 'North_Pacific',
    'INDIAN OCEAN': 'Indian_Ocean',
    'PACIFC OCEAN': 'North_Pacific'}
    df['Oceans'] = df['Oceans'].replace(ocean_dict)
    no_ocean_applied=df['Oceans']==""
    df=df.drop(df[no_ocean_applied].index)
    return df

def time_cleaning(df):
    df = df.dropna(subset=["Time"])
    df['Cleaned_Time'] = df['Time'].str.extract(r'^(\d+)h')
    df.loc[df['Cleaned_Time'].str.contains(r'^\d{2}$') & df['Cleaned_Time'].notnull(), 'Time'] = df['Cleaned_Time']
    subset = df.loc[:, ['Time', 'Cleaned_Time']]
    df['time frame'] = df['Time'].str.extract(r'([a-zA-Z]{2,})').fillna('') #matches any sequence of 2 or more consecutive letters
    def set_time_frame(time):
        time = int(time)
        if 6 <= time <= 9:
            return 'Sunrise'
        elif 10 <= time <= 13:
            return 'Morning'
        elif 14 <= time <= 18:
            return 'Afternoon'
        else:
            return 'Night'
    df['Cleaned_Time'] = df['Cleaned_Time'].fillna(0).astype(int)
    df['Time frame'] = df['Cleaned_Time'].apply(set_time_frame)
