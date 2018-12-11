# encoding: UTF-8

import csv

# 讀取 CSV 檔案內容
path = 'C:\\Users\\Bette\Anaconda2\\Lib\\site-packages\\vnpy-1.9.0-py2.7.egg\\examples\\CtaBacktesting'

csvfile = '\TXF_Tick.csv'

with open(path + csvfile, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)