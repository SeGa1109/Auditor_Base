import copy

from Env import *


def AttendanceViewLay():
    head=['Emp.Code','Name','F/S Name']
    headwidth=[15,30,30]
    #----
    for i in range (1,32):
        head.append(str(i).zfill(2))
        headwidth.append(7)
    #print(todatemy)
    globals()['atnvwdata']=attendance_fetch(todatemy)
    data=copy.deepcopy(atnvwdata)
    TL=ms.Table(values=datasplit(data,"Attendance"), headings=head,
                justification='centre', enable_events=True,
                auto_size_columns=False,
                row_height=20,
                col_widths=headwidth,
                num_rows=100,
                font=fstyle,
                enable_click_events=True, key="TL_Atview")
    #print(data)
    #print(atnvwdata)
    layout=[[ms.Sizer(swi-1500),ms.Text("Attendance View",font=fstylehd,justification='center')],
            [ms.Combo(['Attendance','OT','Expenses','Atn+ot','DP_List'],default_value="Attendance",
                      enable_events=True, key='atnvwfltr',size=(15,4),font=fstyle),ms.Sizer(swi -500),
             ms.Text("Date",font=fstyle,size=(7,1)),ms.Input(todatemy,disabled= True,enable_events=True, size=(8,2),font=fstyle,key='atvwdate'),
             ms.CalendarButton(" ",target='atvwdate',format="%m-%Y")],
            [ms.Frame("Output",layout=[[ms.Column([[TL]],size=(swi-70,shi-200),scrollable=True)],
                                        [ms.Button("Export",key='wcxlexp',font=fstyle)],
                                       ],size=(swi-70,shi-100),font=fstyle,element_justification='center')]
            ]

    return layout

'''
TestMenu=ms.Window("", AttendanceViewLay(),location=(0,0),element_justification='center')
while True:
    event,values = TestMenu.read()

'''

def AttendaceViewFn(Menu,event,values):
    if event == 'atnvwfltr':

        Menu['TL_Atview'].update(values=datasplit(copy.deepcopy(atnvwdata),values['atnvwfltr']))

    if event == 'atvwdate':
        globals()['atnvwdata'] = attendance_fetch(values['atvwdate'])
        Menu['TL_Atview'].update(values=datasplit(copy.deepcopy(atnvwdata), values['atnvwfltr']))

    if event == 'wcxlexp':
        data=attendance_fetch(values['atvwdate'])
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






        

