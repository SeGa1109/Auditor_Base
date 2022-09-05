from Env import *
def CC_View_GUI():
    mycursor.execute("select wrk_date,crew_name,discription from cc_attendence as catd "
                     "inner join cleaning_crew as cc on catd.UID  = cc.UID "
                     "inner join cc_work_list as cwl on catd.WID =cwl.WID ")
    globals()['cv_data']=[list(x) for x in mycursor.fetchall()]
    mycursor.execute("select discription from cc_work_list")
    f_dis=list(sum(mycursor.fetchall(),()))
    mycursor.execute("select crew_name from cleaning_crew")
    f_name = list(sum(mycursor.fetchall(), ()))
    C_view=[ms.Table(values=cv_data, headings=["Date","Name","Discription"],
                justification='centre', enable_events=True,
                auto_size_columns=False,
                row_height=20,
                col_widths=[13,30,80],
                num_rows=28,
                font=fstyle,
                enable_click_events=True, key="cc_view")]
    layout = [[
               ms.Sizer(70,0),
               ms.Text("Date", font=fstyle, justification='left',size=(7, 1)),
               ms.Sizer(150,0),
               ms.Text("Name", font=fstyle, size=(7, 1)),
               ms.Sizer(500,0),
               ms.Text("Discription", font=fstyle, size=(13, 1))],
              [ms.Sizer(88,0),ms.CalendarButton(" ", target='cvf_date', format="%y-%m-%d"),
               ms.Input("", enable_events=True, size=(13, 1),pad=(0,0), font=fstyle, key='cvf_date'),
               ms.Combo(f_name, enable_events=True, size=(28, 1),pad=(0,0), font=fstyle, key='cvf_name'),
               ms.Combo(f_dis, enable_events=True, size=(79, 1),pad=(0,0), font=fstyle, key='cvf_dis')],
              [ms.Frame("Output", layout=[C_view,
               [ms.Button("Export", key='cc_export', font=fstyle)],], size=(swi - 70, shi - 100), font=fstyle, element_justification='center')]
              ]
    return layout
def c_view_db(event,values,Menu):
    if event == 'cvf_date':
        mycursor.execute("select wrk_date,crew_name,discription from cc_attendence  as catd "
                         "inner join cleaning_crew as cc on catd.UID  = cc.UID "
                         "inner join cc_work_list as cwl on catd.WID =cwl.WID where wrk_date='%s'" % values['cvf_date'])
        globals()['cv_data']=[list(x) for x in mycursor.fetchall()]
        Menu["cc_view"].update(values=cv_data)
    if event == "cvf_name":
        mycursor.execute("select wrk_date,crew_name,discription from cc_attendence  as catd "
                         "inner join cleaning_crew as cc on catd.UID  = cc.UID "
                         "inner join cc_work_list as cwl on catd.WID =cwl.WID where crew_name='%s'" % values['cvf_name'])
        globals()['cv_data'] = [list(x) for x in mycursor.fetchall()]
        Menu["cc_view"].update(values=cv_data)
    if event == "cvf_dis":
        mycursor.execute("select wrk_date,crew_name,discription from cc_attendence  as catd "
                         "inner join cleaning_crew as cc on catd.UID  = cc.UID "
                         "inner join cc_work_list as cwl on catd.WID =cwl.WID where discription='%s'" % values['cvf_dis'])
        globals()['cv_data'] = [list(x) for x in mycursor.fetchall()]
        Menu["cc_view"].update(values=cv_data)
    if event == "cc_export":
        data = cv_data
        xl = openpyxl.load_workbook(filename=r'C:\Twink_06MA\Master_Files\Atn_Exp.xlsx')
        for step in ['Attendance', 'OT', 'Expenses']:
            xl.active = xl[step]
            xlc = xl.active
            atndata = datasplit(copy.deepcopy(data), step)
            crow = 2
            ccol = 1
            for part in atndata:
                for i in range(len(part)):
                    xlc.cell(row=crow, column=ccol).value = part[i]
                    ccol += 1
                crow += 1
                ccol = 1

        xl.save(filename=r'C:\Twink_06MA\Master_Files\Atn_ExpT1.xlsx')
        os.system(r'C:\Twink_06MA\Master_Files\Atn_ExpT1.xlsx')