import pandas as pd
import squarify
from matplotlib import pyplot as plt

company_type = pd.read_csv("company_type.csv")
type_occurences = company_type.groupby("Company Type").count()["Company Name"]

squarify.plot(sizes = type_occurences, label = type_occurences.index, alpha = .8 )

plt.title("The Types of Companies That Make Up the Largest Companies List")
plt.axis("off")
plt.show()