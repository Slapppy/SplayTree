from _csv import writer
from random import randint
import pandas as pd
import matplotlib.pyplot as plt
from SplayTreeIm.benchmark.Benchmark import test_insert, test_search, test_delete


# create dataset
def case_test_search_lineal():
    n = 100
    for i in range(1, 100):
        dataset = [i for i in range(n)]
        test_insert(dataset)
        with open('dataset_for_visual/search_lineal.csv', 'a') as case:
            write_line = writer(case)
            write_line.writerow(['search'] + [len(dataset)] + [test_search(dataset)])
        n += 100


def case_test_search():
    n = 100
    for i in range(1, 100):
        dataset = [randint(1, 10000) for i in range(n)]
        test_insert(dataset)
        dataset.sort()
        with open('dataset_for_visual/search.csv', 'a') as case:
            write_line = writer(case)
            write_line.writerow(['search'] + [len(dataset)] + [test_search(dataset)])
        n += 100


def case_test_delete_lineal():
    n = 100
    for i in range(1, 100):
        dataset = [i for i in range(n)]
        test_insert(dataset)
        with open('dataset_for_visual/delete_lineal.csv', 'a') as case:
            write_line = writer(case)
            write_line.writerow(['delete'] + [len(dataset)] + [test_delete(dataset)])
        n += 100


def case_test_delete():
    n = 100
    for i in range(1, 100):
        dataset = [randint(1, 10000) for i in range(n)]
        test_insert(dataset)
        new_x = list(set(dataset))
        with open('dataset_for_visual/delete.csv', 'a') as case:
            write_line = writer(case)
            write_line.writerow(['delete'] + [len(dataset)] + [test_delete(new_x[:-50])])
        n += 100


# case_test_search()
# case_test_delete()
# case_test_delete_lineal()
# case_test_search_lineal()

# make visualization
df = pd.read_csv('dataset_for_visual/search_lineal.csv')
df.columns = ['method', 'elem', 'time']

plt.title('Search elements lineal', fontsize=20)
plt.plot(df['elem'], df['time'])
plt.show()
