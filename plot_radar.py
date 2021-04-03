import matplotlib.pyplot as plt 
import pandas as pd 
from math import pi
import wikipedia_scrape

industries_occurence = wikipedia_scrape.fortune_dataframe.groupby("Industry").count()["Rank"]
industries = industries_occurence.index
num_angles = len(industries)
occurences = industries_occurence.append(pd.Series(industries_occurence[0]))
angles = [n / float(num_angles) * 2 * pi for n in range(num_angles)]
angles += angles[:1]
 
axes = plt.subplot(111, polar=True)

plt.xticks(angles[:-1], industries, color='grey', size=8)
 
axes.set_rlabel_position(0)
plt.yticks([3,6,9], ["3","6","9"], color="grey", size=7)
plt.ylim(0,10)

axes.plot(angles, occurences, 'g', linewidth=1, linestyle='solid')

axes.fill(angles, occurences, 'g', alpha=0.3)

plt.title('Occurences of the Various Industries in Our Data')

plt.show()

