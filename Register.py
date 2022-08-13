from Env import *


def RegsiterLay():
    layout = [[ms.Text("Employee Register", font=fstylehd)],
              [ms.Sizer(swi - 200, 0),
               ms.Button("Export", font=fstyle, key='empexp'),
               ms.Button("Add", font=fstyle, key='empadd')],

              [ms.Frame("Employee Data",
                        [[ms.Table(values=EmpdataFetch(),
                                   headings=["Employee Code", "Name", "Father/Spouse Name", "Gender", "Phone No.",
                                             "Base Salary"],
                                   justification='centre', enable_events=True, auto_size_columns=False, row_height=30,
                                   col_widths=[15, 40, 40, 10, 20, 15],
                                   right_click_selects=True,
                                   right_click_menu=[[], ["Update Employee", "Remove"]],
                                   enable_click_events=True, size=(swi - 70, shi - 120), key="emp_data", font=fstyle)]],
                        font=fstyle, size=(swi - 50, shi - 100), element_justification='center')]]

    return layout


def RegisterFn(Menu, event, values):

    def Employee_Add_GUI():
        Employee_Details = [
            [ms.Text("Employee Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e1', font=fstyle)],
            [ms.Text("Emp Code:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1),default_text=Emp_code_Gen("PF"), do_not_clear=True, key='e2', font=fstyle)],
            [ms.Text("ESIC NO:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e3', font=fstyle)],
            [ms.Text("UAN NO:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e4', font=fstyle)],
            [ms.Text("Aadhar No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e5', font=fstyle)],
            [ms.Text("Address:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Multiline("", size=(28, 3), do_not_clear=True, key='e6', font=fstyle)],
            [ms.Text("Father/Spouse Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e7', font=fstyle)],
            [ms.Text("Gender:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Radio("M","gender", size=(5, 1), key='e8', font=fstyle),
             ms.Radio("F","gender", size=(5, 1), key='e8', font=fstyle),
             ms.Radio("O","gender", size=(5, 1), key='e8', font=fstyle)],
            [ms.Text("Shift Work:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Radio("Yes","sw", size=(5, 1), key='e9', font=fstyle),
             ms.Radio("No","sw", size=(5, 1), key='e9', font=fstyle)],
            [ms.Text("Base salary:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e10', font=fstyle)],
            [ms.Text("Shift 1 salary:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e11', font=fstyle)],
            [ms.Text("Shift 2 salary:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e12', font=fstyle)],
            [ms.Text("Shift 3 salary:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e13', font=fstyle)],
            [ms.Text("Phone No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e14', font=fstyle)],
            [ms.Text("Bank Account Number:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e15', font=fstyle)],
            [ms.Text("Bank Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e16', font=fstyle)],
            [ms.Text("IFSC Code:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e17', font=fstyle)],
            [ms.Text("Branch:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e18', font=fstyle)],
            [ms.Text("Date of Birth :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(26, 1), do_not_clear=True, key='e19', font=fstyle),
             ms.CalendarButton('Choose',image_data=chse, format='%d_%m_%y', target='e19', font=fstyle, size=(6, 1), key='date1'), ],
            [ms.Text("Date of Joining :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(26, 1), do_not_clear=True, key='e20', font=fstyle),
             ms.CalendarButton('Choose',image_data=chse, format='%d_%m_%y', font=fstyle, target='e20', size=(6, 1), key='date1'), ],
            [ms.Text("photo:", justification='left', size=(20, 1), font=fstyle),
             ms.Input("", size=(19, 1), do_not_clear=True, key='e21', font=fstyle),
             ms.FileBrowse(file_types=file_types,size=(6,1),enable_events=True, target="e21",key="b1", font=fstyle),
             ms.Button("Load",image_data=load, font=fstyle,size=(5,1), key="load pimg"), ms.Sizer(2, 0),
             ],
            [ms.Text("Specimen Signature:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(19, 1), do_not_clear=True, key='e22', font=fstyle),
             ms.FileBrowse(file_types=file_types,size=(6,1),enable_events=True, target="e22",key="b2", font=fstyle),
             ms.Button("Load",image_data=load,size=(5,1), font=fstyle, key="load simg"), ms.Sizer(2, 0),
             ],
            [ms.Text("Nominee Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e23', font=fstyle)],
            [ms.Text("Nominee Phone No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e24', font=fstyle)],
            [ms.Text("Nominee photo:", justification='left', size=(20, 1), font=fstyle),
             ms.Input("", size=(19, 1), do_not_clear=True, key='e25', font=fstyle),
             ms.FileBrowse(file_types=file_types,size=(6,1),enable_events=True, target="e25",key="b3", font=fstyle),
             ms.Button("Load",image_data=load,size=(5,1), font=fstyle, key="load nimg"), ms.Sizer(2, 0),
             ],
            [ms.Text("ET :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Radio("PF","etype", size=(5, 1),enable_events=True, key='e26', font=fstyle),
             ms.Radio("Non PF","etype", size=(5, 1),enable_events=True, key='e26', font=fstyle)
             ],
        ]
        Employee_Image = [[ms.Image(key="-IMAGE-")]]
        Signature_Image = [[ms.Image(key="-IMAGE2-")]]
        Nominee_Image = [[ms.Image(key="-IMAGE3-")]]
        Employee_Add_GUI = [[
            ms.Column([[ms.Frame("Employee Details", Employee_Details, font=fstyle)]]),
            ms.Column([
                [ms.Frame("Employee Photo", Employee_Image,size=(170,200), font=fstyle)],
                [ms.Frame("Signature", Signature_Image,size=(170,100), font=fstyle)],
                [ms.Frame(" Nominee Photo", Nominee_Image,size=(170,200), font=fstyle)]])],
            [ms.Button("Add", key="add employee", font=fstyle)]]

        return Employee_Add_GUI

    def Add_Employee(event, values):


        if event == "add employee":
            for i in range(1, 15):
                chk=True
                if values['e' + str(i)] == "":
                    chk = False
                    break
            if chk == True:
                filename = str(values['e21'])
                file = open(filename, 'rb').read()
                image_data_ep = base64.b64encode(file)
                filename = str(values['e22'])
                file = open(filename, 'rb').read()
                image_data_sp = base64.b64encode(file)
                filename = str(values['e25'])
                file = open(filename, 'rb').read()
                image_data_np = base64.b64encode(file)

                dict = {'employee_name': values['e1'], 'emp_code': values['e2'],'esic_no':values['e3'],'uan_no':values['e4'],
                        'aadhar_no': values['e5'],'address': values['e6'], 'f_sp_name': values['e7'],
                        'gender': values['e8'],'shift_work': values['e9'],'base_salary': values['e10'],
                        'shift_1_salary': values['e11'],'shift_2_salary': values['e12'],'shift_3_salary': values['e13'],
                        'phone_no': values['e14'],
                        'bank_account_no': values['e15'], 'bank_name': values['e16'], 'ifsc_code': values['e17'],
                        'branch': values['e18'],'date_of_birth': values['e19'], 'date_of_join': values['e20'],
                        'photo': image_data_ep,'signature': image_data_sp, 'nominee_name': values['e23'],
                        'nominee_phone_no': values['e24'],'nominee_photo':image_data_np,'ET': values['e26']}

                print(dict)
                placeholders = ', '.join(['%s'] * len(dict))
                columns = ', '.join(dict.keys())
                sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('register',
                                                               columns, placeholders)
                mycursor.execute(sql, list(dict.values()))
                mydb.commit()

                ms.PopupTimed("Added",
                              title='Employee Added',
                              button_type=0,
                              auto_close=True,
                              auto_close_duration=1)
                Menu.close()

            else:
                ms.popup("Enter valid info..!")

    def Employee_update_GUI():
        Employee_Details = [

            [ms.Text("Employee Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u2', font=fstyle)],
            [ms.Text("Emp Code:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u3', font=fstyle),
             ms.Button("Fetch", key="fetch", font=fstyle), ],
            [ms.Text("Aadhar No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u4', font=fstyle)],
            [ms.Text("Address:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u5', font=fstyle)],
            [ms.Text("Father/Spouse Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u6', font=fstyle)],
            [ms.Text("Gender:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Combo(('M', 'F', 'O'), size=(30, 1), key='u7', font=fstyle)],
            [ms.Text("Base salary:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u8', font=fstyle)],
            [ms.Text("Phone No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u9', font=fstyle)],
            [ms.Text("Bank Account Number:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u10', font=fstyle)],
            [ms.Text("Bank Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u11', font=fstyle)],
            [ms.Text("IFSC Code:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u12', font=fstyle)],
            [ms.Text("Branch:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u13', font=fstyle)],
            [ms.Text("Date of Birth :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u14', font=fstyle),
             ms.CalendarButton('Choose', format='%d_%m_%y', target='u14', size=(5, 1), key='date1'), ],
            [ms.Text("Date of Joining :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u15', font=fstyle),
             ms.CalendarButton('Choose', format='%d_%m_%y', target='u15', size=(5, 1), key='date1'), ],
            [ms.Text("photo:", justification='left', size=(20, 1), font=fstyle),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u16', font=fstyle),
             ms.FileBrowse(file_types=file_types, target="e16", font=fstyle),
             ms.Button("Load", font=fstyle, key="load pimg"), ms.Sizer(2, 0),
             ],
            [ms.Text("Specimen Signature:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u17', font=fstyle),
             ms.FileBrowse(file_types=file_types, target="e17", font=fstyle),
             ms.Button("Load", font=fstyle, key="load simg"), ms.Sizer(2, 0)
             ],
            [ms.Text("Nominee Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u18', font=fstyle)],
            [ms.Text("Nominee Phone No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u19', font=fstyle)],
            [ms.Text("ET :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='u20', font=fstyle)],
            [ms.Text("Active:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Combo(("Y", "N"), size=(30, 1), key='u20', font=fstyle)],

            [ms.Button("", key="add employee", font=fstyle)],
        ]
        Employee_Image = [[ms.Image(key="-IMAGE-")]]
        Signature_Image = [[ms.Image(key="-IMAGE2-")]]
        Employee_Update_GUI = [
            [ms.Frame("Employee Details", Employee_Details, font=fstyle)],
            ([ms.Frame("Photo Preview", Employee_Image, font=fstyle),
              ms.Frame("Photo Preview", Signature_Image, font=fstyle),
              ms.Frame("Photo Preview", Signature_Image, font=fstyle)])]
        return Employee_Update_GUI
    def Emp_code_Gen(type):
        if type=="PF":
            mycursor.execute("SELECT emp_code FROM register WHERE emp_code LIKE 'SIL'")

            return  str("SIL" + str((int("0" if (mycursor.fetchall())==None else str(len(mycursor.fetchall()))) + 1)).zfill(3))
        if type=="Non PF":
            mycursor.execute("SELECT emp_code FROM register WHERE emp_code LIKE 'SILTEMP'")
            return "SILTEMP" + str((int("0" if (mycursor.fetchall())==None else str(len(mycursor.fetchall()))) + 1)).zfill(3)

    print(Emp_code_Gen("PF"))



    if event == 'empadd':
        Menu = ms.Window("Add Employee", [[ms.Column(Employee_Add_GUI(),scrollable=True,size=(760,700), element_justification='centre')]])
        while True:
            event, values = Menu.read()
            if event == ms.WIN_CLOSED:
                Menu.close()
                break
            if event == 'add employee':
                Add_Employee(event, values)
            if event == "b1":
                print("hii")
                filename = str(values["b1"])
                file = open(filename, 'rb').read()
                image_data = base64.b64encode(file)
                print(image_data)
                Menu["e21"].update(value=image_data)
            if event == "b2":
                filename = str(values["b2"])
                file = open(filename, 'rb').read()
                image_data = base64.b64encode(file)
                Menu["e22"].update(value=image_data)
            if event == "b3":
                filename = str(values["b3"])
                file = open(filename, 'rb').read()
                image_data = base64.b64encode(file)
                Menu["e25"].update(value=image_data)

            if event == "load pimg":
                filename = values["e21"]
                if os.path.exists(filename):
                    image = Image.open(values["e21"])
                    image.thumbnail((300, 300))
                    bio = io.BytesIO()
                    # Actually store the image in memory in binary
                    image.save(bio, format="PNG")
                    # Use that image data in order to
                    Menu["-IMAGE-"].update(data=bio.getvalue())

            if event == "load simg":
                filename = values["e22"]
                if os.path.exists(filename):
                    image = Image.open(values["e22"])
                    image.thumbnail((300, 300))
                    bio = io.BytesIO()
                    # Actually store the image in memory in binary
                    image.save(bio, format="PNG")
                    # Use that image data in order to
                    Menu["-IMAGE2-"].update(data=bio.getvalue())
            if event == "load nimg":
                filename = values["e25"]
                if os.path.exists(filename):
                    image = Image.open(values["e25"])
                    image.thumbnail((300, 300))
                    bio = io.BytesIO()
                    # Actually store the image in memory in binary
                    image.save(bio, format="PNG")
                    # Use that image data in order to
                    Menu["-IMAGE3-"].update(data=bio.getvalue())
            if event=="PF":
                eMenu["e2"].update(values=Emp_code_Gen("PF"))
            if event =="Non PF":
                eMenu["e2"].update(values=Emp_code_Gen("Non PF"))

    if event == "emp_data":
        data = Menu['emp_data'].get()
        crow = [data[row] for row in values[event]]

    if event == "Remove ":
        chk = ms.popup_ok("Please Confirm to Delete", font=fstyle)
        if chk == "OK":
            mycursor.execute("UPDATE `register` SET `active_status` = 'N' WHERE (`emp_code` = '%s')" % crow[0][0])
            mydb.commit()
            Menu['emp_data'].update(values=EmpdataFetch())
