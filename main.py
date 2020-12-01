from numpy import sort
from Process import *
from classification import *
from visulization import *
import pandas as pd
from data_Cube import *


df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
df = df[df['User_Count'].notna()]
df = df[df['Publisher'].notna()]
year = df['Year_of_Release']
na_sales = df['NA_Sales']
name = df['Name']
genre = df['Genre']
user_score = list(df['User_Score'])
publisher = df['Publisher']
sales = list(df['Global_Sales'])
platform = df['Platform']
user_count = list(df['User_Count'])
user_score_val = []
new_user_score = []
estimated_sales = [round(sales[i], -1) for i in range(len(sales))]

categories = ['Name','Platform', 'Year_of_Release','Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales',
              'Other_Sales', 'Global_Sales', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer',
              'Rating']
cond_options = ['=', '/=', '>', '>=', '<', '<=']


for i in range(len(user_score)):
    if user_score[i] == 'tbd':
        user_score_val.append(-1)
        new_user_score.append(-1)
    else:
        user_score_val.append((float(user_score[i]) * 10) // 10)
        new_user_score.append(float(user_score[i]))
df['User_Score'] = new_user_score

dim = Dimension(categories)
cube = DataCube(df, categories)
cube.get_games_on_option(dim)
dim_list = cube.used_values
values = cube.options

lst = [sort(unique(genre)), sort(unique(platform))]
user_vals = [10, 55, 100]
compare_vals = ['<10', '10<=55', '55<=100', '>=100']

for i in range(len(values)):
    d = dim.get_option('Enter the value that you would like to see the pie chart based off of. ' +
                       values[i] + ' is being compared aggaint the whole dataset.')
    data = df.loc[df[dim_list[i]] == values[i]]
    pie(df, d, 'Percent of games of each ' + d + ' in the whole dataset')
    pie(data, d, 'Percent of games of each ' + d + ' made for the ' + values[i])


options1 = ['Electronic Arts', 'Activision', 'Ubisoft', 'THQ', 'Sony Computer Entertainment',
            'Take-Two Interactive', 'Sega', 'Nintendo']
options = list(genre)
df = df[df['Genre'].isin(options)]
publisher = df['Genre']

#display(genre, user_count, user_vals, lst[0], compare_vals)
#display(platform, user_count, user_vals, lst[1], compare_vals)
#display(publisher, user_count, user_vals, sort(unique(publisher)), compare_vals)

