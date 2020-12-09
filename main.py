import os
import xlrd
import sys
import xdrlib
import time
import datetime
import sys
import re
# -*- coding: UTF-8 -*-
# sys.path.append('../')
import B
import AA


def openexcel(path):
    try:
        data = xlrd.open_workbook(path)
        return data
    except:
        print('wrong')


def dealwithexcel(path, classnum):
    data = openexcel(path)
    sheet = data.sheet_by_index(0)
    nrows = sheet.nrows
    totlist = []
    for i in range(2, nrows):
        r = sheet.row_values(i, start_colx=0, end_colx=None)
        banji = str(r[2])
        if(',' in banji):
            b = banji.split(',')
            for d in b:
                if(d == classnum):
                    print(r)
                    totlist.append(r)
                    break
        else:
            banji = banji[0:7]
            if(banji == str(classnum)):
                print(r)
                totlist.append(r)
    B.standardlized(classnum, totlist)
    AA.standardlized(classnum, totlist)


if __name__ == "__main__":
    filename = r'F:\Python\excel\arrange.xls'
    classnum = input("班级号：")
    dealwithexcel(filename, classnum)
