import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

# Fetch the data.

def read_retirement_data():
    '''
    reads Retirement_Age.csv file and parses the year column as a date and sets it as an index
    '''
    retirement_df = pd.read_csv('GroupProject/Retirement_Age.csv', parse_dates=['Year'],  index_col='Year')
    return retirement_df
    
retirement_df =read_retirement_data()

#mask to get OECD data 
OECD_average = retirement_df[retirement_df['Entity'] == 'OECD average'].copy()

#mask to get United Kingdom data
UK_average = retirement_df[retirement_df['Entity'] == 'United Kingdom'].copy()


#choosing based on when dates overlap in the dataset for OECD and UK
#improvement is so that the code dynamically selects when this overlap happens and fills up?
st_date=date(1970, 1, 1)
end_date=date(2018, 1, 1) 

#plotting both OECD women and UK same graph
plot_retirement_women= OECD_average[st_date:end_date].plot(kind='line',y='Average effective age of retirement, women (OECD)', label='"Average effective age of retirement, women (OECD)"')
#ax = puts both lines on the same plot
UK_average[st_date:end_date].plot(kind='line',y='Average effective age of retirement, women (OECD)', label="Average effective age of retirement, women (UK)" ,ax = plot_retirement_women)
plot_retirement_women.set_title("Retirement Age Over Time - Women (1970-2018)")


#plotting both OECD women and UK same graph
plot_retirement_men= OECD_average[st_date:end_date].plot(kind='line',y='Average effective age of retirement, men (OECD)', label='Average effective age of retirement, men (OECD)')
#ax = puts both lines on the same plot
UK_average[st_date:end_date].plot(kind='line',y='Average effective age of retirement, men (OECD)', label='Average effective age of retirement, men (UK)' ,ax = plot_retirement_men)
plot_retirement_men.set_title("Retirement Age Over Time - Men (1970-2018)")

plt.show()
