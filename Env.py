import copy

import PySimpleGUI as ms
import mysql.connector
from datetime import *
import os
import io
from PIL import Image
import base64
from win32api import GetSystemMetrics
import os
import calendar
import openpyxl

mydb = mysql.connector.connect( host='localhost', user="root", passwd="MSeGa@1109",)
mycursor = mydb.cursor()
mycursor.execute('Use Twink_06ma')
mydb.commit

mycursor.execute("select value from nrdb order by description")
nrdb_data=list(sum(mycursor.fetchall(),()))
print(nrdb_data)
shi=GetSystemMetrics(1)-100
swi=GetSystemMetrics(0)

fstyle=(nrdb_data[0],int(nrdb_data[1]))
fstylehd=(nrdb_data[0],int(nrdb_data[1])+2)
file_types = [("JPEG (*.jpg)", "*.jpg"),("All files (*.*)", "*.*")]
os.chdir('C:\ERP\Icons')
with open("choose.png", "rb") as image_file:
 chse = base64.b64encode(image_file.read())
with open("browse.png", "rb") as image_file:
 browse = base64.b64encode(image_file.read())
with open("load.png", "rb") as image_file:
 load = base64.b64encode(image_file.read())

todate=datetime.today()
todatestr=todate.strftime("%Y-%m-%d")
todatenf=todate.strftime("%d-%m-%Y")
todatemy=todate.strftime("%m-%Y")
file_types = [("JPEG (*.jpg)", "*.jpg"),("All files (*.*)", "*.*")]
def border(element, color=None, width=3):
    if color is None:
        color = ms.theme_background_color()
    element.Widget.configure(highlightcolor=color, highlightbackground=color,
        highlightthickness=width)

def CCWFetch():
    mycursor.execute("select * from cleaning_crew")
    return ([list(x) for x in mycursor.fetchall()])

def EmpdataFetch(type):
    if type=="PF":
        mycursor.execute("select Emp_code, employee_name,f_sp_name,Gender,Phone_no,base_salary "
                         "from register where active_status = 'Y' and ET ='PF' ")
        return ([list(x) for x in mycursor.fetchall()])
    if type=="Non PF":
        mycursor.execute("select Emp_code, employee_name,f_sp_name,Gender,Phone_no,base_salary "
                         "from register where active_status = 'Y' and ET ='Non PF' ")
        return ([list(x) for x in mycursor.fetchall()])

def DB_Creation(inp):
    date_split=list(inp.split("-"))
    mycursor.execute('CREATE TABLE IF NOT EXISTS %s_%s (empcode varchar(50), primary key (empcode))'%(date_split[1],date_split[2]))
    mydb.commit()
    try:
        for i in range (1,calendar.monthrange(int(date_split[2]),int(date_split[1]))[1]+1):
            sql="alter table %s_%s add column (`%s` varchar(10))"%(date_split[1],date_split[2],str(i).zfill((2)))
            mycursor.execute(sql)
    except:
        pass
    mycursor.execute("select emp_code from register where active_status = 'Y'" )
    db_data=list(sum(mycursor.fetchall(),()))

    for i in db_data:
        try:
            mycursor.execute("insert into %s_%s (empcode) values ('%s')"%(date_split[1],date_split[2],str(i)))
            mydb.commit()
        except:
            pass
    try:
        mycursor.execute("insert into %s_%s (empcode) values ('counter')" % (date_split[1], date_split[2]))
        mydb.commit()
    except:
        pass

def datasplit(data,filter):

    if filter == 'Attendance':
        for part in data:
            for i in range(3,len(part)):
                if part[i]!=None:
                    temp=list(part[i].split(","))
                    part[i]=temp[0]
                else:
                    pass
    elif filter == 'OT':
        for part in data:
            for i in range(3,len(part)):
                if part[i]!=None:
                    temp=list(part[i].split(","))
                    part[i]=temp[1]
                else:
                    pass
    elif filter == 'Expenses':
        for part in data:
            for i in range(3,len(part)):
                if part[i]!=None:
                    temp=list(part[i].split(","))
                    part[i]=temp[2]
                else:
                    pass
    elif filter =='Atn+ot':
        for part in data:
            for i in range(3,len(part)):
                if part[i]!=None:
                    temp=list(part[i].split(","))
                    part[i]=str(temp[0])+";",str(temp[1])
                else:
                    pass
    return data

def attendance_fetch(inp):
    form = list(inp.split("-"))
    mycursor.execute("select register.employee_name,register.f_sp_name, %s_%s.* "
                     "from register inner join %s_%s on register.emp_code = %s_%s.empcode" % (
                     form[0], form[1], form[0], form[1], form[0], form[1]))
    db_data = [list(x) for x in mycursor.fetchall()]
    #print(db_data)
    for i in range(len(db_data)):
        # print(db_data[i])
        db_data[i].insert(0, db_data[i][2])
        del db_data[i][3]
    return db_data

def wage_fetch():
    mycursor.execute("Select emp_code,base_salary from register where shift_work='No' ")
    db_data=[list(x) for x in mycursor.fetchall()]
    #print(db_data)
    dict_data={x[0]:float(x[1]) for x in db_data}
    #print(dict_data)
    mycursor.execute("Select emp_code,shift_1_salary,shift_2_salary,shift_3_salary from register where shift_work='Yes'")
    db_data=[list(x) for x in mycursor.fetchall()]
    output=[]
    for step in db_data:
        temp=[]
        temp.append(step[0])
        temp1=[]
        for i in range (1,4):
            temp1.append(float(step[i]))
        temp.append(temp1)
        output.append(temp)
    dict_data_SY= {x[0]:x[1] for x in output}

    dict_data.update(dict_data_SY)
    print(dict_data)
    return dict_data

wage_fetch()

