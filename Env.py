import PySimpleGUI as ms
import mysql.connector
import datetime
from win32api import GetSystemMetrics

mydb = mysql.connector.connect( host='localhost', user="root", passwd="MSeGa@1109",)
mycursor = mydb.cursor()
mycursor.execute('Use Twink_06ma')
mydb.commit

shi=GetSystemMetrics(1)-70
swi=GetSystemMetrics(0)

fstyle=('Courier New',12)
fstylehd=('Courier New',14)
file_types = [("JPEG (*.jpg)", "*.jpg"),("All files (*.*)", "*.*")]

def EmpdataFetch():
    mycursor.execute("select Emp_code, employee_name,f_sp_name,Gender,Phone_no,base_salary "
                     "from register where active_status = 'Y' ")
    return ([list(x) for x in mycursor.fetchall()])