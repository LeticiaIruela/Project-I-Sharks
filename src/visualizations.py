import seaborn as sns
import matplotlib.pyplot as plt

def graf_oceans:
    sns.set_style("whitegrid")
    sns.set_palette("pastel")
    df_filtered = df8[(df8['Year'] >= 1950) & (df8['Year'] <= 2020)]
    df_filtered["Oceans"].value_counts().plot(kind="bar", title="Attacks from 1950 - 2018")
    plt.xticks(rotation=90, fontsize=10)
    plt.ylabel("Cases")
    plt.show()

def mainoceans_country:
    sns.set_style("whitegrid")
    sns.set_palette("pastel")
    oceans_to_include = ["North_Atlantic", "South_pacific", "Indian_Ocean"]
    df_filtered = df8[(df8['Year'] >= 1950) & (df8['Year'] <= 2018) & df8['Oceans'].isin(oceans_to_include)]
    top_countries = df_filtered.groupby('Oceans')['Country'].value_counts().groupby('Oceans').head(3).index.get_level_values('Country').tolist()
    sns.countplot(x='Oceans', hue='Country', data=df_filtered[df_filtered['Country'].isin(top_countries)],width=1)

def time_frame_attacks:
    sns.histplot(palette="mako", 
    x=df8[(df8.Oceans=="Noth_Atlantic")|(df8.Oceans=="South_Pacific")|(df8.Oceans=="Indian_Ocean")], 
    hue=df8[(df8.Country)].Country)
