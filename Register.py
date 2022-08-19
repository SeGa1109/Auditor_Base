from Env import *


def RegsiterLay():
    layout = [[ms.Text("Employee Register", font=fstylehd)],
              [ms.Sizer(swi - 200, 0),
               ms.Button("Export", font=fstyle, key='empexp'),
               ms.Button("Add", font=fstyle, key='empadd')],

              [ms.Frame("Employee Data",
                        [[ms.Table(values=EmpdataFetch("PF"),
                                   headings=["Employee Code", "Name", "Father/Spouse Name", "Gender", "Phone No.",
                                             "Base Salary"],
                                   justification='centre', enable_events=True, auto_size_columns=False, row_height=30,
                                   col_widths=[15, 40, 40, 10, 20, 15],
                                   right_click_selects=True,
                                   right_click_menu=[[], ["Update Employee", "Remove"]],
                                   enable_click_events=True, size=(swi - 70, shi - 120), key="emp_data", font=fstyle)]],
                        font=fstyle, size=(swi - 50, shi - 180), element_justification='center')],
              [ms.Button("Cleaning Crew", font=fstyle, key='ccwin'),ms.Sizer(swi-300,0),ms.Checkbox("Non PF",key="etcnge",enable_events=True,default=False,)]]

    return layout


def RegisterFn(Menu, event, values):
    def Cleaning_Crew_GUI():
        layout = [[ms.Text("Cleaning Crew Register", font=fstylehd)],
                  [ms.Sizer(swi - 900, 0),
                   ms.Button("Add", font=fstyle, key='ccwadd')],

                  [ms.Frame("Cleaning Crew Data",
                            [[ms.Table(values=CCWFetch(),
                                       headings=["UID", "Name", "Phone No","Pan No","Bank Account No"],
                                       justification='centre', enable_events=True, auto_size_columns=False,
                                       row_height=30,
                                       col_widths=[10, 20, 20,20,20],
                                       right_click_selects=True,
                                       right_click_menu=[[], ["Remove"]],
                                       enable_click_events=True, size=(swi - 100, shi - 300), key="ccw_data",
                                       font=fstyle)]],
                            font=fstyle, size=(swi - 585, shi - 300), element_justification='center')],
                  [ms.Frame("Adding Crew",[[ms.Text("Name",size=(20,1)),ms.Sizer(45,0),ms.Text("Phone No",size=(20,1)),ms.Sizer(40,0),
                                            ms.Text("Pan No",size=(20,1)),ms.Sizer(40,0),ms.Text("Bank Account No",size=(20,1))],
                                           [ms.Input("", size=(20, 1), do_not_clear=False, key='c_name', font=fstyle),ms.Sizer(5,0),
                                            ms.Input("", size=(20, 1), do_not_clear=False, key='c_ph.no', font=fstyle),
                                            ms.Input("", size=(20, 1), do_not_clear=False,key='c_pan.no', font=fstyle),
                                            ms.Input("", size=(20, 1), do_not_clear=False,key='c_bkac.no', font=fstyle),
                                            ms.Button("Add",font=fstyle,key="add_crow")]],visible=False,key="add_frame")]]
        return layout

    def Employee_Add_GUI():
        Employee_Details = [
            [ms.Text("Employee Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e1', font=fstyle)],
            [ms.Text("Emp Code:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(Emp_code_Gen("PF"), size=(30, 1),disabled=True, enable_events=True,do_not_clear=True, key='e2', font=fstyle)],
            [ms.Text("Designation:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Combo(("Worker","Supervisor","Manager"),enable_events=True, size=(29, 1), key='e3', font=fstyle)],
            [ms.Text("ESIC NO:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e4', font=fstyle)],
            [ms.Text("UAN NO:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e5', font=fstyle)],
            [ms.Text("Pan No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e6', font=fstyle)],
            [ms.Text("Aadhar No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e7', font=fstyle)],
            [ms.Text("Address:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Multiline("", size=(28, 3), enable_events=True,do_not_clear=True, key='e8', font=fstyle)],
            [ms.Text("Married Status:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Radio("Yes", "ms", size=(5, 1), enable_events=True, key='m_yes', font=fstyle),
             ms.Radio("No", "ms", size=(5, 1), enable_events=True, key='m_no', font=fstyle)],
            [ms.Text("Father/Spouse Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e9', font=fstyle)],
            [ms.Text("Gender:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Radio("M","gender", size=(5, 1), key='m', font=fstyle),
             ms.Radio("F","gender", size=(5, 1), key='f', font=fstyle),
             ms.Radio("O","gender", size=(5, 1), key='o', font=fstyle)],
            [ms.Text("Shift Work:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Radio("Yes","sw", size=(5, 1),enable_events=True, key='yes', font=fstyle),
             ms.Radio("No","sw", size=(5, 1),enable_events=True, key='no', font=fstyle)],
            [ms.Text("Base salary:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("0.00", size=(30, 1),disabled=True, enable_events=True,do_not_clear=True, key='e10', font=fstyle)],
            [ms.Text("Shift  salary:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("0.00", size=(9, 1),tooltip="shift 1 salary",disabled=True, enable_events=True,do_not_clear=True, key='e11', font=fstyle),
             ms.Input("0.00", size=(9, 1),tooltip="shift 2 salary",disabled=True, enable_events=True,do_not_clear=True, key='e12', font=fstyle),
             ms.Input("0.00", size=(9, 1),tooltip="shift 3 salary",disabled=True, enable_events=True,do_not_clear=True, key='e13', font=fstyle)],
            [ms.Text("Phone No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e14', font=fstyle)],
            [ms.Text("Blood Group:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Combo(("O+","O-","A+"),enable_events=True, size=(30, 1), key='e15', font=fstyle)],
            [ms.Text("Bank Account Number:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e16', font=fstyle)],
            [ms.Text("Bank Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e17', font=fstyle)],
            [ms.Text("IFSC Code:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e18', font=fstyle)],
            [ms.Text("Branch:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e19', font=fstyle)],
            [ms.Text("Date of Birth :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(26, 1), enable_events=True,do_not_clear=True, key='e20', font=fstyle),ms.Sizer(4, 0),
             ms.CalendarButton('Choose',image_data=chse, format='%d-%m-%y', target='e20', font=fstyle, size=(6, 1), key='date1'), ],
            [ms.Text("Date of Joining :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(26, 1), enable_events=True,do_not_clear=True, key='e21', font=fstyle),ms.Sizer(4, 0),
             ms.CalendarButton('Choose',image_data=chse, format='%d-%m-%y', font=fstyle, target='e21', size=(6, 1), key='date1'), ],
            [ms.Text("photo:", justification='left', size=(20, 1), font=fstyle),
             ms.Input("", size=(19, 1), enable_events=True,do_not_clear=True, key='e22', font=fstyle),
             ms.FileBrowse(file_types=file_types,size=(6,1),enable_events=True, target="e22",key="b1", font=fstyle),
             ms.Button("Load",image_data=load, font=fstyle,size=(5,1), key="load pimg"), ms.Sizer(2, 0),
             ],
            [ms.Text("Specimen Signature:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(19, 1), enable_events=True,do_not_clear=True, key='e23', font=fstyle),
             ms.FileBrowse(file_types=file_types,size=(6,1),enable_events=True, target="e23",key="b2", font=fstyle),
             ms.Button("Load",image_data=load,size=(5,1), font=fstyle, key="load simg"), ms.Sizer(2, 0),
             ],
            [ms.Text("Nominee Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e24', font=fstyle)],
            [ms.Text("Nominee Phone No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input("", size=(30, 1), enable_events=True,do_not_clear=True, key='e25', font=fstyle)],
            [ms.Text("Nominee photo:", justification='left', size=(20, 1), font=fstyle),
             ms.Input("", size=(19, 1), enable_events=True,do_not_clear=True, key='e26', font=fstyle),
             ms.FileBrowse(file_types=file_types,size=(6,1),enable_events=True, target="e26",key="b3", font=fstyle),
             ms.Button("Load",image_data=load,size=(5,1), font=fstyle, key="load nimg"), ms.Sizer(2, 0),
             ],
            [ms.Text("ET :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Radio("PF","etype", size=(5, 1),enable_events=True, key='pf', font=fstyle),
             ms.Radio("Non PF","etype", size=(6, 1),enable_events=True, key='non pf', font=fstyle)
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
            for i in range(1,27):
                chk=True
                if values['e' + str(i)] == "":
                    chk = False
                    break
            if chk == True:
                filename = str(values['e22'])
                file = open(filename, 'rb').read()
                image_data_ep = base64.b64encode(file)
                filename = str(values['e23'])
                file = open(filename, 'rb').read()
                image_data_sp = base64.b64encode(file)
                filename = str(values['e26'])
                file = open(filename, 'rb').read()
                image_data_np = base64.b64encode(file)
                print( )

                dict = {'employee_name': values['e1'], 'emp_code': values['e2'],'designation':values['e3'],'esic_no':values['e4'],'uan_no':values['e5'],'pan_no': values['e6'],
                        'aadhar_no': values['e7'],'address': values['e8'],'marriage_status':"Yes" if values["m_yes"]==True else "No", 'f_sp_name': values['e9'],
                        'gender':"M" if values['m']==True else "F" if values['f']==True else "O" ,
                        'shift_work':"Yes" if values["yes"]==True else "No",'base_salary': values['e10'],
                        'shift_1_salary': values['e11'],'shift_2_salary': values['e12'],'shift_3_salary': values['e13'],
                        'phone_no': values['e14'],'blood_group': values['e15'],'bank_account_no': values['e16'], 'bank_name': values['e17'],
                        'ifsc_code': values['e18'],'branch': values['e19'],'date_of_birth': values['e20'],
                        'date_of_join': values['e21'],'photo': image_data_ep,'signature': image_data_sp,
                        'nominee_name': values['e24'],'nominee_phone_no': values['e25'],'nominee_photo':image_data_np,
                        'ET':"PF" if values['pf']==True else "Non PF"}

                placeholders = ', '.join(['%s'] * len(dict))
                columns = ', '.join(dict.keys())
                sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('register',
                                                               columns, placeholders)
                mycursor.execute(sql, list(dict.values()))
                mydb.commit()

                ms.PopupTimed("Successfully Added",
                              title='Employee Added',
                              button_type=0,
                              auto_close=True,
                              auto_close_duration=1)
                eMenu.close()

            else:
                ms.popup("Enter valid info..!")

    def Employee_update_GUI(epc):
        mycursor.execute("select * from register where emp_code='%s'" % epc)
        ep_dat= list(mycursor.fetchall())
        ep_data=ep_dat[0]
        print("ep_data",ep_data)
        if ep_data[9]=="M":
            g_val=[True,False,False]
        elif ep_data[9]=="F":
            g_val=[False,True,False]
        else :
            g_val=[False,False,True]
        if ep_data[10]=="Yes":
            s_val=[True,False]
        else:
            s_val=[False,True]
        if ep_data[28]=="PF":
            et_val=[True,False]
        elif ep_data[28]=="Non PF":
            et_val=[False,True]

        Employee_Details = [
            [ms.Text("Employee Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[1], size=(30, 1), do_not_clear=True, key='u1', font=fstyle)],
            [ms.Text("Emp Code:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[2], size=(30, 1),disabled=True, do_not_clear=True, key='u2', font=fstyle)],
            [ms.Text("Designation:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Combo(("Worker","Supervisor","Manager"),default_value =ep_data[3], size=(29, 1), key='u3', font=fstyle)],
            [ms.Text("ESIC NO:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[4], size=(30, 1), do_not_clear=True, key='u4', font=fstyle)],
            [ms.Text("UAN NO:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[5], size=(30, 1), do_not_clear=True, key='u5', font=fstyle)],
            [ms.Text("Aadhar No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[6], size=(30, 1), do_not_clear=True, key='u6', font=fstyle)],
            [ms.Text("Address:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Multiline(ep_data[7], size=(28, 3), do_not_clear=True, key='u7', font=fstyle)],
            [ms.Text("Father/Spouse Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[8], size=(30, 1), do_not_clear=True, key='u8', font=fstyle)],
            [ms.Text("Gender:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Radio("M","gender", size=(5, 1),default=g_val[0], key='u9', font=fstyle),
             ms.Radio("F","gender", size=(5, 1),default=g_val[1], key='u10', font=fstyle),
             ms.Radio("O","gender", size=(5, 1),default=g_val[2], key='u11', font=fstyle)],
            [ms.Text("Shift Work:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Radio("Yes","sw",default=s_val[0], size=(5, 1), key='u12', font=fstyle),
             ms.Radio("No","sw",default=s_val[1], size=(5, 1), key='u13', font=fstyle)],
            [ms.Text("Base salary:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[11], size=(30, 1),disabled=True, do_not_clear=True, key='u14', font=fstyle)],
            [ms.Text("Shift  salary:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[12], size=(9, 1),tooltip="shift 1 salary",disabled=True, do_not_clear=True, key='u15', font=fstyle),
             ms.Input(ep_data[13], size=(9, 1),tooltip="shift 2 salary",disabled=True, do_not_clear=True, key='u16', font=fstyle),
             ms.Input(ep_data[14], size=(9, 1),tooltip="shift 3 salary",disabled=True, do_not_clear=True, key='u17', font=fstyle)],

            [ms.Text("Phone No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[15], size=(30, 1), do_not_clear=True, key='u18', font=fstyle)],
            [ms.Text("Bank Account Number:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[16], size=(30, 1), do_not_clear=True, key='u19', font=fstyle)],
            [ms.Text("Bank Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[17], size=(30, 1), do_not_clear=True, key='u20', font=fstyle)],
            [ms.Text("IFSC Code:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[18], size=(30, 1), do_not_clear=True, key='u21', font=fstyle)],
            [ms.Text("Branch:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[19], size=(30, 1), do_not_clear=True, key='u22', font=fstyle)],
            [ms.Text("Date of Birth :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[20], size=(26, 1), do_not_clear=True, key='u23', font=fstyle),ms.Sizer(4, 0),
             ms.CalendarButton('Choose',image_data=chse, format='%d-%m-%y', target='e23', font=fstyle, size=(6, 1), key='date1'), ],
            [ms.Text("Date of Joining :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[21], size=(26, 1), do_not_clear=True, key='u24', font=fstyle),ms.Sizer(4, 0),
             ms.CalendarButton('Choose',image_data=chse, format='%d-%m-%y', font=fstyle, target='e24', size=(6, 1), key='date2'), ],
            [ms.Text("photo:", justification='left', size=(20, 1), font=fstyle),
             ms.Input(" ", size=(19, 1), do_not_clear=True, key='u25', font=fstyle),
             ms.FileBrowse(file_types=file_types,size=(6,1),enable_events=True, target="u25",key="b1", font=fstyle),
             ms.Button("Load",image_data=load, font=fstyle,size=(5,1), key="load pimg"), ms.Sizer(2, 0),
             ],
            [ms.Text("Specimen Signature:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(" ", size=(19, 1), do_not_clear=True, key='u26', font=fstyle),
             ms.FileBrowse(file_types=file_types,size=(6,1),enable_events=True, target="u26",key="b2", font=fstyle),
             ms.Button("Load",image_data=load,size=(5,1), font=fstyle, key="load simg"), ms.Sizer(2, 0),
             ],
            [ms.Text("Nominee Name:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[25], size=(30, 1), do_not_clear=True, key='u27', font=fstyle)],
            [ms.Text("Nominee Phone No:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[26], size=(30, 1), do_not_clear=True, key='u28', font=fstyle)],
            [ms.Text("Nominee photo:", justification='left', size=(20, 1), font=fstyle),
             ms.Input("", size=(19, 1), do_not_clear=True, key='u29', font=fstyle),
             ms.FileBrowse(file_types=file_types,size=(6,1),enable_events=True, target="u29",key="b3", font=fstyle),
             ms.Button("Load",image_data=load,size=(5,1), font=fstyle, key="load nimg"), ms.Sizer(2, 0),
             ],
            [ms.Text("ET :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Radio("PF","etype",default=et_val[0], size=(5, 1),enable_events=True, key='u30', font=fstyle),
             ms.Radio("Non PF","etype",default=et_val[1], size=(5, 1),enable_events=True, key='u31', font=fstyle)
             ],

            [ms.Text("Active:", justification='left', size=(20, 1), font=fstyle, ),
             ms.Combo(("Y","N"),default_value=ep_data[29], size=(30, 1),enable_events=True, key='u32', font=fstyle)],
            [ms.Text("Date of Exit :", justification='left', size=(20, 1), font=fstyle, ),
             ms.Input(ep_data[22], size=(26, 1),disabled=True, do_not_clear=True, key='u33', font=fstyle), ms.Sizer(4, 0),
             ms.CalendarButton('Choose', image_data=chse, format='%d-%m-%y', target='u33', font=fstyle, size=(6, 1),
                               key='date3',disabled=True), ],

        ]
        #Employee_Image = [[ms.Image(ep_data[23],key="-IMAGE-")]]
       # Signature_Image = [[ms.Image(ep_data[24],key="-IMAGE2-")]]
        #Nominee_Image = [[ms.Image(ep_data[27],key="-IMAGE3-")]]
        Employee_Update_GUI = [[
            ms.Column([[ms.Frame("Employee Details", Employee_Details, font=fstyle)]]),
            ms.Column([
                [ms.Frame("Employee Photo", [[]] ,size=(170, 200), font=fstyle)],
                [ms.Frame("Signature",  [[]],size=(170, 100), font=fstyle)],
                [ms.Frame(" Nominee Photo", [[]], size=(170, 200), font=fstyle)]])],
            [ms.Button("",[[]], key="update employee", font=fstyle)]]
        return Employee_Update_GUI

    def Update_Employee(event, values):
        if event == "update employee":
            for i in range(1, 25):
                chk=True
                if values['u' + str(i)] == "":
                    chk = False
                    break
            if chk == True:
                filename = str(values['u25'])
                file = open(filename, 'rb').read()
                image_data_ep = base64.b64encode(file)
                filename = str(values['u26'])
                file = open(filename, 'rb').read()
                image_data_sp = base64.b64encode(file)
                filename = str(values['u29'])
                file = open(filename, 'rb').read()
                image_data_np = base64.b64encode(file)

                dict = {'employee_name': values['u1'],'designation':values['u3'],'esic_no':values['u4'],'uan_no':values['u5'],
                        'aadhar_no': values['u6'],'address': values['u7'], 'f_sp_name': values['u8'],
                        'gender':"M" if values['u9']==True else "F" if values['u10']==True else "O" ,
                        'shift_work':Yes if values["u12"]==True else "No",'base_salary': values['u14'],
                        'shift_1_salary': values['u15'],'shift_2_salary': values['u16'],'shift_3_salary': values['u17'],
                        'phone_no': values['u18'],'bank_account_no': values['u19'], 'bank_name': values['u20'],
                        'ifsc_code': values['u21'],'branch': values['u22'],'date_of_birth': values['u23'],
                        'date_of_join': values['u24'],'photo': image_data_ep,'signature': image_data_sp,
                        'nominee_name': values['u27'],'nominee_phone_no': values['u28'],'nominee_photo':image_data_np,
                        'ET':"PF" if values['u30']==True else "Non PF"}

                c_name=list(dict.keys())
                c_data=list(dict.values())
                for i in range(0,29):
                    print(c_data[i])
                    sql='UPDATE `twink_06ma`.`register` SET `%s` = "%s" WHERE (`emp_code` = "%s");' %(c_name[i],c_data[i],values['u2'] )
                    mycursor.execute(sql)

                mydb.commit()

                ms.PopupTimed("Successfully updated",
                              title='Employee Added',
                              button_type=0,
                              auto_close=True,
                              auto_close_duration=1)
                if values["etcnge"]==True:
                    Menu["emp_data"].update(values=EmpdataFetch("Non PF"))
                if values["etcnge"] == False:
                    Menu["emp_data"].update(values=EmpdataFetch("PF"))
                uMenu.close()

            else:
                ms.popup("Enter valid info..!")

    def Emp_code_Gen(type):
        if type=="PF":
            mycursor.execute("SELECT emp_code FROM register WHERE emp_code LIKE 'SIL0%'")
            db_data=mycursor.fetchall()
            #print(mycursor.fetchall())
            return  str("SIL" + str((int("0" if (db_data)==None else (len(db_data))) + 1)).zfill(3))
        if type=="Non PF":
            mycursor.execute("SELECT emp_code FROM register WHERE emp_code LIKE 'SILTEMP%'")
            db_data=mycursor.fetchall()
            return "SILTEMP" + str((int("0" if (db_data)==None else str(len(db_data))) + 1)).zfill(3)

    print(Emp_code_Gen("PF"))

    if event =="ccwin":
        ccwMenu = ms.Window("Add Crow", [[ms.Column(Cleaning_Crew_GUI(), scrollable=True, size=(960, 700), element_justification='centre')]])
        while True:
            event, values = ccwMenu.read()
            if event == ms.WIN_CLOSED:
                ccwMenu.close()
                break
            if event =="ccwadd":
                ccwMenu["add_frame"].update(visible=True)
            if event =="add_crow":
                sql ="INSERT INTO cleaning_crow ( crow_name,phone_no,pan_no,bank_account ) VALUES ( '%s','%s','%s','%s' )" % (values['c_name'],values['c_ph.no'],values['c_pan.no'],values['c_bkac.no'])
                mycursor.execute(sql)
                mydb.commit()
                ccwMenu['ccw_data'].update(values=CCWFetch())
                ccwMenu["add_frame"].update(visible=False)
            if event == "ccw_data":
                data = ccwMenu['ccw_data'].get()
                globals()['crow1'] = [data[row] for row in values[event]]
            if event =="Remove":
                chk = ms.popup_ok("Please Confirm to Delete", font=fstyle)
                if chk == "OK":
                    mycursor.execute("DELETE FROM `twink_06ma`.`cleaning_crew` WHERE (`UID` = %d);" % int(crow1[0][0]))
                    mydb.commit()
                    ccwMenu['ccw_data'].update(values=CCWFetch())
            if event =='c_ph.no':
                if len(values['c_ph.no']) > 10:
                    ccwMenu['c_ph.no'].update(background_color ="red")
                else:
                    ccwMenu['c_ph.no'].update(background_color=ms.DEFAULT_INPUT_ELEMENTS_COLOR)

    if event == 'empadd':
        eMenu = ms.Window("Add Employee", [[ms.Column(Employee_Add_GUI(),scrollable=True,size=(760,700), element_justification='centre')]], finalize=True)
        while True:
            event, values = eMenu.read()
            if event == ms.WIN_CLOSED:
                eMenu.close()
                break

            if event == 'add employee':
                Add_Employee(event, values)
                if values["pf"]==True:
                    Menu["emp_data"].update(values=EmpdataFetch("PF"))
                if values["non pf"] == True:
                    Menu["emp_data"].update(values=EmpdataFetch("Non PF"))
                    Menu["etcnge"].update(value=True)

            if event == "load pimg":
                filename = values["e20"]
                if os.path.exists(filename):
                    image = Image.open(values["e20"])
                    image.thumbnail((300, 300))
                    bio = io.BytesIO()
                    # Actually store the image in memory in binary
                    image.save(bio, format="PNG")
                    # Use that image data in order to
                    eMenu["-IMAGE-"].update(data=bio.getvalue())

            if event =="e1":
                if values[event]!="":
                    border(eMenu[event],"green")
                else:
                    border(eMenu[event], "red")

            if event =="e3":
                if values[event]!="":
                    border(eMenu[event],"green")
                else:
                    border(eMenu[event], "red")
            if event =="e4":
                if values[event]!="":
                    if values[event] is int and len(values[event])==10:
                        border(eMenu[event], "green")
                    if len(values[event])>10:
                        border(eMenu[event], "red")
                    else:
                        border(eMenu[event], "red")
            if event =="e5":
                if values[event]!="":
                    if values[event] is int and len(values[event])==10:
                        border(eMenu[event], "green")
                    if len(values[event])>10:
                        border(eMenu[event], "red")
                    else:
                        border(eMenu[event], "red")
            if event =="e6":
                if values[event]!="":
                    if values[event].isalnum()==True and len(values[event])==10:
                        border(eMenu[event], "green")
                    if len(values[event])>10:
                        border(eMenu[event], "red")
                    else:
                        border(eMenu[event], "red")
            if event =="e7":
                if values[event]!="":
                    if values[event] is int and len(values[event])==12:
                        border(eMenu[event], "green")
                    if len(values[event])>12:
                        border(eMenu[event], "red")
                    else:
                        border(eMenu[event], "red")
            if event =="e8":
                if values[event]!="":
                    border(eMenu[event],"green")
                else:
                    border(eMenu[event], "red")
            if event =="e9":
                if values[event]!="":
                    border(eMenu[event],"green")
                else:
                    border(eMenu[event], "red")
            if event =="e10":
                if values[event] != "":
                    if values[event] is float:
                        border(eMenu[event], "green")
                else:
                    border(eMenu[event], "red")
            if event =="e11":
                if values[event] != "":
                    if values[event] is float:
                        border(eMenu[event], "green")
                else:
                    border(eMenu[event], "red")
            if event =="e12":
                if values[event] != "":
                    if values[event] is float:
                        border(eMenu[event], "green")
                else:
                    border(eMenu[event], "red")
            if event =="e13":
                if values[event] != "":
                    if values[event] is float:
                        border(eMenu[event], "green")
                else:
                    border(eMenu[event], "red")
            if event =="e14":
                if values[event]!="":
                    if values[event] is int and len(values[event])==10:
                        border(eMenu[event], "green")
                    if len(values[event])>10:
                        border(eMenu[event], "red")
                    else:
                        border(eMenu[event], "red")

            if event =="e15":
                if values[event]!="":
                    border(eMenu[event],"green")
                else:
                    border(eMenu[event], "red")
            if event =="e16":
                if values[event]!="":
                    if values[event].isalnum()==True  and 8<len(values[event])<19:
                        border(eMenu[event], "green")
                    if len(values[event])<9 and len(values[event])>18:
                        border(eMenu[event], "red")
                    else:
                        border(eMenu[event], "red")



            if event == "load simg":
                filename = values["e21"]
                if os.path.exists(filename):
                    image = Image.open(values["e21"])
                    image.thumbnail((300, 300))
                    bio = io.BytesIO()
                    # Actually store the image in memory in binary
                    image.save(bio, format="PNG")
                    # Use that image data in order to
                    eMenu["-IMAGE2-"].update(data=bio.getvalue())

            if event == "load nimg":
                filename = values["e24"]
                if os.path.exists(filename):
                    image = Image.open(values["e24"])
                    image.thumbnail((300, 300))
                    bio = io.BytesIO()
                    # Actually store the image in memory in binary
                    image.save(bio, format="PNG")
                    # Use that image data in order to
                    eMenu["-IMAGE3-"].update(data=bio.getvalue())

            if event=="pf":
                eMenu["e2"].update(value=Emp_code_Gen("PF"))

            if event =="non pf":
                eMenu["e2"].update(value=Emp_code_Gen("Non PF"))

            if event =="yes":
                eMenu["e11"].update(disabled=False)
                eMenu["e12"].update(disabled=False)
                eMenu["e13"].update(disabled=False)
                eMenu["e10"].update(disabled=True,value=0.00)

            if event =="no":
                eMenu["e11"].update(disabled=True, value=0.00)
                eMenu["e12"].update(disabled=True, value=0.00)
                eMenu["e13"].update(disabled=True, value=0.00)
                eMenu["e10"].update(disabled=False)

    if event =="etcnge":
        if values["etcnge"]==True:
           Menu["emp_data"].update(values=EmpdataFetch("Non PF") )
        if values["etcnge"] == False:
            Menu["emp_data"].update(values=EmpdataFetch("PF") )

    if event == "emp_data":
        data = Menu['emp_data'].get()
        globals()['crow'] = [data[row] for row in values[event]]
        print(crow)

    if event =="Update Employee":
        print(crow[0][0])
        a=crow[0][0]
        print("a",a)
        uMenu = ms.Window("Update Employee", [[ms.Column( Employee_update_GUI(a), scrollable=True, size=(760, 700), element_justification='centre')]])
        while True:
            event, values = uMenu.read()
            if event == ms.WIN_CLOSED:
                uMenu.close()
                break
            if event == 'update employee':
                Update_Employee(event, values)
            if event == "load pimg":
                filename = values["u25"]
                if os.path.exists(filename):
                    image = Image.open(values["u25"])
                    image.thumbnail((300, 300))
                    bio = io.BytesIO()
                    # Actually store the image in memory in binary
                    image.save(bio, format="PNG")
                    # Use that image data in order to
                    uMenu["-IMAGE-"].update(data=bio.getvalue())

            if event == "load simg":
                filename = values["u26"]
                if os.path.exists(filename):
                    image = Image.open(values["u26"])
                    image.thumbnail((300, 300))
                    bio = io.BytesIO()
                    # Actually store the image in memory in binary
                    image.save(bio, format="PNG")
                    # Use that image data in order to
                    uMenu["-IMAGE2-"].update(data=bio.getvalue())
            if event == "load nimg":
                filename = values["u29"]
                if os.path.exists(filename):
                    image = Image.open(values["u29"])
                    image.thumbnail((300, 300))
                    bio = io.BytesIO()
                    # Actually store the image in memory in binary
                    image.save(bio, format="PNG")
                    # Use that image data in order to
                    uMenu["-IMAGE3-"].update(data=bio.getvalue())
            if event == "PF":
                uMenu["u2"].update(values=Emp_code_Gen("PF"))
            if event == "Non PF":
                uMenu["u2"].update(values=Emp_code_Gen("Non PF"))
            if event == "yes":
                uMenu["u10"].update(disabled=False)
                uMenu["u11"].update(disabled=False)
                uMenu["u12"].update(disabled=False)
                uMenu["u9"].update(disabled=True, value=0.00)
            if event == "no":
                uMenu["u10"].update(disabled=True, value=0.00)
                uMenu["u11"].update(disabled=True, value=0.00)
                uMenu["u12"].update(disabled=True, value=0.00)
                uMenu["u9"].update(disabled=False)
            if event=="u25":
                if values["u25"]=="N":
                    uMenu["u26"].update(disabled=False)
                    uMenu["date3"].update(disabled=False)
                if values["u25"] == "y":
                    uMenu["u26"].update(disabled=True)
                    uMenu["date3"].update(disabled=True)

    if event == "Remove":
        chk = ms.popup_ok("Please Confirm to Delete", font=fstyle)
        if chk == "OK":
            mycursor.execute("UPDATE `register` SET `active_status` = 'N' WHERE (`emp_code` = '%s')" % crow[0][0])
            mydb.commit()
            Menu['emp_data'].update(values=EmpdataFetch("PF"))