
def wage_mon(dm):
    global atdata,MMenu,netwage
    todays_date = date.today()
    yrs = str(todays_date.year)
    netwage = 0
    sql = "select emp_no, concat(first_name,' ',last_name) fullname from attendance.employees where salary_mode= 'Monthly' order by emp_no  "
    mycursor.execute(sql)
    dat = mycursor.fetchall()
    print(dat)
    datas=[]
    print(len(dat))
    netwage=0
    for i in range(len(dat)):
        print("i",i)
        print("dat",len(dat))
        if i<len(dat):
            datas1 = []
            a = dat[i]
            print(a)
            for j in range(2):
                x = a[j]
                datas1.append(str(x))
            emplist = int(datas1[0])
            mon = "`" + str(dm) + "`"
            print(mon)
            sql = "select * from attendance.%s where emp_id = '%d'" % (mon, emplist)
            mycursor.execute(sql)
            dath = mycursor.fetchall()
            gcell = [item for t in dath for item in t]
            del gcell[0]
            sql = "select salary from attendance.employees where emp_no='%d'" % emplist
            mycursor.execute(sql)
            datf = mycursor.fetchall()
            print(dat)
            salary = datf[0][0]
            v = 0
            wage = 0
            for x in range(len(gcell)):
                v += int(gcell[x][1])
            datas1.append(str(v))
            wage = v * salary
            netwage += wage
            datas1.append(str(wage))

            datas.append(datas1)
        else:
            break

    return datas

def gui():
    head2 = ["E.ID", "Name", "Days Present", "Wages"]
    dam = wage_mon(q)
    layout_m = [[ms.Text('Month'),
                 ms.Combo(month, default_value=dm,
                          size=(20, 1), pad=(0, 0), key='mdate'),
                 ms.Button("", image_data=okie, key='mok')],
                [ms.Table(values=dam,
                          headings=head2,
                          justification='centre',
                          enable_events=True,
                          auto_size_columns=False,
                          row_height=30,
                          col_widths=[10, 20, 20, 20],
                          select_mode=ms.TABLE_SELECT_MODE_EXTENDED,
                          enable_click_events=True,
                          alternating_row_color=ms.theme_input_background_color(),
                          num_rows=10,
                          key="T6")],
                [ms.Text("Total wage need", size=(15, 1), pad=(5, 5), font=(fon, si + 2)),
                 ms.Text('', size=(15, 1), pad=(15, 0), key='mnw', font=(fon, si + 2))],
                [ms.Button("", image_data=save, key="Save_m"),
                 ms.Button("", image_data=prnt, key="prnt_m")]
                ]

    head3 = ["E.ID", "Name", "Days", "Wages", "Ot Hours", "OT Wages", "Net Wages"]
    drl = [["", "", "", "", "", "", ""]]
    layout_w = [[ms.Text('Start Date', ),
                 ms.InputText("", size=(20, 1), pad=(0, 5), key='WCS'),
                 ms.CalendarButton('Choose', image_data=chse, format='%d_%m', target='WCS',
                                   pad=(5, 0), size=(5, 1), key='date1'),
                 ms.Text('End Date', ),
                 ms.InputText("", size=(20, 1), pad=(0, 5), key='WCE'),
                 ms.CalendarButton('Choose', image_data=chse, format='%d_%m', target='WCE',
                                   pad=(5, 0), size=(5, 1), key='date2'),
                 ms.Button("", image_data=okie, key='wok')
                 ],
                [ms.Table(values=drl,
                          headings=head3,
                          justification='centre',
                          enable_events=True,
                          auto_size_columns=False,
                          row_height=30,
                          col_widths=[10, 20, 10, 20, 10, 20, 20],
                          select_mode=ms.TABLE_SELECT_MODE_EXTENDED,
                          enable_click_events=True,
                          alternating_row_color=ms.theme_input_background_color(),
                          num_rows=10,
                          key="T7")],
                [ms.Text("Total wage need", size=(15, 1), pad=(5, 5), font=(fon, si + 4)),
                 ms.Text('', size=(15, 1), pad=(25, 0), key='wnw', font=(fon, si + 4))],
                [ms.Button("", image_data=save, key="Save_w", disabled=True),
                 ms.Button("", image_data=prnt, key="prnt_w", disabled=True)]]
    layout_Combo = [[ms.TabGroup([[ms.Tab('Weekly', layout_w, element_justification='c'),
                                   ms.Tab('Monthly', layout_m, element_justification='c')],
                                  ])]]

def wage_week(start,end):
    global netwage2
    netwage = 0
    blur=[]
    sql = "select emp_no, concat(first_name,' ',last_name) fullname from attendance.employees order by emp_no  "
    mycursor.execute(sql)
    dat = mycursor.fetchall()
    for i in range(len(dat)):
        print("i", i)
        print("dat", len(dat))
        if i < len(dat):
            datas1 = []
            a = dat[i]
            print(a)
            for j in range(2):
                x = a[j]
                datas1.append(str(x))
            emplist = int(datas1[0])
            if start[1] == end[1]:
                days = list(range(int(start[0]), int(end[0]) + 1))
                ran = "`" + "`,`".join(str(x) for x in days) + "`"
                mon = "`" + end[1] + "`"
                sql = "select salary_mode from attendance.employees where " \
                      "emp_no='%d'" % emplist
                mycursor.execute(sql)
                datu = mycursor.fetchall()
                smode = datu[0][0]
                if smode == "Weekly":
                    sql = "select %s from attendance.%s where emp_id = '%d'" % (ran, mon, emplist)
                    mycursor.execute(sql)
                    datq = mycursor.fetchall()
                    print(datq)
                    gcell = [item for t in datq for item in t]
                    sql = "select salary from attendance.employees where emp_no='%d'" % \
                          emplist
                    mycursor.execute(sql)
                    datw = mycursor.fetchall()
                    salary = datw[0][0]
                    v = 0;
                    otw = 0;
                    wage = 0
                    for x in range(len(gcell)):
                        v += int(gcell[x][1])
                    wage = v * salary
                    datas1.append(str(v))
                    datas1.append(wage)
                    v = 0
                    print(gcell)
                    for x in range(len(gcell)):
                        v += int(gcell[x][4])
                    otw = (v * salary) / 8
                    datas1.append(str(v))
                    datas1.append(str(otw))
                    NW = otw + wage
                    netwage+=NW
                    datas1.append(str(NW))

                if smode == "Monthly":
                    sql = "select %s from attendance.%s where emp_id = '%d'" % (ran, mon, emplist)
                    mycursor.execute(sql)
                    datt = mycursor.fetchall()
                    gcell = [item for t in datt for item in t]
                    sql = "select salary from attendance.employees where emp_no='%d'" % \
                          emplist
                    mycursor.execute(sql)
                    daty = mycursor.fetchall()
                    salary = daty[0][0]
                    v = 0;
                    otw = 0
                    print(gcell)
                    for x in range(len(gcell)):
                        v += int(gcell[x][4])
                    print(v)
                    otw = (v * salary) / 8
                    netwage+=otw
                    datas1.append("-")
                    datas1.append("-")
                    datas1.append(str(v))
                    datas1.append(str(otw))
                    datas1.append(str(otw))
                print("valuesofwages",  datas1)
            else:
                if start[1] == "01" or "03" or "05" or "07" or "08" or "10" or "12":
                    days1 = list(range(int(start[0]), 32))
                elif start[1] == "04" or "06" or "09" or "11":
                    days1 = list(range(int(start[0]), 31))
                elif start[1] == "02":
                    days1 = list(range(int(start[0]), 30))
                days2 = list(range(1, int(end[0]) + 1))
                ran1 = "`" + "`,`".join(str(x) for x in days1) + "`"
                ran2 = "`" + "`,`".join(str(x) for x in days2) + "`"
                mon1 = "`" + start[1] + "`"
                mon2 = "`" + end[1] + "`"
                sql = "select salary_mode from attendance.employees where " \
                      "emp_no='%d'" % emplist
                mycursor.execute(sql)
                dati = mycursor.fetchall()
                smode = dati[0][0]
                # ---
                if smode == "Weekly":
                    sql = "select %s from attendance.%s where emp_id = '%d'" % (
                        ran1, mon1, emplist)
                    mycursor.execute(sql)
                    dato = mycursor.fetchall()
                    gcell1 = [item for t in dato for item in t]
                    # ---
                    sql = "select %s from attendance.%s where emp_id = '%d'" % (
                        ran2, mon2, emplist)
                    mycursor.execute(sql)
                    datp = mycursor.fetchall()
                    gcell2 = [item for t in datp for item in t]
                    # ---
                    sql = "select salary from attendance.employees where emp_no='%d'" % \
                          emplist
                    mycursor.execute(sql)
                    dats = mycursor.fetchall()
                    salary = dats[0][0]
                    # ---
                    v = 0;
                    otw = 0;
                    wage = 0
                    for x in range(len(gcell1)):
                        v += int(gcell1[x][1])
                    for x in range(len(gcell2)):
                        v += int(gcell2[x][1])
                    wage = v * salary
                    print(v)
                    datas1.append(v)
                    datas1.append(wage)
                    v = 0
                    for x in range(len(gcell1)):
                        v += int(gcell1[x][4])
                    for x in range(len(gcell2)):
                        v += int(gcell2[x][4])
                    otw = (v * salary) / 8
                    print(v)
                    datas1.append(v)
                    datas1.append(otw)
                    NW = otw + wage
                    netwage+=NW
                    datas1.append(NW)
                    print( datas1)
                if smode == "Monthly":
                    sql = "select %s from attendance.%s where emp_id = '%d'" % (
                        ran1, mon1, emplist)
                    mycursor.execute(sql)
                    datd = mycursor.fetchall()
                    gcell1 = [item for t in datd for item in t]
                    # ---
                    sql = "select %s from attendance.%s where emp_id = '%d'" % (
                        ran2, mon2, emplist)
                    mycursor.execute(sql)
                    datf = mycursor.fetchall()
                    gcell2 = [item for t in datf for item in t]
                    # ---
                    sql = "select salary from attendance.employees where emp_no='%d'" % \
                          emplist
                    mycursor.execute(sql)
                    datg = mycursor.fetchall()
                    salary = datg[0][0]
                    v = 0;
                    otw = 0
                    for x in range(len(gcell1)):
                        v += int(gcell1[x][4])
                    for x in range(len(gcell2)):
                        v += int(gcell2[x][4])
                    otw = (v * salary) / 8
                    datas1.append("-")
                    datas1.append("-")
                    datas1.append(v)
                    datas1.append(otw)
                    netwage+=otw
                    datas1.append(otw)
            netwage2=netwage
            blur.append(datas1)
        else:
            break
    print("valuesofwageselse",blur)
    return blur

def wages_save_DB(a, values, dy, start, end, data, atdata):
    ms.popup_animated(gif, time_between_frames=100)
    wdata = []
    st = start[0]
    en = end[0]
    m = start[1]
    print("sscsc", len(atdata))
    j = 0
    for i in range(0, len(data), 2):
        wdata.append(data[i])
        wdata.append(data[i + 1])
        wdata.append(atdata[j])
        wdata.append(atdata[j + 1])
        wdata.append(atdata[j + 2])
        wdata.append(atdata[j + 3])
        wdata.append(atdata[j + 4])
        j += 5

    os.chdir("C:\ERP\Master_Files")
    inv = openpyxl.load_workbook(filename="wages_report_master.xlsx")
    xls = inv.active
    row_index = 2
    print("wdata", wdata)
    print(len(wdata))
    rows = len(wdata) // 7
    i = 0
    for x in range(rows):
        column_index = 1
        for y in range(7):
            xls.cell(row=row_index, column=column_index).value = wdata[y + i]
            column_index += 1
        i += 7
        row_index += 1
    inv.save('C:\ERP\wages\weekly\weekly_(%s-%s)-%s-%s.xlsx' % (st, en, m, dy))
    ms.popup_animated(None)
    os.system('C:\ERP\wages\weekly\weekly_(%s-%s)-%s-%s.xlsx' % (st, en, m, dy))
    if a == "prnt":
        os.startfile('C:\ERP\wages\weekly\weekly_(%s-%s)-%s-%s.xlsx' % (st, en, m, dy), 'print')

def monthly_save(b, values, mon, yrs, data, atdata):
    ms.popup_animated(gif, time_between_frames=100)
    mdata = []
    for i in range(len(data)):
        mdata.append(data[i])
        mdata.append(data[i + 1])
        for j in range(len(atdata)):
            mdata.append(atdata[j])
            mdata.append(atdata[j + 1])
            j += 3
        i += 2
    os.chdir("C:\ERP\Master_Files")
    inv = openpyxl.load_workbook(filename="monthly_wages_report_master.xlsx")
    xls = inv.active
    row_index = 2
    rows = len(mdata) // 4
    i = 0
    for x in range(rows):
        column_index = 1
        for y in range(4):
            xls.cell(row=row_index, column=column_index).value = mdata[y + i]
            column_index += 1
        i += 4
    inv.save('C:\ERP\wages\monthly\monthly_%s_%s.xlsx' % (mon, yrs))
    ms.popup_animated(None)
    os.system('C:\ERP\wages\monthly\monthly_%s_%s.xlsx' % (mon, yrs))
    if b == "prnt":
        os.startfile('C:\ERP\wages\monthly\monthly_%s_%s.xlsx' % (mon, yrs), 'print')

if event == "Save_m":
            b = "ddddd"
            monthly_save(b, values, mon, yrs, data, atdata)
            ms.popup_ok('Saved Sucessfully')
            MMenu['Save_m'].update(disabled=True)
if event == "prnt_m":
    b = "prnt"
    monthly_save(b, values, mon, yrs, data, atdata)
    ms.popup_ok('Saved and printed Sucessfully')
    MMenu['Save_m'].update(disabled=True)
    MMenu['prnt_m'].update(disabled=True)
if event == 'wok':
    MMenu["Save_w"].update(disabled=False)
    MMenu["prnt_w"].update(disabled=False)
    start = list(values['WCS'].split("_"))
    end = list(values['WCE'].split("_"))
    drl=wage_week(start,end)
    MMenu["T7"].update(values=drl)
    MMenu['wnw'].update(netwage2)
if event == "prnt_w":
    a = "prnt"
    todays_date = date.today()
    dy = str(todays_date.year)
    wages_save_DB(a, values, dy, start, end, data, atdata)
    ms.popup_ok('Saved and printed Sucessfully')
    MMenu['Save_w'].update(disabled=True)
    MMenu['prnt_w'].update(disabled=True)
if event == "Save_w":
    a = "jhgu"
    todays_date = date.today()
    dy = str(todays_date.year)
    wages_save_DB(a, values, dy, start, end, data, atdata)
    ms.popup_ok('Saved  Sucessfully')
    MMenu['Save_w'].update(disabled=True)