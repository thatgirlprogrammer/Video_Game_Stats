import math
from numpy.ma import log2


class Classifier:
    def __init__(self, categories, user_count, select_values, cond):
        self.categories = categories
        self.user_count = user_count
        self.select_values = select_values
        self.condition = cond
        for i in range(len(categories)):
            categories[i] = list(categories[i])

    def find_above_dict(self, category, condition_val):
        values = {}
        for i in range(len(category)):
            if condition_val[i] > self.condition and not math.isnan(condition_val[i]):
                if category[i] not in values:
                    val = category[i]
                    values.update({val: 1})
                else:
                    values[category[i]] += 1
        return values

    def find_below_dict(self, category, condition_val):
        values = {}
        for j in range(len(category)):
            if condition_val[j] <= self.condition and not math.isnan(condition_val[j]):
                if category[j] not in values:
                    val = category[j]
                    values.update({val: 1})
                else:
                    values[category[j]] += 1
        return values

    def get_dict(self, partition_value, check_value):
        return self.find_above_dict(partition_value, list(check_value))

    def get_less_than_dict(self, partition_value, check_value):
        return self.find_below_dict(partition_value, list(check_value))

    def find_probabilities(self, probability_func, index):
        probability_list = []
        for j in range(len(self.categories)):
            values = probability_func(self.categories[j], self.user_count)
            probability_list.append(values[self.select_values[j]] /
                                    self.get_counts(self.user_count)[index])
        return probability_list

    def get_counts(self, partition_list):
        above = 0
        below = 0
        for j in range(len(partition_list)):
            if partition_list[j] > self.condition:
                above += 1
            else:
                below += 1
        return [above, below]

    def get_condition_probability(self):
        count = 0
        total = 0
        for j in range(len(self.user_count)):
            if self.user_count[j] > self.condition:
                count += 1
            total += 1
        return count / total

    def determine_label(self):
        prob = self.get_condition_probability()
        more_prob = self.find_probabilities(self.get_dict, 0)
        less_prob = self.find_probabilities(self.get_less_than_dict, 1)
        print(prob)
        print(more_prob)
        print(less_prob)

        more_prob_val = prob
        less_prob_val = 1 - prob
        for i in range(len(more_prob)):
            more_prob_val *= more_prob[i]
            less_prob_val *= less_prob[i]

        print('more prob: ', more_prob_val)
        print('less prob: ', less_prob_val)
        return 'count above 10' if more_prob_val > less_prob_val else 'count below 10'


def get_info(self, values):
    result = []
    for j in range(len(values)):
        for k in range(len(values[j])):
            result.append(-1 * values[k] * log2(values[k]))
    return result

def gain(self, infos, probabilities):
    result = 0
    for j in range(infos):
        result += infos[j]*probabilities[j]
    return result