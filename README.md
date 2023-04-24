# Project-I-Sharks

## 0. Introduction

On this project, the main goal is to clean the data of the provided attacks.csv* file using pandas. Additionaly, we will define some functions to run the code and we will execute some visualizations to present the findings.
*The data is extracted from www.kaggle.com.



## 1. Project description

Firstly we re going to provide a brief overview of the all he aspects involved in the project and what we want to achive with our analysys.
In order to clean acuratey our data based, we set the researh main question to focus the cleaning.

---------------------------------------**VALIDATION**--------------------------------------
  -  **The particularities of each maritime area (temperature, climatology, etc) does affects to the attacks?** -
-------------------------------------------------------------------------------------------
- Which is most dangeruos maritime area? 
- Which are ethe countries with more attacks in each maritime area?
- The own particularities of each maritime area (temperature, climatology, etc) affects to the attacks?
- What is the most likely timeframe where the attacks can occur? Is the same in the two most dangerous areas?


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

- we open we start cleaning general data:
    - 

- `pandas_1.ipynb` with your responses to each of the exercises.

## Libraries used


## Submission

Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.

## Link & Resources
Links & Resources
https://www.kaggle.com/teajay/global-shark-attacks
https://numpy.org/doc/1.18/
https://pandas.pydata.org/
https://docs.python.org/3/library/functions.html
https://plotly.com/python/
https://matplotlib.org/
https://seaborn.pydata.org/
https://pandas.pydata.org/docs/
