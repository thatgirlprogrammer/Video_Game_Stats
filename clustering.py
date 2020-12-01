import matplotlib.pyplot as plt
import pandas
from sklearn.cluster import KMeans
import seaborn as sns; sns.set()  # for plot styling
import numpy as np


def counts_val(lst):
    count = {}
    for i in range(len(lst)):
        if lst[i] not in count:
            count.update({lst[i]: 1})
        else:
            count[lst[i]] += 1
    print(count)
    arr = [[], []]
    for c in count:
        for j in range(count[c]):
            arr[0].append(c)
            arr[1].append(j)
    return arr


def cluster(df):
    dataset = list()
    sales = list(df['Global_Sales'])
    users = list(df['User_Count'])
    for i in range(len(sales)):
        dataset.append([])
        dataset[i].append(sales[i])
        dataset[i].append(users[i])
    plt.scatter(df['Global_Sales'], df['User_Count'])
    plt.show()
    dataset = np.array(dataset)

    # Using sklearn
    km = KMeans(n_clusters=6)
    km.fit(dataset)
    # Get cluster assignment labels
    labels = km.labels_
    # Format results as a DataFrame
    dataset = list(dataset)
    results = pandas.DataFrame([dataset.index, labels]).to_dict()
    print(results)
    count = counts_val(labels)
    plt.scatter(x=count[0], y=count[1])
    plt.show()


    """
    plt.scatter(X[:, 0], X[:, 1], s=50);
    plt.show()

    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)

    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
    plt.show()
"""
