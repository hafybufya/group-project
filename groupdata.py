import pandas as pd
import matplotlib.pyplot as plt

# colors for plots
colour_1 = "#2596be"
colour_2 = "orange"

#thiink about depth of hardocding. SHould i take out paths take out year to a diff name like how much shall i do.
#fetch the data

def read_retirement_data():
    '''
    reads Retirement_Age.csv file and parses the year column as a date and sets it as an index
    '''
    retirement_df = pd.read_csv('GroupProject/Retirement_Age.csv', parse_dates=['Year'],  index_col='Year')
    return retirement_df
    
retirement_df =read_retirement_data()


#Finding the lowest and highest year defo should be done
min_value = retirement_df['Year'].min()
max_value = retirement_df['Year'].max()
print('Min: ', min_value)
print('Max: ', max_value)

#mask to get OECD data 
OECD_average = retirement_df[retirement_df['Entity'] == 'OECD average'].copy()

#mask to get United Kingdom data
UK_average = retirement_df[retirement_df['Entity'] == 'United Kingdom'].copy()



def plot_OEC_women_graph():
#plotting both OECD women and UK same graph
    plot_retirement_women= OECD_average.plot(kind='line',y='Average effective age of retirement, women (OECD)', label='"Average effective age of retirement, women (OECD)"', color=colour_1, linestyle='-')
    UK_average.plot(kind='line',y='Average effective age of retirement, women (OECD)', label="Average effective age of retirement, women (UK)" ,ax = plot_retirement_women, color=colour_2, linestyle='--')
    plot_retirement_women.set_title("Retirement Age Over Time - Women (1970-2018)")
    plt.show()


def plot_OECD_men_graph():
    #plotting both OECD women and UK same graph
    plot_retirement_men= OECD_average.plot(kind='line',y='Average effective age of retirement, men (OECD)', label='Average effective age of retirement, men (OECD)', color=colour_1,  linestyle='-')
    #ax = puts both lines on the same plot
    UK_average.plot(kind='line',y='Average effective age of retirement, men (OECD)', label='Average effective age of retirement, men (UK)' ,ax = plot_retirement_men , color=colour_2, linestyle='--')
    #unhardcode numbers
    plot_retirement_men.set_title("Retirement Age Over Time - Men (1970-2018)")
    plt.show()


def plot_men_women_graph():

    #plotting both UK men and women on the graph
    plot_retirement_women= UK_average.plot(kind='line',y='Average effective age of retirement, women (OECD)', label='Average effective age of retirement, women (UK)', color=colour_1, linestyle='-')
    #ax = puts both lines on the same plot
    UK_average.plot(kind='line',y='Average effective age of retirement, men (OECD)', label="Average effective age of retirement, men (UK)" ,ax = plot_retirement_women, color=colour_2, linestyle='--')
    plot_retirement_women.set_title("Retirement Age Over Time - Men vs Women (1970-2018)")
    plt.show()



#Calling UK men vs UK women comparison graph
plot_men_women_graph()

