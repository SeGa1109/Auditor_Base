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