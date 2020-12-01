import pandas as pd
from numpy import sort

from Process import get_number


class DataCube:
    def __init__(self, df, categories):
        self.df = df
        self.categories = categories
        self.options = []
        self.used_values = []

    def get_val_based_on_condition(self, dataset, option, value):
        cond = input('Enter one of these options =, /=, >, >=, <, <=')
        if cond == '=':
            return dataset.loc[self.df[option] == value]
        elif cond == '/=':
            return dataset.loc[self.df[option] != value]
        elif cond == '>':
            return dataset.loc[self.df[option] > value]
        elif cond == '>=':
            return dataset.loc[self.df[option] >= value]
        elif cond == '<':
            return dataset.loc[self.df[option] < value]
        elif cond == '<=':
            return dataset.loc[self.df[option] <= value]
        else:
            return self.get_val_based_on_condition(dataset, option, value)

    def get_games_on_option(self, dimension):
        num = input('Enter the number of values you want to use in your query. You may select multiple values of the '
                    'same option.')

        for i in range(get_number(num, int)):
            option = dimension.get_option()
            self.used_values.append(option)

        sort(self.used_values)
        count_vals = {}
        for i in self.used_values:
            if i not in count_vals:
                count_vals.update({i: 1})
            else:
                count_vals[i] += 1

        data = self.df[self.categories]
        for option in count_vals:
            datasets = []
            for i in range(count_vals[option]):
                op = Options(option, self.df)
                option_value = op.get_values_for_data()
                self.options.append(option_value)
                val = self.get_val_based_on_condition(data, option, option_value)
                datasets.append(val)
            data = pd.concat(datasets)

        dimensions = dimension.get_dimensions()
        print(data[dimensions].to_string(index=False))


class Options:
    def __init__(self, option, df):
        self.option = option
        self.df = df

    def get_values_for_data(self):
        option_value = input('Enter the value for ' + self.option + ' You would like to view.')
        if self.option in ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Score',
                           'Critic_Count', 'User_Score', 'User_Count', 'Year_of_Release']:
            option_value = get_number(option_value)

        if type(option_value) != float:
            while option_value not in list(self.df[self.option]):
                option_value = input('Not a valid option, try again.')
        return option_value


class Dimension:
    def __init__(self, categories):
        self.categories = categories

    def get_dimensions(self):
        num = input('How many variables from the dataset would you like to use?')
        dimensions = []
        for i in range(get_number(num, int)):
            dimension = self.get_option('What dimension would you like to view')
            if dimension not in dimensions:
                dimensions.append(dimension)
            else:
                print('dimension', dimension, 'already in the list.')
                i -= 1
        return dimensions

    def get_option(self, value='What option of games would you like to get your data based on?'):
        option = input(value)
        while option not in self.categories:
            option = input('Not a valid option, try again.')
        return option
