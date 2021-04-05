import matplotlib.pyplot as plt 
import pandas as pd
import plotly.express as px
from iso_code_dict import cc3_cn

company_total = pd.read_csv("company_total.csv")
origin_occurences = pd.DataFrame(company_total.groupby("Country").count()["Employees"])
print(origin_occurences)#DEBUG
origin_occurences = origin_occurences.rename(columns = {"Employees":"Number of Fortune 500 HQs"})
list_origins = origin_occurences.index.tolist()

list_iso_codes = []
for country in list_origins:
    list_iso_codes.append(cc3_cn[country])

origin_occurences["ISO Code"] = list_iso_codes

fig = px.choropleth(origin_occurences, locations="ISO Code",
                    color="Number of Fortune 500 HQs", 
                    hover_name=origin_occurences.index, 
                    color_continuous_scale=px.colors.sequential.Teal, title = "Visualization of Countries With Global 500 Headquarters")
fig.show()