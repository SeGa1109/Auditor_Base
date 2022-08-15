import copy
import os

import openpyxl

from Env import *

def WageCalcLay():
    layout=[
        [ms.Input(todatemy,font=fstyle,size=(10,1),key='wcdateinp'),ms.CalendarButton(" ",target='wcdateinp',format="%m-%Y"),
         ms.Button("Export",key='wcxlexp',font=fstyle)]
    ]
    return layout

def WageCalcFn(Menu,event,values):

    if event=='wcxlexp':
        data=attendance_fetch(values['wcdateinp'])
        xl=openpyxl.load_workbook(filename=r'C:\Twink_06MA\Master_Files\Atn_Exp.xlsx')
        for step in ['Attendance','OT','Expenses']:
            xl.active=xl[step]
            xlc=xl.active
            atndata=datasplit(copy.deepcopy(data),step)
            crow=2
            ccol=1
            for part in atndata:
                for i in range(len(part)):
                    xlc.cell(row=crow,column=ccol).value=part[i]
                    ccol+=1
                crow+=1
                ccol = 1


        xl.save(filename=r'C:\Twink_06MA\Master_Files\Atn_ExpT1.xlsx')
        os.system(r'C:\Twink_06MA\Master_Files\Atn_ExpT1.xlsx')