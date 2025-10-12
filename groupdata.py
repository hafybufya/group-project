import pandas as pd
import matplotlib.pyplot as plt




# colors for plots
OECD_color = "#2596be"
UK_color = "orange"
#fetch the data

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


#plotting both OECD women and UK same graph
plot_retirement_women= OECD_average.plot(kind='line',y='Average effective age of retirement, women (OECD)', label='"Average effective age of retirement, women (OECD)"', color=OECD_color, linestyle='-')
#ax = puts both lines on the same plot
UK_average.plot(kind='line',y='Average effective age of retirement, women (OECD)', label="Average effective age of retirement, women (UK)" ,ax = plot_retirement_women, color=UK_color, linestyle='--')
plot_retirement_women.set_title("Retirement Age Over Time - Women (1970-2018)")

#plotting both OECD women and UK same graph
plot_retirement_men= OECD_average.plot(kind='line',y='Average effective age of retirement, men (OECD)', label='Average effective age of retirement, men (OECD)', color=OECD_color,  linestyle='-')

#ax = puts both lines on the same plot
UK_average.plot(kind='line',y='Average effective age of retirement, men (OECD)', label='Average effective age of retirement, men (UK)' ,ax = plot_retirement_men , color=UK_color, linestyle='--')

#unhardcode numbers
plot_retirement_men.set_title("Retirement Age Over Time - Men (1970-2018)")


#plotting both UK men and women on the graph
plot_retirement_women= UK_average.plot(kind='line',y='Average effective age of retirement, women (OECD)', label='Average effective age of retirement, women (UK)', color=OECD_color, linestyle='-')
#ax = puts both lines on the same plot
UK_average.plot(kind='line',y='Average effective age of retirement, men (OECD)', label="Average effective age of retirement, men (UK)" ,ax = plot_retirement_women, color=UK_color, linestyle='--')
plot_retirement_women.set_title("Retirement Age Over Time - Men vs Women (1970-2018)")

plt.axvline(x=2010, color='grey', linestyle='--', linewidth=1)
plt.text(2010.5, 67, 'Equalisation of State Pension Age begins', rotation=90, va='bottom', color='grey')

plt.style.use("seaborn-v0_8")

plt.show()

