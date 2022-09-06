from Env import *

#---Initiation
from Env import *
import Attendance_Push
import Attendance_View
import Register
import Wage_Calc
import Master_User
import Cleaning_Crew
import CC_Attendence_View
#---Custom DB Declaration
mycursor.execute('Use Twink_06ma')
mydb.commit()

#--- Base Menu Declaration
MenuDef = [
           ['Navigate',   ['Home','Register','Master User']],
           ['Attendance', ['Create','View','CC_Attendence','CC_View','Advance']],
           ['Reports',    ['Wages']],
]
#--- Base Layout Declaration
BaseLayout=[[ms.Sizer(swi/2-200,0),ms.Image(source=logo)],
            [ms.Sizer(swi/2-200,0) ,ms.Text("SUNIL INDUSTRIES LIMITED",font=("Courier New",18),justification='center')],
            [ms.Sizer(0,150)],
            [ms.Sizer(600,500),ms.Frame(layout=[
                [ms.Text('Date',font=fstyle,size=(20,1)),ms.Text(todatenf,font=fstyle,size=(10,1))],
                [ms.Text('No. of Employees',font=fstyle,size=(20,1)),ms.Text(empcount,font=fstyle,size=(10,1))],
                [ms.Text('Attendance Status',font=fstyle,size=(20,1)),ms.Text(atstat,font=fstyle,size=(15,1))],
                [ms.Sizer(150,0),ms.Button("Mail",disabled= False if atstat == "created" else True,font=fstyle,key='mailreport')]
            ],size=(400,140),font=fstyle,title="Infographics")]
            ]

layout=[[ms.Menu    (MenuDef, key='MENU',font=fstyle)],
        [
        ms.Column  (BaseLayout,key="base",visible=True,size=(swi,shi),element_justification='center'),
        ms.Column  (Register.RegsiterLay(),key='register',visible=False,size=(swi,shi),element_justification='center'),
        ms.Column  (Master_User.Master_User_GUI(),key='mumneu',visible=False,size=(swi,shi),element_justification='center'),
        ms.Column  (Attendance_Push.AttendancePushLay(),key='atnpush',visible=False,size=(swi,shi),element_justification='center'),
        ms.Column  (Attendance_View.AttendanceViewLay(),key='atnview',visible=False,size=(swi,shi),element_justification='center'),
        ms.Column  (Wage_Calc.WageCalcLay(),key='wagecalc',visible=False,size=(swi,shi),element_justification='center'),
        ms.Column  (Cleaning_Crew.crew_att_gui(),key='cc_att',visible=False,size=(swi,shi),element_justification='center'),
        ms.Column  (CC_Attendence_View.CC_View_GUI(),key='c_view',visible=False,size=(swi,shi)),
        ms.Column  (Wage_Calc.WageCalcLay(),key='wagecalc',visible=False,size=(swi,shi),element_justification='center'),
        ms.Column  (Attendance_View.AdvanceoptLay(), key='advopt', visible=False, size=(swi, shi),element_justification='center')

        ]]

MenuList=["base","register",'atnpush','atnview','wagecalc','mumneu','c_view','cc_att','advopt']

Menu = ms.Window("Twink_Attendance",layout,location=(0,0),size=(swi,shi),element_justification='center',return_keyboard_events=True)

while True:

    #try:
        event, values = Menu.read()
        print(event)
        if event == ms.WIN_CLOSED:
            Menu.close()
            break

        if event == "Home" or  event[:6] == 'Escape':
            mycursor.execute(
                "select `%s` from %s_%s where empcode = 'counter'" % (tempdate[0], tempdate[1], tempdate[2]))
            atstat = "created" if mycursor.fetchall()[0][0] == "v" else "To be Created"
            for i in MenuList:
                Menu[i].update(visible=False)
            Menu['base'].update(visible=True)

        if event == 'Register' or  event[:2] == 'F1' :
            for i in MenuList:
                Menu[i].update(visible=False)
            Menu['register'].update(visible=True)

        if event == 'Create' or event[:2] == 'F2':
            for i in MenuList:
                Menu[i].update(visible=False)
            Menu['atnpush'].update(visible=True)

        if event == 'View' or event[:2] == 'F3':
            for i in MenuList:
                Menu[i].update(visible=False)
            Menu['atnview'].update(visible=True)

        if event == 'Master User' or event[:2] == 'F9' :
            chk = ms.popup_get_text("Enter password to enter Master User ", password_char='*', size=(20, 1), font=fstyle,
                                     keep_on_top=True)
            if chk == "AstA_SIL":
                for i in MenuList:
                    Menu[i].update(visible=False)
                Menu['mumneu'].update(visible=True)
            else:
                ms.popup_auto_close("Please try again",font=fstyle, no_titlebar=True, auto_close_duration=2)


        if event == 'CC_Attendence':
            for i in MenuList:
                Menu[i].update(visible=False)
            Menu['cc_att'].update(visible=True)

        if event == 'CC_View':
            for i in MenuList:
                Menu[i].update(visible=False)
            Menu['c_view'].update(visible=True)


        if event == 'Wages' or event[:2] == 'F4':
            for i in MenuList:
                Menu[i].update(visible=False)
            Menu['wagecalc'].update(visible=True)

        if event == 'Advance':
            for i in MenuList:
                Menu[i].update(visible=False)
            Menu['advopt'].update(visible=True)


        Register.RegisterFn(Menu,event,values)
        Attendance_Push.AttendancePushFn(Menu,event,values)
        Attendance_View.AttendaceViewFn(Menu,event,values)
        Wage_Calc.WageCalcFn(Menu,event,values)
        Master_User.Master_User(Menu,event,values)
        Cleaning_Crew.cc_att_(event, values, Menu)
        CC_Attendence_View.c_view_db(event, values, Menu)

        if event == 'mailreport':
            chk=ms.popup_ok("Please confrim to send mail",font=fstyle,no_titlebar=True)
            if chk == "OK":
                mailreport(todatenf)
    #except Exception as e:
       # ms.popup_ok(e,font=fstyle,title="Error, Please try again")




