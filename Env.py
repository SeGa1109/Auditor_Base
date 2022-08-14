import PySimpleGUI as ms
import mysql.connector
import datetime
import os
import io
from PIL import Image
import base64
from win32api import GetSystemMetrics
import os
mydb = mysql.connector.connect( host='localhost', user="root", passwd="MSeGa@1109",)
mycursor = mydb.cursor()
mycursor.execute('Use Twink_06ma')
mydb.commit

shi=GetSystemMetrics(1)-70
swi=GetSystemMetrics(0)

fstyle=('Courier New',12)
fstylehd=('Courier New',14)
file_types = [("JPEG (*.jpg)", "*.jpg"),("All files (*.*)", "*.*")]
os.chdir('C:\ERP\Icons')
with open("choose.png", "rb") as image_file:
 chse = base64.b64encode(image_file.read())
with open("browse.png", "rb") as image_file:
 browse = base64.b64encode(image_file.read())
with open("load.png", "rb") as image_file:
 load = base64.b64encode(image_file.read())


file_types = [("JPEG (*.jpg)", "*.jpg"),("All files (*.*)", "*.*")]

def EmpdataFetch(type):
    if type=="PF":
        mycursor.execute("select Emp_code, employee_name,f_sp_name,Gender,Phone_no,base_salary "
                         "from register where active_status = 'Y' and ET ='PF' ")
        return ([list(x) for x in mycursor.fetchall()])
    if type=="Non PF":
        mycursor.execute("select Emp_code, employee_name,f_sp_name,Gender,Phone_no,base_salary "
                         "from register where active_status = 'Y' and ET ='Non PF' ")
        return ([list(x) for x in mycursor.fetchall()])