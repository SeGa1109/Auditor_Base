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
 if q in days_31:
        l = 31
    elif q in days_30:
        l = 30
    else:
        l = 29
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

def gui():
    j= 101
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
                layout_1.append([ms.Checkbox('', pad=(15, 0), key="holi_chek"),
                                 ms.Text("Mark this day as holiday", font=(fon, si))])
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