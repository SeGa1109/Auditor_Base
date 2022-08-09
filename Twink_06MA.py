def manpower_f(tm, p):
    global MMenu,netwage,netwage2,swlist
    atdata = []
    print(tm)
    q = tm
    Manpower_Menu(q)
    MMenu = ms.Window("Manpower", layout)
    while True:
        event, values = MMenu.read()
        MMenu['mnw'].update(netwage)
        if event == ms.WIN_CLOSED:
            break
        if event == "-refresh-":
            tm = today.strftime("%m")
            MMenu.close()
            manpower_f(tm, p)

        if event == "Add":
            MMenu.Hide()
            Employee_Add_GUI()
            mMenu = ms.Window("Add", layout)
            while True:
                event, values = mMenu.read()
                if event == ms.WIN_CLOSED:
                    p = None
                    MMenu.UnHide()
                    break
                if event == "Add Entry":
                    Add_Employee(values)
                    mMenu.Close()
                    MMenu.close()
                    p = 1
                    manpower_f(tm, p)
        if event =="T5":
            data_selected = [swlist[row] for row in values[event]]
            va1 = data_selected[0]
            MMenu["Eno"].update(va1[0])
            MMenu["Ename"].update(va1[1])
            MMenu["update4"].update(disabled=False)
            MMenu["del4"].update(disabled=False)

        if event == "Upda":
            Attendance_DB(event, values)
        if event == "update4":
            MMenu.Hide()
            x = va1[0]
            Employee_Update_GUI(x)
            eMenu = ms.Window("Edit", layout)
            while True:
                event, values = eMenu.read()
                if event == ms.WIN_CLOSED:
                    MMenu.UnHide()
                    break
                if event == "Update":
                    Employee_Update_DB(values, x)
                    eMenu.close()
                    MMenu.close()
                    manpower_f(tm, p)

        if event == "del4":
            r = va1[0]
            x = ms.popup_ok('Are you sure You want to remove..?')
            if x == "OK":
                ms.popup_animated(gif, time_between_frames=100)
                delete = "delete from attendance.employees where emp_no = '%d'" % (int(r))
                mycursor.execute(delete)
                mydb.commit()
                mm = ['01', '03', '05', '07', '08', '10', '12', '04', '06', '09', '11', '02']
                for x in range(len(mm)):
                    mycursor.execute(
                        "delete from attendance.`%s` where emp_id = '%d' " % (mm[x], int(r)))
                    mydb.commit()
                ms.popup_animated(None)
                ms.PopupTimed("Deleted",
                              title='Employee Removed',
                              button_type=0,
                              auto_close=True,
                              auto_close_duration=1)
                MMenu.Close()
                manpower_f(tm, p)
        if event == "OK3":
            tm = values['mon']
            atdata = []
            MMenu.close()
            p = None
            manpower_f(tm, p)
        if event == "OK4":
            tm = values['mon1']
            print(q)
            atdata = []
            p = None
            MMenu.close()
            manpower_f(tm, p)

        try:
            if event == 'mok':
                dm = values['mdate']
                todays_date = date.today()
                yrs = str(todays_date.year)
                dam = wage_mon( dm)
                MMenu["T6"].update(values=dam)
                MMenu['mnw'].update(netwage)
        except:
            ms.popup_error("Fill the attendance")
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

        if event == "AtRep":
            d = str(ms.popup_get_text("Enter the Number of month in mm"))
            try:
                mycursor.execute("select * from attendance.%s" % d)
                rows = mycursor.fetchall()
                os.chdir("C:\ERP\Master_Files")
                ms.popup_animated(gif, time_between_frames=100)
                inv = openpyxl.load_workbook(filename="Attendance_Master.xlsx")
                xls = inv.active
                row_index = 2
                for x in rows:
                    column_index = 1
                    for y in x:
                        xls.cell(row=row_index, column=column_index).value = y
                        column_index += 1
                    row_index += 1
                os.chdir("C:\ERP\Attendance")
                inv.save('%s.2021.xlsx' % d)
                ms.popup_animated(None)
                os.system("C:\ERP\Attendance\%s.2021.xlsx" % d)
                rows.clear()
                MMenu.Close()
            except:
                ms.popup_error("Please recheck the selection")

                def wage_mon(dm):
                    global atdata, MMenu, netwage
                    todays_date = date.today()
                    yrs = str(todays_date.year)
                    netwage = 0
                    sql = "select emp_no, concat(first_name,' ',last_name) fullname from attendance.employees where salary_mode= 'Monthly' order by emp_no  "
                    mycursor.execute(sql)
                    dat = mycursor.fetchall()
                    print(dat)
                    datas = []
                    print(len(dat))
                    netwage = 0
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
                            v = 0;
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

                def wage_week(start, end):
                    global netwage2
                    netwage = 0
                    blur = []
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
                                    netwage += NW
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
                                    netwage += otw
                                    datas1.append("-")
                                    datas1.append("-")
                                    datas1.append(str(v))
                                    datas1.append(str(otw))
                                    datas1.append(str(otw))
                                print("valuesofwages", datas1)
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
                                    netwage += NW
                                    datas1.append(NW)
                                    print(datas1)
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
                                    netwage += otw
                                    datas1.append(otw)
                            netwage2 = netwage
                            blur.append(datas1)
                        else:
                            break
                    print("valuesofwageselse", blur)
                    retur

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
            v = 0;
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

def Manpower_Menu(q):
    global count, layout, dele, edit, update,swlist
    month=["01","02","03","04","05","06","07","08","09","10","11","12"]
    TL = []
    AB=[]
    head1 = ["E.No","Name","Designation","Salary Mode"]
    sql = ("select emp_no,concat(first_name,'  ',last_name) fullname,designation,salary_mode from attendance.employees")
    mycursor.execute(sql)
    dat = mycursor.fetchall()
    swlist = []
    for i in range(len(dat)):
        x = dat[i]
        print(x)
        sslist = []
        for j in range(4):
            val = str(x[j])
            sslist.append(val)
        swlist.append(sslist)
    j = 101
    m = 0
    sql = ("select emp_no,concat(first_name,'  ',last_name) fullname,designation,salary_mode from attendance.employees")
    mycursor.execute(sql)
    data = mycursor.fetchall()
    dt = [item for t in data for item in t]
    size = int(len(dt) / 40) + 1
    count = int(len(dt) / 4)
    for re in range(size):
        if size - re > 1:
            layout_1 = [
                [ms.Text("E.ID", pad=(100, 0), justification='center',
                         size=(10, 2), font=(fon, si + 3), ),
                 ms.Text("Name", pad=(5, 0), justification='center',
                         size=(20, 2), font=(fon, si + 3), ),
                 ms.Text("P/A", pad=(115, 0), justification='center',
                         size=(5, 2), font=(fon, si + 3), ),
                 ms.Text("OT", pad=(0, 0), justification='center',
                         size=(5, 2), font=(fon, si + 3), )
                 ]]
            for i in range(1, 11):
                l1 = [ms.InputText(dt[m], size=(5, 1), pad=(140, 0), key=str(j)),
                      ms.Text(dt[m + 1], size=(30, 1), pad=(70, 0), key=str(j + 1)),
                      ms.Checkbox('', pad=(15, 0), default=False, key=str(j + 2)),
                      ms.InputText('', size=(10, 1), pad=(95, 0), key=str(j + 3))]
                j += 10
                m += 4
                layout_1.append(l1)
                layout_1.append( [ms.Checkbox('', pad=(15, 0), key="holi_chek"),ms.Text("Mark this day as holiday",font=(fon,si))])
            AB.append(ms.Tab(str(re), layout_1))
    layout_1 = [
        [ms.Text("E.ID", justification='left',
                 size=(10, 2), font=(fon, si + 3), ),
         ms.Text("Name", justification='center',
                 size=(15, 2), font=(fon, si + 3), ),
         ms.Text("P/A", justification='center',
                 size=(20, 2), font=(fon, si + 3), ),
         ms.Text("OT", justification='center',
                 size=(5, 2), font=(fon, si + 3), )
         ]]
    for i in range(int((len(dt) / 4) % 10)):
        l1 = [ms.InputText(dt[m], size=(5, 1), pad=(0, 5), key=str(j)),
              ms.Text(dt[m + 1], size=(15, 1), pad=(100, 5), key=str(j + 1)),
              ms.Checkbox('', pad=(10, 5), default=False, key=str(j + 2)),
              ms.InputText('', size=(10, 5), pad=(80, 0), key=str(j + 3))]
        j += 10
        m += 4
        layout_1.append(l1)
    AB.append(ms.Tab("l", layout_1))

    layout_a = [
        [ms.Text(
            'To win in the marketplace you must first win in the workplace',
            font=(fon, si + 3)),
            ms.Button(" ", image_data=add, size=(15, 1), key="Add")],
              [ms.Table(values=swlist,
                        headings=head1,
                        justification='centre',
                        enable_events=True,
                        auto_size_columns=False,
                        row_height=30,
                        col_widths=[20, 30, 30,10],
                        select_mode=ms.TABLE_SELECT_MODE_EXTENDED,
                        enable_click_events=True,
                        alternating_row_color=ms.theme_input_background_color(),
                        num_rows=10,
                        key="T5")],
        [ms.Text("E.NO :", justification='centre', size=(7, 1), font=(fon, si + 3)),
         ms.Text(" ", justification='centre', size=(5, 1), font=(fon, si + 3), key="Eno"),
         ms.Text("Name :", justification='centre', size=(10, 1), font=(fon, si + 3)),
         ms.Text(" ", justification="centre", font=(fon, si + 3), key="Ename"),
         ms.Button(' ', image_data=edit, size=(10, 1), pad=(0, 5), disabled=True, key="update4"),
         ms.Button(' ', image_data=dele, size=(10, 1), pad=(5, 5), disabled=True, key="del4")]
    ]
    global numdays
    numdays = 3
    base = datetime.date.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]
    layout_b = [
        [
            ms.Text("ATTEND TODAY! ACHIEVE TOMORROW", justification='left', font=(fon, si + 3), ),
            ms.Combo(values=date_list, default_value=date_list[0], size=(20, 1), pad=(25, 0), key='v'),
            ms.Button("Reports", key='AtRep')
        ],
        [ms.TabGroup([AB])],
        [ms.Button("", image_data=update, key="Upda", size=(15, 1), pad=(300, 10), font=(fon, si + 1))]
    ]

    head2=["E.ID","Name","Days Present","Wages"]
    dam=wage_mon( q)
    layout_m = [[ms.Text('Month' ),
                 ms.Combo(month, default_value=dm,
                          size=(20, 1), pad=(0, 0), key='mdate'),
         ms.Button("", image_data=okie, key='mok')],
                [ms.Table(values=dam,
                          headings=head2,
                          justification='centre',
                          enable_events=True,
                          auto_size_columns=False,
                          row_height=30,
                          col_widths=[10, 20, 20,20],
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

    head3 = ["E.ID", "Name", "Days", "Wages", "Ot Hours","OT Wages", "Net Wages"]
    drl=[["","","","","","",""]]
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
                          col_widths=[10, 20, 10, 20,10,20,20],
                          select_mode=ms.TABLE_SELECT_MODE_EXTENDED,
                          enable_click_events=True,
                          alternating_row_color=ms.theme_input_background_color(),
                          num_rows=10,
                          key="T7")],
                [ms.Text("Total wage need", size=(15, 1), pad=(5, 5), font=(fon, si + 4)),
                    ms.Text('', size=(15, 1), pad=(25, 0), key='wnw', font=(fon, si + 4))],
                [ms.Button("", image_data=save, key="Save_w",disabled=True),
                ms.Button("", image_data=prnt, key="prnt_w",disabled=True)]]
    layout_Combo = [[ms.TabGroup([[ms.Tab('Weekly', layout_w, element_justification='c'),
                                   ms.Tab('Monthly', layout_m, element_justification='c')],
                                  ])]]
    if q in days_31:
        l = 31
    elif q in days_30:
        l = 30
    else:
        l = 29
    l_at = m_attendance(l, q)
    layout = [[ms.Button("Refresh", key="-refresh-")],
              [ms.TabGroup([[ms.Tab('List', layout_a, element_justification='c'),
                             ms.Tab('Attendance', layout_b, element_justification='c'),
                             ms.Tab('Wages', layout_Combo, element_justification='c'),
                             ms.Tab('View_Attendance', [[l_at]])]])]
              ]

def m_attendance(l, q):
    global days_31, days_30
    VIEW = []
    the = ("select emp_no,concat(first_name,'  ',last_name) fullname from attendance.employees")
    mycursor.execute(the)
    na = mycursor.fetchall()
    dr = [item for t in na for item in t]
    print(dr)
    siz = int(len(dr) / 20) + 1
    co = int(len(dr) / 2)
    j = 1100101
    v = 0

    sql = ("select *  from attendance.`%s` ; " % q)
    mycursor.execute(sql)
    data = mycursor.fetchall()
    raw = [item for t in data for item in t]
    print(raw)
    print(len(raw))
    gb = []
    if q in days_31:
        n = 31
        b = len(raw)
        a = len(raw) % n
        for i in range(0, b, 31):
            raw.remove(raw[i])
            if b - a == len(raw):
                break

    elif q in days_30:
        n = 30
        b = len(raw)
        a = len(raw) % n
        for i in range(0, b, 30):
            raw.remove(raw[i])
            if b - a == len(raw):
                break
    else:
        n = 29
        b = len(raw)
        a = len(raw) % n
        for i in range(0, b, 29):
            raw.remove(raw[i])
            if b - a == len(raw):
                break
    print(raw)
    print(len(raw))
    z = 0
    for s in range(siz):
        if siz - s > 1:
            layo = []
            low = ["E.ID", "Name"]
            for i in range(1, l + 1):
                if i < 10:
                    low.append("0" + str(i))
                else:
                    low.append(str(i))
            for i in range(1, 11):
                l1 = [str(dr[v]), str(dr[v + 1])]
                print(l)
                for x in range(l):
                    d = z
                    a = raw[d]
                    print("hiiiiiiiiiiiii", a)
                    b = a[1]
                    print("domar")
                    if a[4] != "]":
                        print(a[4])
                        if len(a) == 7:
                            t = str(a[4]) + str(a[5])
                        else:
                            t = str(a[4])
                    else:
                        b = "0"
                    if b == "1":
                        p = "P" + " " + t
                    else:
                        p = "A" + " " + t
                    print(p)
                    l1.append(p)
                    z += 1
                v += 2
                j += n + 2
                z = i * n
                layo.append(l1)
            a = [5, 100]
            for i in range(1, n + 1):
                a.append(10)
            tabl = [[ms.Table(values=layo, headings=low, max_col_width=25,
                              auto_size_columns=True,
                              col_widths=a,
                              justification='left',
                              num_rows=10,
                              alternating_row_color=ms.theme_input_background_color(),
                              key='-TABLE-',
                              row_height=35, )]]
            VIEW.append(ms.Tab(str(s), tabl))
        U = z
    layo = []
    low = ["E.ID", "Name"]
    for i in range(1, l + 1):
        if i < 10:
            low.append("0" + str(i))
        else:
            low.append(str(i))
    for i in range(int((len(dr) / 2) % 10)):
        l1 = [str(dr[v]), str(dr[v + 1])]
        print(l)
        for x in range(l):
            print(len(raw))
            print(z)
            d = z
            a = raw[d]
            print(raw[d])
            print("hiiiiiiiiiiiii", a)
            print("domar", len(a))
            if a[4] != "]":
                print(a[4])
                if len(a) == 7:
                    t = str(a[4]) + str(a[5])
                else:
                    t = str(a[4])
            else:
                t = "0"
            print("att",a[2])
            if a[1] == "1":
                p = "P" + " | " + t
            else:
                p = "A" + " | " + t
            print(p)
            l1.append(p)
            z += 1
        layo.append(l1)
        v += 2
        j += n + 2
        z = U + ((i + 1) * n)

    U = z
    a = [5, 100]
    for i in range(1, n + 1):
        a.append(10)
    tabl = [[ms.Table(values=layo, headings=low, max_col_width=25,
                      auto_size_columns=True,
                      col_widths=a,
                      justification='left',
                      alternating_row_color=ms.theme_input_background_color(),
                      key='-TABLE-',
                      row_height=35)]]
    VIEW.append(ms.Tab(" l ", tabl))
    print(raw)
    for i in range(1,n):
        holi=raw[i-1]
        if holi[1]=="H":
            if i <10:
                hide_c="0"+str(i)
            else:
                hide_c=str(i)
    displaycolumns = deepcopy(a)
    displaycolumns.remove(hide_c)
    table.ColumnsToDisplay = displaycolumns
    table.Widget.configure(displaycolumns= displaycolumns)


    Month = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    layout_c = [[ms.Text('Month', size=(10, 1), pad=(0, 0), justification='right'),
                 ms.Combo(Month, default_value=q, size=(20, 1), pad=(0, 0), key='mon', ),
                 ms.Button("", image_data=okie, key='OK3'), ], [ms.TabGroup([VIEW])]]
    r = ms.Column(layout_c, scrollable=True, size=(1000, 500))
    return r

def Employee_Add_GUI():
    global layout
    Gender = ('M', 'F', 'O')
    Blood_Group = ('O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-')
    Salaried = ('Weekly', 'Monthly')
    layout = [
        [ms.Text("First name", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.InputText('', size=(20, 1), key=1)],
        [ms.Text("Last name", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.InputText('', size=(20, 1), key=2)],

        [ms.Text("Gender", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.Combo(values=Gender, default_value='', size=(20, 1), key=3)],

        [ms.Text('D.O.B                                              ', ),
         ms.InputText("", size=(20, 1), key='4a'),
         ms.CalendarButton('', image_data=chse, format='%d_%m_%Y', target='4a',
                           pad=(0, 0), size=(5, 1), key='date1')],

        [ms.Text('D.O.J                                                ', ),
         ms.InputText("", size=(20, 1), pad=(0, 5), key='5b'),
         ms.CalendarButton('', image_data=chse, format='%d_%m_%Y', target='5b',
                           pad=(5, 0), size=(5, 1), key='date2')],

        [ms.Text("Blood_Group", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.Combo(values=Blood_Group, default_value='', size=(20, 1), key=6)],

        [ms.Text("Designation", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.InputText('', size=(20, 1), key=7)],

        [ms.Text("salary", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.InputText('', size=(20, 1), key=8)],

        [ms.Text("Address", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.Multiline('', size=(20, 1), key=9)],

        [ms.Text("Phone_no", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.InputText('', size=(20, 1), key=10)],

        [ms.Text("Salaried", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.Combo(values=Salaried, default_value='', size=(20, 1), key=11)],
        [ms.Button("", image_data=update, key="Add Entry", size=(15, 1), pad=(220, 20), font=(fon, si + 1))],

    ]
    return layout

def Add_Employee(values):
    if values[1] and values[2] and values[3] and values['4a'] and values['5b'] and values[9] and values[6] and values[
        7] and values[8] and values[10] and values[11] != "":
        ms.popup_animated(gif, time_between_frames=100)
        A = values[1]
        B = values[2]
        C = values[3]
        D = values['4a']
        E = values['5b']
        F = values[9]
        G = values[6]
        H = values[7]
        I = values[8]
        J = values[10]
        K = values[11]

        dict = {'first_name': A, 'last_name': B, 'gender': C, 'birth_date': D,
                'hire_date': E, 'address': F, 'blood_group': G, 'designation': H,
                'salary': I, 'phone_no': J, 'salary_mode': K}
        print(dict)
        placeholders = ', '.join(['%s'] * len(dict))
        columns = ', '.join(dict.keys())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('attendance.employees',
                                                       columns, placeholders)
        mycursor.execute(sql, list(dict.values()))
        mydb.commit()
        mycursor.execute("Use Attendance")
        mm = ['01', '03', '05', '07', '08', '10', '12', '04', '06', '09', '11', '02']
        for x in range(len(mm)):
            mycursor.execute("INSERT INTO `%s` (`1`) VALUE ('[0,0]')" % mm[x])
            mydb.commit()
        mycursor.execute("Use erp_db")
        ms.popup_animated(None)
        ms.PopupTimed("Added",
                      title='Employee Added',
                      button_type=0,
                      auto_close=True,
                      auto_close_duration=1)

    else:
        ms.popup("Enter valid info..!")

def Employee_Update_GUI(x):
    global layout
    mycursor.execute("select * from attendance.employees where emp_no=%d " % int(x))
    dat = mycursor.fetchall()
    out = [item for t in dat for item in t]
    Gender = ('M', 'F', 'O')
    Blood_Group = ('O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-')
    Salaried = ('Weekly', 'Monthly')
    layout = [
        [ms.Text("First name", justification='left', size=(20, 1),
                 font=(fon, si + 1),
                 ),
         ms.Text(out[1], size=(20, 1), key=19),
         ms.InputText('', do_not_clear=False, size=(20, 1), key=20)

         ],
        [ms.Text("Last name", justification='left', size=(20, 1),
                 font=(fon, si + 1),
                 ),
         ms.Text(out[2], size=(20, 1), key=21, ),
         ms.InputText('', do_not_clear=False, size=(20, 1), key=22)],

        [ms.Text("Gender", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.Text(out[3], size=(20, 1), key=23, ),
         ms.Combo(values=Gender, default_value='', size=(20, 1), key=24)],

        [ms.Text('D.O.B                                         ',
                 ),
         ms.Text(out[4], size=(20, 1), key='cal1', ),
         ms.InputText("", size=(20, 1), key='4'),
         ms.CalendarButton('', image_data=chse, format='%d_%m_%Y', target='4',
                           pad=(0, 0), size=(5, 1), key='date1')],

        [ms.Text('D.O.J                                          ', ),
         ms.Text(out[5], size=(20, 1), key='cal2', ),
         ms.InputText("", size=(20, 1), pad=(5, 5), key='5'),
         ms.CalendarButton('', image_data=chse, format='%d_%m_%Y', target='5',
                           pad=(0, 0), size=(5, 1), key='date2')],

        [ms.Text("Blood_Group", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.Text(out[7], size=(20, 1), key=29, ),
         ms.Combo(values=Blood_Group, default_value='', size=(20, 1), key=30)],

        [ms.Text("Designation", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.Text(out[8], size=(20, 1), key=31, ),
         ms.InputText('', do_not_clear=False, size=(20, 1), key=32)],

        [ms.Text("salary", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.Text(out[9], size=(20, 1), key=33, ),
         ms.InputText('', do_not_clear=False, size=(20, 1), key=34)],

        [ms.Text("Address", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.Text(out[6], size=(20, 1), key=35, ),
         ms.InputText('', do_not_clear=False, size=(20, 1), key=36)],

        [ms.Text("Phone_no", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.Text(out[10], size=(20, 1), key=39, ),
         ms.InputText('', do_not_clear=False, size=(20, 1), key=40)],

        [ms.Text("Salaried", justification='left', size=(20, 1), font=(fon, si + 1),
                 ),

         ms.Text(out[11], size=(20, 1), key=41, ),
         ms.Combo(values=Salaried, default_value='', size=(20, 1), key=42)],
        [ms.Button("", image_data=update, key="Update", size=(15, 1), pad=(270, 20), font=(fon, si + 1))]
    ]

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

def sorted_name():
    sql = "SELECT emp_no,concat(first_name,'  ',last_name) fullname FROM " \
          "attendance.employees ORDER BY fullname;"
    mycursor.execute(sql)
    list = mycursor.fetchall()
    employeesortednamelist = [item for t in list for item in t]
    return employeesortednamelist

def Employee_Update_DB(values, x):
    ms.popup_animated(gif, time_between_frames=100)
    emp_id = x
    A = values[20]
    B = values[22]
    C = values[24]
    D = values['4']
    E = values['5']
    F = values[30]
    G = values[32]
    H = values[34]
    I = values[36]
    J = values[40]
    K = values[42]
    print(A, B, C, D, E, F, G, H, I, J, K)
    if A != "":
        sql = "UPDATE attendance.attendance.employees SET first_name = '%s' where emp_no = '%s'" \
              % (A, emp_id)
        mycursor.execute(sql)
        mydb.commit()

    if B != "":
        sql = "UPDATE attendance.employees SET last_name = '%s' where emp_no = '%s'" \
              % (B, emp_id)
        mycursor.execute(sql)
        mydb.commit()

    if C != "":
        sql = "UPDATE attendance.employees SET gender = '%s' where emp_no = '%s'" \
              % (C, emp_id)
        mycursor.execute(sql)
        mydb.commit()
    if D != "":
        sql = "UPDATE attendance.employees SET birth_date = '%s' where emp_no = '%s'" \
              % (D, emp_id)
        mycursor.execute(sql)
        mydb.commit()
    if E != "":
        sql = "UPDATE attendance.employees SET hire_date = '%s' where emp_no = '%s'" \
              % (E, emp_id)
        mycursor.execute(sql)
        mydb.commit()
    if I != "":
        sql = "UPDATE attendance.employees SET address = '%s' where emp_no = '%s'" \
              % (I, emp_id)
        mycursor.execute(sql)
        mydb.commit()
    if G != "":
        sql = "UPDATE attendance.employees SET designation = '%s' where emp_no = '%s'" \
              % (G, emp_id)
        mycursor.execute(sql)
        mydb.commit()
    if F != "":
        sql = "UPDATE attendance.employees SET blood_group = '%s' where emp_no = '%s'" \
              % (F, emp_id)
        mycursor.execute(sql)
        mydb.commit()
    if H != "":
        sql = "UPDATE attendance.employees SET salary = '%s' where emp_no = '%s'" \
              % (H, emp_id)
        mycursor.execute(sql)
        mydb.commit()
    if J != "":
        sql = "UPDATE attendance.employees SET phone_no = '%s' where emp_no = '%s'" \
              % (J, emp_id)
        mycursor.execute(sql)
        mydb.commit()
    if K != "":
        sql = "UPDATE attendance.employees SET salary_mode = '%s' where emp_no = '%s'" \
              % (K, emp_id)
        mycursor.execute(sql)
        mydb.commit()
    ms.popup_animated(None)
    ms.PopupTimed("Updated",
                  title='Details Updated',
                  button_type=0,
                  auto_close=True,
                  auto_close_duration=1)
# ----------------------------------------------------------------------------------------------------------"attendance"

def Attendance_DB(event, values):
    ms.popup_animated(gif, time_between_frames=100)
    global emp, mont, day, numdays
    date = str(values['v'])
    Ldate = list(date.split("-"))
    Date = [int(i) for i in Ldate]
    mont = Ldate[1]
    day = Date[2]
    atn = 103
    id = 101
    t = 104
    emp = sorted_name()
    for p in range(0, len(emp), 2):
        if values[str(atn)] == True:
            if values[str(t)] == "":
                ot = 0
            else:
                ot = int(values[str(t)])
            eid = int(values[str(id)])
            print(ot)
            at = [1, ot]
            print(at)
            print(mont, day, at, eid)
            mycursor.execute(
                "update  Attendance.`%s` set `%s` = '%s' where emp_id='%s'" % (mont, day, at, eid))
            mydb.commit()
            atn += 10
            t += 10
            id += 10
        else:
            if values[str(t)] == "":
                ot = 0
            else:
                ot = int(values[str(t)])
            eid = int(values[str(id)])
            at = [0, ot]
            print(mont, day, at, eid)
            mycursor.execute("update  Attendance.`%s` set `%s` = '%s' where emp_id='%s'" % (mont, day, at, eid))
            mydb.commit()
            atn += 10
            t += 10
            id += 10
    ms.popup_animated(None)
    ms.PopupTimed("Updated",
                  title='Update',
                  button_type=0,

                  auto_close=True,
                  auto_close_duration=1)
