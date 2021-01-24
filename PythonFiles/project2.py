import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(sum(df[df['sex']=='Male']['age'])/len(df[df['sex']=='Male']['age']),2)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors'])/len(df['education'])*100,2)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round(len(df[df['education-num']>=13]),2)
    lower_education = round(len(df[df['education-num']<13]),2)

    # percentage with salary >50K
    higher_education_rich = round(len(df[(df['education-num']>=13)&(df['salary']=='>50K')])/higher_education*100,2)
    lower_education_rich = round(len(df[(df['education-num']<13)&(df['salary']=='>50K')])/lower_education*100,2)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week']==1])

    rich_percentage = round(len(df[(df['hours-per-week']==1) & (df['salary']=='>50K')])/num_min_workers*100,2)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country1 = df['native-country'].value_counts()
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts()/highest_earning_country1).idxmax()
    highest_earning_country_percentage = round((df[df['salary'] == '>50K']['native-country'].value_counts()/highest_earning_country1*100).max(),2)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (df[(df['salary']=='>50K')&(df['native-country']=='India')]['occupation'].value_counts()).idxmax()
