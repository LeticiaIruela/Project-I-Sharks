# Project-I-Sharks

## 0. Introduction

On this project, the main goal is to clean the data of the provided attacks.csv* file using pandas. Additionaly, we will define some functions to run the code and we will execute some visualizations to present the findings.
*The data is extracted from www.kaggle.com.



## 1. Project description

Firstly we re going to provide a brief overview of the all he aspects involved in the project and what we want to achive with our analysys.
In order to clean acuratey our data based, we set the researh main question to focus the cleaning.

---------------------------------------**VALIDATION**--------------------------------------
  -  **Which is the most dangerous maritime area since 1980?** -
-------------------------------------------------------------------------------------------
- ****First question: Which is most dangeruos maritime area? 
- ****Second question: Which are ethe countries with more attacks in each maritime area?
- ****Third question: What is the most likely timeframe where the attacks can occur? Is the same in the two most dangerous areas?

To take into account: the year 1980 is chosen randomly to have a wide range of years. In this way, it is also guaranteed in a certain way that more records were made in the 80s than before and we avoid to much dispersion in the results.

## 2. Metholody

To perform the investigation, we proceed as follows:

- 0 Read the file 'attacks.csv.'
- 1. Explore the dataframe it self, verifying:
       - Dimension of the df ***(df.shape)**
       - Head of the df **(df.head)**
       - Data types **(df.types)***
       - Verify if we have repeated columns or rows as "Case Number" "Unnamed 22 &23" and           "hred & href formula"
       - Nulls ***isnull(df).sum***

- 2. General Cleaning data -- YEARS COLUMN:
    - We perform a ***general dataframe cleaning***:
            - Removing rolls with all null values
            - Droping duplicate values 

- 3. Cleaning data -- YEARS COLUMN:
    - Drop all the rows that have NaN in years & date column
    - Create a new column "New_Year" duplying the years in "Date" in order to extract the year that appears in the column when Date when Year column is = 0 using regex code . We create a new column in order to don't modify the original columns. we move all the dtaa t new column "All_years".
    - we detect some values of Year as 500, 70,7 and 0 that could be correct. So we are going to verify the data with the column date.  ***df6***
    - We will apply the result of the extraction to Years column whenever is < 1542 ( as al the years below here we suspect are they are wrong)

- 4. Cleaning data -- COUNTRY COLUMN:
    - Try to find the null values in other columns as "Area or Location" **.loc**
    - Clean country values: moddify to upper case
    - Assign Countries to Oceans with for loop in a new empty column "Oceans"
    - For not assigned values, we try to extract whenever the string contains the word      "OCEAN", copy the string value to the column Ocean
    - Unify names and assign to column
    - Drop empty values with no ocean assigned (194 values)
    
- 5. Cleaning Data - Cleaning
    - Remove null values 
    - Assign hour to a time zone with for loop (Sunrise, Morning, Afternoon and Night) with regex method ((r'^\d{2}$') and add the result to a new column "Cleaned time"

## CONCLUSIONS

- The most dangerous ocean is the North Atlantic, followed by South Atlantic and Indian Sea
- From the North Atlatinc the countries with more attacks are: USA and Bahamas, and from the South Pacific: Australia and New Zealand
- The time frame with more attacks is the afternoon


## Libraries used
- import pandas as pd
- import numpy as np
- import seaborn as sns
- import matplotlib.pyplot as plt
- import os


## Link & Resources
- https://www.kaggle.com/teajay/global-shark-attacks
- https://numpy.org/doc/1.18/
- https://pandas.pydata.org/
- https://docs.python.org/3/library/functions.html
- https://plotly.com/python/
- https://matplotlib.org/
- https://seaborn.pydata.org/
- https://pandas.pydata.org/docs/
