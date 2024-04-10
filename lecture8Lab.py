
"""
EXCERCISE 1

Short: Open the data.

Long: In this repo is a file named "L08 LabData.csv". Use pandas to create a
datafrane named df. Explore it.
"""

"""
EXCERCISE 2

Short: Rename the variables to something sensible

Long: You will notice that the column names are IN ALLCAPS AS IF THEY WERE SHOUTING
AT YOU making them hard to read. Change their names into something easier to use.
Use a standalone dictionary object to ensure that you can easily make changes in
the future. Make sure that you use the Python naming conventions for variables
e.g. all lower case. You can look up the what each variable means in the 
associated Codebook which every dataset should come with. In this case it is a
 plain text file.

Hint: the following variable names are suggested: date, gdp, population, 
unemployment
"""

"""
EXCERCISE 3

Short: Make a GDP per capita column

Long: Create a new column called gdp_per_capita which is equal to the total GDP
divided by the population. The end result should be in dollars. 
Recall that GDP is in billions of dollars while population is in millions of
people.

Hint: the GDP per capita in 1947 should be around 17,000 dollars
"""

"""
EXCERCISE 4

Short: Fix the date column

Long: Whatever monster created this dataset seems to have used their own esoteric 
naming convention, truncating December to DCMBR. Awful! Panda's to_dateime module
cannot parse this. Create a function that will replace all instances of "31DCMBR"
in a string something that can be parsed by to_datetime such as "12-31-" and use
the map method to fix this column. Then use the to_datetime method to turn 
this column into a datetime object.
"""

"""
EXCERCISE 5

Short: Filter the dataset, so as to find all the 'good' years i.e. the years where the
rate of unemployment was less than 4.5%. How many were there?

Long: Create a dataframe called df_filtered that contains the rows for which 
the rate of unemployement is less than 4.5. Use df.shape to view the number of
rows remaining.

Hint: The answer should be 26
"""

"""
BONUS

Short: Find the rate of growth of GDP per capita. You may assume that it grows
exponentially, and that the rate of growth is constant.

Long: Recall that the model of exponential growth looks something like this:
    
    y_2023 = y_1947 * (R^t)
    
where y_1947 is the value in 1947, y_2023 is the value in 2023, R is the rate of
growth (or 1 + rate of growth) and t is the number of years since 1947. Here t = 76

Using logs and rearranging, we have 

log(R) = (log(y_2023) - log(y_1947)) / t

Hint: Note that the math package has a function log that can generate the log
of various numbers. So log(2,10) will give you log 2 to the base 10.

More: https://www.w3schools.com/python/ref_math_log.asp

To get the antilog of x, you can use then use 10 ** x

Hint: Find y_2023 and y_1947 by using the .loc method. You can look up the indexes
using .head() and .tail()
"""
