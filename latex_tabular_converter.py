'''
Title: LaTeX tabular converter

Author: Alan Carrasco

Desc: This program converts a csv file into
a tabular format for LaTeX so you don't have
to.

Note: DO NOT include the headers of the csv file
'''

import csv

with open('practica4_TEM_resultados.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print('&'.join(row)+'//')
        print('\hline')
