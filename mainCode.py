# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# Defined CSV file name, axis names and values used in program
#  -> make the code flexible if used dataset changed
#  -> or to reuse the same function for a different file.
# ---------------------------------------------------------------------


csv_in_use = "retirementAge.csv"

# Colours for plots
colour_1 = "#2596be"
colour_2 = "#ec9d41"

# Axises used in program
y_axis_men = 'Average effective age of retirement, men (OECD)'
y_axis_women = 'Average effective age of retirement, women (OECD)'


# ---------------------------------------------------------------------
# FUNCTION: Read CSV data into Dataframe
# ---------------------------------------------------------------------

def read_retirement_data():

    """

    Loads the csv dataset defined in 'csv_in_use'

    Returns
    -------

    pandas Dataframe -> converts csv to df containing retirement data with year as the index

    """
    # Year set as index for line graph plots 
    retirement_df = pd.read_csv(csv_in_use, parse_dates=['Year'],  index_col='Year')

    return  retirement_df

# Call for function to be used for graphs
retirement_df =read_retirement_data()


# ---------------------------------------------------------------------
# FUNCTION: Get min and max value from CSV
# ---------------------------------------------------------------------

def min_max_index():

    """

    Loads the csv dataset defined in 'csv_in_use'

    Returns
    -------
    min_value -> integer, earliest year in the csv
    max_value -> integer, most recent year in the csv

    """
    
    # Passed in csv_in_use again as retirement_df wouldn't work as Year is the index col
    df = pd.read_csv(csv_in_use)
    min_value = df['Year'].min()
    max_value = df['Year'].max()
    
    return min_value, max_value


# ---------------------------------------------------------------------
# Masks for OECD and UK
# ---------------------------------------------------------------------

# Mask to get OECD data 
OECD_average = retirement_df[retirement_df['Entity'] == 'OECD average'].copy()

# Mask to get United Kingdom data
UK_average = retirement_df[retirement_df['Entity'] == 'United Kingdom'].copy()


# ---------------------------------------------------------------------
# FUNCTION: Plot OECD and UK women graph
# ---------------------------------------------------------------------

def plot_OECD_women_graph():

    """

    Plots both OECD women and UK women on the same graph


    """
    
    plot_retirement_women= OECD_average.plot(kind='line',y=y_axis_women, label='"Average effective age of retirement, women (OECD)"', color=colour_1, linestyle='-')
    # ax = puts both lines on the same plot
    UK_average.plot(kind='line',y=y_axis_women, label="Average effective age of retirement, women (UK)" ,ax = plot_retirement_women, color=colour_2, linestyle='--')
    plot_retirement_women.set_title("Retirement Age Over Time - Women ({min_value}-{max_value})")
    plt.show()


# ---------------------------------------------------------------------
# FUNCTION: Plot OECD and UK men graph
# ---------------------------------------------------------------------


def plot_OECD_men_graph():

    """

    Plots both OECD men and UK men on the same graph


    """
   
    plot_retirement_men= OECD_average.plot(kind='line',y= y_axis_men , label='Average effective age of retirement, men (OECD)', color=colour_1,  linestyle='-')
    # ax = puts both lines on the same plot
    UK_average.plot(kind='line',y= y_axis_men , label='Average effective age of retirement, men (UK)' ,ax = plot_retirement_men , color=colour_2, linestyle='--')
    plot_retirement_men.set_title("Retirement Age Over Time - Men ({min_value}-{max_value})")
    plt.show()


# ---------------------------------------------------------------------
# FUNCTION: Plot UK men and UK woman graph
# ---------------------------------------------------------------------

def plot_UK_men_women_graph():

    """  

    Plots both UK men and UK women on the same graph


    """
   
    plot_retirement_women= UK_average.plot(kind='line',y=y_axis_women, label='Average effective age of retirement, women (UK)', color=colour_1, linestyle='-')
    #ax = puts both lines on the same plot
    UK_average.plot(kind='line',y=y_axis_men, label="Average effective age of retirement, men (UK)" ,ax = plot_retirement_women, color=colour_2, linestyle='--')
    plot_retirement_women.set_title(f"Retirement Age Over Time - Men vs Women ({min_value}-{max_value})")
    plt.show()





# run program
if __name__ == "__main__":

    min_value, max_value = min_max_index()
    print(min_value)
    print(max_value)

    # Calling UK men vs UK women comparison graph
    plot_UK_men_women_graph()