from Env import *

#---Initiation
from Env import *
import Attendance_Push
import Attendance_View
import Register
import Wage_Calc
import Master_User
#---Custom DB Declaration
mycursor.execute('Use Twink_06ma')
mydb.commit()

#--- Base Menu Declaration
MenuDef = [
           ['Navigate',   ['Home','Register','Master User']],
           ['Attendance', ['Create','View']],
           ['Reports',    ['Wages']],
]
#--- Base Layout Declaration
BaseLayout=[[ms.Sizer(swi/2-170,0) ,ms.Text("SUNIL INDUSTRIES LIMITED",font=fstylehd,justification='center')]]

layout=[[ms.Menu    (MenuDef, key='MENU',font=fstyle)],
        [
        ms.Column  (BaseLayout,key="base",visible=False,size=(swi,shi),element_justification='center'),
        ms.Column  (Register.RegsiterLay(),key='register',visible=True,size=(swi,shi),element_justification='center'),
        ms.Column  (Master_User.Master_User_GUI(),key='mumneu',visible=False,size=(swi,shi),element_justification='center'),
        ms.Column  (Attendance_Push.AttendancePushLay(),key='atnpush',visible=False,size=(swi,shi),element_justification='center'),
        ms.Column  (Attendance_View.AttendanceViewLay(),key='atnview',visible=False,size=(swi,shi),element_justification='center'),
        ms.Column  (Wage_Calc.WageCalcLay(),key='wagecalc',visible=False,size=(swi,shi),element_justification='center')
        ]]

MenuList=["base","register",'atnpush','atnview','wagecalc','mumneu']

Menu = ms.Window("Twink_Attendance",layout,location=(0,0),size=(swi,shi),element_justification='center')

while True:
    event,values=Menu.read()
    print(event)
    if event == ms.WIN_CLOSED:
        Menu.close()
        break

    if event == "Home":
        for i in MenuList:
            Menu[i].update(visible=False)
        Menu['base'].update(visible=True)

    if event == 'Register':
        for i in MenuList:
            Menu[i].update(visible=False)
        Menu['register'].update(visible=True)

    if event == 'Create':
        for i in MenuList:
            Menu[i].update(visible=False)
        Menu['atnpush'].update(visible=True)

    if event == 'View':
        for i in MenuList:
            Menu[i].update(visible=False)
        Menu['atnview'].update(visible=True)

    if event == 'Master User':
        chk = ms.popup_get_text("Enter password to enter Master User ", password_char='*', size=(20, 1), font=fstyle,
                                no_titlebar=True, keep_on_top=True)
        if chk == "AstA_SIL":
            for i in MenuList:
                Menu[i].update(visible=False)
            Menu['mumneu'].update(visible=True)
        elif chk != "AstA_SIL":
            ms.popup_auto_close("Wrong Password", no_titlebar=True, auto_close_duration=2)
        elif chk == "Cancel":
            print(None)

    if event == 'Wages':
        for i in MenuList:
            Menu[i].update(visible=False)
        Menu['wagecalc'].update(visible=True)



    Register.RegisterFn(Menu,event,values)
    Attendance_Push.AttendancePushFn(Menu,event,values)
    Attendance_View.AttendaceViewFn(Menu,event,values)
    Wage_Calc.WageCalcFn(Menu,event,values)
    Master_User.Master_User(Menu,event,values)

