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


def RegisterFn(Menu,event,values):

    def Employee_Add_GUI():
        Employee_Details = [
            [ms.Text("Employee Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e2', font=fstyle)],
            [ms.Text("Emp Code:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e3', font=fstyle),
             ms.Button("Fetch", key="fetch", font=fstyle), ],
            [ms.Text("Aadhar No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e4', font=fstyle)],
            [ms.Text("Address:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e5', font=fstyle)],
            [ms.Text("Father/Spouse Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e6', font=fstyle)],
            [ms.Text("Gender:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Combo(('M', 'F', 'O'), size=(30, 1), key='e7', font=fstyle)],
            [ms.Text("Base salary:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e8', font=fstyle)],
            [ms.Text("Phone No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e9', font=fstyle)],
            [ms.Text("Bank Account Number:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e10', font=fstyle)],
            [ms.Text("Bank Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e11', font=fstyle)],
            [ms.Text("IFSC Code:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e12', font=fstyle)],
            [ms.Text("Branch:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e13', font=fstyle)],
            [ms.Text("Date of Birth :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e14', font=fstyle),
             ms.CalendarButton('Choose', format='%d_%m_%y', target='e14', font=fstyle, size=(6, 1), key='date1'), ],
            [ms.Text("Date of Joining :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e15', font=fstyle),
             ms.CalendarButton('Choose', format='%d_%m_%y', font=fstyle, target='e15', size=(6, 1), key='date1'), ],
            [ms.Text("photo:", justification='left', size=(20, 1), font=fstyle),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e16', font=fstyle),
             ms.FileBrowse(file_types=file_types, target="e16", font=fstyle),
             ms.Button("Load", font=fstyle, key="load pimg"), ms.Sizer(2, 0),
             ],
            [ms.Text("Specimen Signature:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e17', font=fstyle),
             ms.FileBrowse(file_types=file_types, target="e17", font=fstyle),
             ms.Button("Load", font=fstyle, key="load simg"), ms.Sizer(2, 0),
             ],
            [ms.Text("Nominee Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e18', font=fstyle)],
            [ms.Text("Nominee Phone No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e19', font=fstyle)],
            [ms.Text("ET :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), do_not_clear=True, key='e20', font=fstyle)],
        ]
        Employee_Imgae = [[ms.Image(key="-IMAGE-")]]
        Signature_Image = [[ms.Image(key="-IMAGE2-")]]
        Employee_Add_GUI = [[
            ms.Column([[ms.Frame("Employee Details", Employee_Details, font=fstyle)]]),
            ms.Column([
                [ms.Frame("Photo Preview", Employee_Imgae, font=fstyle)],
                [ms.Frame("Photo Preview", Signature_Image, font=fstyle)]])],
            [ms.Button("Add", key="add employee", font=fstyle)]]
    
        return Employee_Add_GUI


    def Add_Employee(event, values):
        if event == "load pimg":
            filename = values["e16"]
            if os.path.exists(filename):
                image = Image.open(values["e16"])
                image.thumbnail((300, 300))
                bio = io.BytesIO()
                # Actually store the image in memory in binary
                image.save(bio, format="PNG")
                # Use that image data in order to
                Menu["-IMAGE-"].update(data=bio.getvalue())

        if event == "load simg":
            filename = values["e17"]
            if os.path.exists(filename):
                image = Image.open(values["e17"])
                image.thumbnail((300, 300))
                bio = io.BytesIO()
                # Actually store the image in memory in binary
                image.save(bio, format="PNG")
                # Use that image data in order to
                Menu["-IMAGE2-"].update(data=bio.getvalue())

        if event == "add employee":
            if values['e2'] and values['e3'] and values['e4'] and values['e5'] and values['e9'] and values['e6'] and \
                    values['e7'] and values['e8'] and values['e10'] and values['e11'] and values['e12'] \
                    and values['e13'] and values['e14'] and values['e15'] and values['e16'] and values['e17'] \
                    and values['e18'] and values['e19'] and values['e20'] != "":
                dict = {'employee_name': values['e2'], 'emp_code': values['e3'], 'aadhar_no': values['e4'],
                        'address': values['e5'],
                        'f_sp_name': values['e6'], 'gender': values['e7'], 'base_salary': values['e8'],
                        'phone_no': values['e9'],
                        'bank_account_no': values['e10'], 'bank_name': values['e11'], 'ifsc_code': values['e12'],
                        'branch': values['e13'],
                        'date_of_birth': values['e14'], 'date_of_join': values['e15'], 'photo': values['e16'],
                        'signature': values['e17'], 'nominee_name': values['e18'], 'nominee_phone_no': values['e19'],
                        'ET': values['e20']}
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
        Employee_Imgae = [[ms.Image(key="-IMAGE-")]]
        Signature_Image = [[ms.Image(key="-IMAGE2-")]]
        Employee_Update_GUI = [
            [ms.Frame("Employee Details", Employee_Details, font=fstyle)],
            ([ms.Frame("Photo Preview", Employee_Imgae, font=fstyle),
              ms.Frame("Photo Preview", Signature_Image, font=fstyle)])]
        return Employee_Update_GUI

    if event == 'empadd':
        Menu = ms.Window("Add Employee", Employee_Add_GUI(), element_justification='centre')
        while True:
            event, values = Menu.read()
            if event == ms.WIN_CLOSED:
                Menu.close()
                break
            if event == 'add employee':
                Add_Employee(event,values)

    if event == "emp_data":
        data = Menu['emp_data'].get()
        crow = [data[row] for row in values[event]]

    if event == "Remove ":
            chk=ms.popup_ok("Please Confirm to Delete",font=fstyle)
            if chk == "OK":
                mycursor.execute("UPDATE `register` SET `active_status` = 'N' WHERE (`emp_code` = '%s')"%crow[0][0])
                mydb.commit()
                Menu['emp_data'].update(values=EmpdataFetch())
