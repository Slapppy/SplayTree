import time
from csv import writer
import pandas as pd
from random import randint
from SplayTreeIm.SplayTree import SplayTree, Node

spltree = SplayTree()
n = 10000
dataset = []
dataset1 = [i for i in range(0, n)]


def test_insert(dataset, tree=spltree):
    t1 = time.time()
    for i in dataset:
        tree.insert(Node(i))
    t2 = time.time()
    return f"%.8f" % (t2 - t1)


def test_search(dataset, tree=spltree):
    t1 = time.time()
    for i in dataset:
        tree.search_tree(Node(i))
    t2 = time.time()
    return f"%.8f" % (t2 - t1)


def test_delete(dataset, tree=spltree):
    t1 = time.time()
    for i in dataset:
        tree.delete(Node(i))
    t2 = time.time()
    return f"%.8f" % (t2 - t1)


def worst_case_insert():
    for i in range(1, 5 + 1):
        with open(f'data_worst{i}.txt', 'r') as file:
            _list = []
            for line in file:
                _list.append(line)
            with open(r'C:\Users\Slappy\PycharmProjects\SplayTree\SplayTreeIm\benchmark\Results\insert_worst.csv' , 'a') as case:
                write_line = writer(case)
                write_line.writerow(['insert']+[len(_list)] + [test_insert(_list)])

def worst_case_search():
    for i in range(1, 5 + 1):
        with open(f'data_worst{i}.txt', 'r') as file:
            _list = []
            for line in file:
                _list.append(line)
            with open(r'C:\Users\Slappy\PycharmProjects\SplayTree\SplayTreeIm\benchmark\Results\search_worst.csv' , 'a') as case:
                write_line = writer(case)
                write_line.writerow(['search']+[[len(_list)]] + [test_search(_list)])

def worst_case_delete():
    for i in range(1, 5 + 1):
        with open(f'data_worst{i}.txt', 'r') as file:
            _list = []
            for line in file:
                _list.append(line)
            with open(r'C:\Users\Slappy\PycharmProjects\SplayTree\SplayTreeIm\benchmark\Results\delete_worst.csv' , 'a') as case:
                write_line = writer(case)
                write_line.writerow(['delete']+[len(_list)] + [test_delete(_list)])

def case_insert():
    for i in range(1, 5 + 1):
        with open(f'dataset{i}.txt', 'r') as file:
            _list = []
            for line in file:
                _list.append(line)
            with open(r'C:\Users\Slappy\PycharmProjects\SplayTree\SplayTreeIm\benchmark\Results\insert.csv' , 'a') as case:
                write_line = writer(case)
                write_line.writerow(['insert']+[len(_list)] + [test_insert(_list)])

def case_search():
    for i in range(1, 5 + 1):
        with open(f'dataset{i}.txt', 'r') as file:
            _list = []
            for line in file:
                _list.append(line)
            with open(r'C:\Users\Slappy\PycharmProjects\SplayTree\SplayTreeIm\benchmark\Results\search.csv' , 'a') as case:
                write_line = writer(case)
                write_line.writerow(['search']+[len(_list)] + [test_search(_list)])

def case_delete():
    for i in range(1, 5 + 1):
        with open(f'dataset{i}.txt', 'r') as file:
            _list = []
            for line in file:
                _list.append(line)
            with open(r'C:\Users\Slappy\PycharmProjects\SplayTree\SplayTreeIm\benchmark\Results\delete.csv' , 'a') as case:
                write_line = writer(case)
                write_line.writerow(['delete']+[len(_list)] + [test_delete(_list)])

worst_case_insert()
worst_case_search()
worst_case_delete()
case_insert()
case_search()
case_delete()