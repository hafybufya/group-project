# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# Defined CSV file name, prompts and values used in program
#  -> make the code flexible if used dataset changed
#  -> or to reuse the same function for a different file.
# ---------------------------------------------------------------------


csv_in_use = "Retirement_Age.csv"
# colors for plots
colour_1 = "#2596be"
colour_2 = "#ec9d41"

#thiink about depth of hardocding. SHould i take out paths take out year to a diff name like how much shall i do.
#fetch the data

def read_retirement_data():
    '''
    reads Retirement_Age.csv file and parses the year column as a date and sets it as an index
    '''
    #GET RID OF HARDCODED PATH
    retirement_df = pd.read_csv(csv_in_use, parse_dates=['Year'],  index_col='Year')

    return  retirement_df

retirement_df =read_retirement_data()

def min_max_index():
    """getting min max of index"""
    df = pd.read_csv(csv_in_use)
    min_value = df['Year'].min()
    max_value = df['Year'].max()
    
    return min_value, max_value




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





# run program
if __name__ == "__main__":

    min_value, max_value = min_max_index()
    print(min_value)
    print(max_value)

    #Calling UK men vs UK women comparison graph
    plot_men_women_graph()