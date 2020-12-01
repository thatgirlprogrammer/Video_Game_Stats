import matplotlib.pyplot as plt
import pandas as pd


def get_groups(lst, partition, values):
    groups = [{}, {}, {}, {}]
    for i in range(len(lst)):
        if partition[i] < values[0]:
            if lst[i] not in groups[0]:
                groups[0].update({lst[i]: 1})
            else:
                groups[0][lst[i]] += 1
        elif values[0] <= partition[i] < values[1]:
            if lst[i] not in groups[1]:
                groups[1].update({lst[i]: 1})
            else:
                groups[1][lst[i]] += 1
        elif values[1] <= partition[i] < values[2]:
            if lst[i] not in groups[2]:
                groups[2].update({lst[i]: 1})
            else:
                groups[2][lst[i]] += 1
        else:
            if lst[i] not in groups[3]:
                groups[3].update({lst[i]: 1})
            else:
                groups[3][lst[i]] += 1
    return groups


def group_values(lst, partition, values, cat):
    groups = {}
    for i in range(len(lst)):
        if lst[i] == cat:
            if partition[i] < values[0]:
                if '<' + str(values[0]) not in groups:
                    groups.update({'<' + str(values[0]): 1})
                else:
                    groups['<' + str(values[0])] += 1
            elif values[0] <= partition[i] < values[1]:
                if str(values[0]) + '<=' + str(values[1]) not in groups:
                    groups.update({str(values[0]) + '<=' + str(values[1]): 1})
                else:
                    groups[str(values[0]) + '<=' + str(values[1])] += 1
            elif values[1] <= partition[i] < values[2]:
                if str(values[1]) + '<=' + str(values[2]) not in groups:
                    groups.update({str(values[1]) + '<=' + str(values[2]): 1})
                else:
                    groups[str(values[1]) + '<=' + str(values[2])] += 1
            else:
                if '>=' + str(values[2]) not in groups:
                    groups.update({'>=' + str(values[2]): 1})
                else:
                    groups['>=' + str(values[2])] += 1
    return groups


def display(category, count, numbers, names, vals):
    display_values = []
    data = [[] for i in range(len(numbers) + 1)]
    dct = {}
    print(category)
    print(count)
    print(numbers)

    for i in range(len(vals)):
        dct.update({vals[i]: 0})
    for i in range(len(names)):
        display_values.append(group_values(list(category), list(count), numbers, names[i]))
    dct = get_dict(data, display_values, vals)
    # print_data(display_values, names)
    show_plot(dct, names, vals)


def get_dict(data, display_values, vals):
    dct = {}
    for j in range(len(vals)):
        for i in range(len(display_values)):
            try:
                data[j].append(display_values[i][vals[j]])
            except KeyError:
                data[j].append(0)
        dct[vals[j]] = data[j]
    return dct


def print_data(display_values, names):
    print('Number of users per group per cateogory')
    for i in range(len(display_values)):
        print(names[i])
        print(display_values[i])


def show_plot(dct, names, vals):
    # Data
    df = pd.DataFrame(dct)
    # From raw value to percentage
    totals = [i + j + k + h for i, j, k, h in zip(df[vals[0]], df[vals[1]], df[vals[2]], df[vals[3]])]
    greenBars = [i / j * 100 for i, j in zip(df[vals[0]], totals)]
    orangeBars = [i / j * 100 for i, j in zip(df[vals[1]], totals)]
    blueBars = [i / j * 100 for i, j in zip(df[vals[2]], totals)]
    yellowBars = [i / j * 100 for i, j in zip(df[vals[3]], totals)]
    create_plot(blueBars, greenBars, names, orangeBars, vals, yellowBars)


def create_plot(blueBars, greenBars, names, orangeBars, vals, yellowBars):
    # plot
    barWidth = 0.85
    r = [i for i in range(len(names))]
    names = tuple(names)
    # Create green Bars
    plt.bar(r, greenBars, color='#b5ffb9', edgecolor='white', width=barWidth, label=vals[0])
    # Create orange Bars
    plt.bar(r, orangeBars, bottom=greenBars, color='#f9bc86', edgecolor='white', width=barWidth, label=vals[1])
    # Create blue Bars
    plt.bar(r, blueBars, bottom=[i + j for i, j in zip(greenBars, orangeBars)], color='#a3acff', edgecolor='white',
            width=barWidth, label=vals[2])
    # Create yellow Bars
    plt.bar(r, yellowBars, bottom=[i + j + k for i, j, k in zip(greenBars, orangeBars, blueBars)], color='yellow',
            edgecolor='white', width=barWidth, label=vals[3])
    # Custom x axis
    plt.xticks(r, names)
    plt.xlabel("group")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)
    plt.show()


def line(t1, y_val1, y_val2):
    plt.figure()
    ax = plt.subplot(211)
    ax.set_xlim(2000, 2020)
    plt.plot(t1, y_val1, 'bo')

    plt.subplot(212)
    plt.plot(t1, y_val2, 'r--')
    plt.show()


def pie(df, label, title, number = 20):
    vals = df.groupby(by=label).agg('count')['Name']
    values = pd.DataFrame({label:vals.index, 'Count':vals.values})
    values = values.sort_values('Count')

    num = len(values) if len(values) <= number else number
    arr = values[ len(values) - num : len(values)]
    plt.pie(arr['Count'], labels=arr[label], autopct='%1.0f%%', pctdistance=0.9, labeldistance=1.22)
    plt.title(title)
    plt.show()


