from Env import *

datalist=[[ms.Text("Emp. Code",justification= 'center',size=(15,1),relief= 'raised',font=fstylehd),
           ms.Text("Name",justification= 'center',relief= 'raised',size=(32,1),font=fstylehd),
           ms.Text("F/S Name",justification= 'center',relief= 'raised',size=(32,1),font=fstylehd),
           ms.Text("Shift_AT",justification= 'center',relief= 'raised',size=(20,1),font=fstylehd),
           ms.Text("OT Hours",justification= 'center',relief= 'raised',size=(10,1),font=fstylehd),
           ms.Text("Expense",justification= 'center',relief= 'raised', size=(15, 1), font=fstylehd),
          ]]

mycursor.execute('select UID,emp_code,employee_name,f_sp_name from register where active_status = "Y" ')
emplist=[list(x) for x in mycursor.fetchall()]
print(emplist)
#atpec= Attendance Push Employee Code
for i in range (len(emplist)):
    sub1=ms.Column([[ms.Input(emplist[i][1],font=fstyle,key='atpec'+str(i),size=(16,1),disabled=True,justification='center',
                   disabled_readonly_background_color=ms.theme_background_color(),border_width= 0),ms.Sizer(5,0),
          ms.Text(emplist[i][2],font=fstyle,size=(35,1),key='atpn'+str(i),justification='center'),ms.Sizer(2,0),
          ms.Text(emplist[i][3], font=fstyle, size=(35, 1) ,key='atpfs'+str(i),justification='center'),ms.Sizer(35,0),
          ms.Radio("I", font=fstyle, key='atp1s' + str(i), group_id='atpsd' + str(i)),
          ms.Radio("II",font=fstyle,key='atp2s'+str(i),group_id='atpsd'+str(i)),
          ms.Radio("III",font=fstyle,key='atp3s'+str(i),group_id='atpsd'+str(i)),ms.Sizer(25,0),
          ms.Spin(values=[0,1,2,3,4],initial_value=0,font=fstyle,size=(8,1),key='atpot'+str(i),),ms.Sizer(15,0),
          ms.Input("",font=fstyle,key='atpxp'+str(i),size=(15,1))
          ],[ms.HSeparator()] ],visible= True,key='atp'+str(i))
    datalist.append([sub1])

for i in range(len(emplist),len(emplist)+5):
    sub1=ms.Column([[ms.Input("",font=fstyle,key='atpec'+str(i),size=(16,1),disabled=True,justification='center',
                   disabled_readonly_background_color=ms.theme_background_color(),border_width= 0),ms.Sizer(5,0),
          ms.Text("",font=fstyle,size=(35,1),key='atpn'+str(i),justification='center'),ms.Sizer(2,0),
          ms.Text("", font=fstyle, size=(35, 1) ,key='atpfs'+str(i),justification='center'),ms.Sizer(35,0),
          ms.Radio("I", font=fstyle, key='atp1s' + str(i), group_id='atpsd' + str(i)),
          ms.Radio("II",font=fstyle,key='atp2s'+str(i),group_id='atpsd'+str(i)),
          ms.Radio("III",font=fstyle,key='atp3s'+str(i),group_id='atpsd'+str(i)),ms.Sizer(25,0),
          ms.Spin(values=[0,1,2,3,4],initial_value=0,font=fstyle,size=(8,1),key='atpot'+str(i),),ms.Sizer(15,0),
          ms.Input("",font=fstyle,key='atpxp'+str(i),size=(15,1))
          ],[ms.HSeparator()] ],visible= False,key='atp'+str(i))
    datalist.append([sub1])

layout=[
    [ms.Text("Attendance Register",font=fstylehd)],
    [ms.Text("Entry Person",font=fstyle,size=(12,1)),ms.Combo(values=[],font=fstyle,size=(20,1),key='atpers'),ms.Sizer(swi-650,0),
     ms.Text("Date",font=fstyle,size=(5,1)),ms.InputText("",size=(15,1),font=fstyle,key="atpdate"),
     ms.CalendarButton(" ",target='atpdate',format="%d-%m-%Y",location=(1250,100))],
    [ms.Frame("Entry",layout= [[ms.Column(datalist,scrollable=True,vertical_scroll_only=True,size=(swi-70,shi-170))]],
              font=fstyle,size=(swi-50,shi-150))],
     [ms.Input(default_text= "Password",size=(15,1),font=fstyle,password_char="*",key='atppw')],[ms.Button("Update",font=fstyle,key='atp')]]

TestMenu = ms.Window("Attendance Push",layout,location=(0,0),size=(swi,shi),element_justification='center')

while True:
    event,values=TestMenu.read()
    if event == ms.WIN_CLOSED:
        TestMenu.close()
        break
