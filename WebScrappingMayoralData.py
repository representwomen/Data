import pandas as pd
from datetime import datetime

# pull current year to update the url call based on the year
currentYear = datetime.now().year

# check to make sure we have the correct year
print (currentYear)

# If the URL needs updating, update it below
url ='https://cawp.rutgers.edu/levels_of_office/women-mayors-us-cities-'+str(currentYear)

# check to make sure we have the correct url
print(url)

# read the url into a dataframe
dfs = pd.read_html(url,header=0, match='Vivian Jones', encoding='utf-8')

print(len(dfs[0]))

for df in dfs:
    print(df)

dfs[0]

# print dataframe to csv
dfs[0].to_csv(str(currentYear)+"mayorsover30000.csv", sep=',', encoding='utf-8')

readme = open("READ_ME","w+")
readme.write("You will need to find a few names with accents and hand-fix the weird characters that get substituted for the letters with accents. Additionally, the 'Rank' column is for the rank of the city in terms of population, that's why there are so many numbers missing. Otherwise you should be good to go!\n If you have additional questions email me at harbert.marilyn@gmail.com\n-Marilyn Harbert")
readme.close()
