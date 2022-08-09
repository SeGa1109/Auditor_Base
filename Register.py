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
def employee_list_gui():
    head1 = ["E.No", "Name", "Designation", "Salary Mode"]
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
                  col_widths=[20, 30, 30, 10],
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