from Env import *

def Master_User_GUI():

    layout_1=[[ms.Text("Master User"),ms.Sizer(20,0),ms.Button("Add",key="add_user")],
              [ms.Frame("Master User",
                        [[ms.Table(values=MUWFetch(),
                                   headings=["UID", "Name", "Password"],
                                   justification='centre', enable_events=True, auto_size_columns=False,
                                   row_height=50,num_rows=10,
                                   col_widths=[10, 20, 20],
                                   right_click_selects=True,
                                   right_click_menu=[[], ["Remove "]],
                                   enable_click_events=True, size=(swi - 100, shi - 300), key="user_data",
                                   font=fstyle)]],
                        font=fstyle, element_justification='center')],
              [ms.Frame("Adding Mater_User", [
                  [ms.Text("Name", size=(20, 1)), ms.Sizer(45, 0),ms.Text("Password", size=(20, 1))],
                  [ms.Input("", size=(20, 1), do_not_clear=False, key='u_name', font=fstyle), ms.Sizer(5, 0),
                   ms.Input("", size=(20, 1), do_not_clear=False, key='u_password', font=fstyle),
                   ms.Button("Add", font=fstyle, key="add_user1")]], visible=False, key="add_user2")]]
    layout_2=[[ms.Text("Work Discription"),ms.Sizer(20,0),ms.Button("Add",key="add_wrkdsp")],
              [ms.Frame("Work Discription",
                        [[ms.Table(values=CCWORKFetch(),
                                   headings=["WID","Discription", "Amount"],
                                   justification='centre', enable_events=True, auto_size_columns=False,
                                   row_height=30,num_rows=10,
                                   col_widths=[10, 50,20],
                                   right_click_selects=True,
                                   right_click_menu=[[], [" Remove"]],
                                   enable_click_events=True, size=(swi - 100, shi - 300), key="wrk_data",
                                   font=fstyle)]],
                font=fstyle, element_justification='center')],
              [ms.Frame("Adding Work", [
                  [ms.Text("Discription", size=(20, 1)),ms.Text("Amount", size=(20, 1))],
                  [ms.Multiline("", size=(30, 3), do_not_clear=False, key='cc_wrk', font=fstyle),
                   ms.Input("", size=(20, 1), do_not_clear=False, key='amount', font=fstyle),
                   ms.Button("Add", font=fstyle, key="add_wdsp")]], visible=False, key="add_discription")]]
    layout_3 = [[ms.Text("Mail list"), ms.Sizer(20, 0), ms.Button("Add", key="add_mail")],
                [ms.Frame("Mail list",
                          [[ms.Table(values=MAILFetch(),
                                     headings=["UID","Name","Designation","Mai ID"],
                                     justification='centre', enable_events=True, auto_size_columns=False,
                                     row_height=30,
                                     col_widths=[10, 20, 20, 20],
                                     right_click_selects=True,
                                     num_rows=10,
                                     right_click_menu=[[], [" Remove "]],
                                     enable_click_events=True, size=(swi - 100, shi - 300), key="mail_data",
                                     font=fstyle)]],
                          font=fstyle, element_justification='center')],
                [ms.Frame("Adding Mail_User", [
                    [ms.Text("Name", size=(20, 1)),ms.Text("Designation", size=(20, 1)), ms.Text("Mail ID", size=(20, 1))],
                    [ms.Input("", size=(20, 1), do_not_clear=False, key='ml_name', font=fstyle),
                     ms.Input("", size=(20, 1), do_not_clear=False, key='designation', font=fstyle),
                     ms.Input("", size=(20, 1), do_not_clear=False, key='mail_id', font=fstyle),
                     ms.Button("Add", font=fstyle, key="add_mail_list")]], visible=False, key="add_mail_user")]]
    layout=[[ms.TabGroup([[ms.Tab("Master User",layout_1)],[ms.Tab("Work Discription",layout_2)],[ms.Tab("Mail ID",layout_3)]])]]
    return layout

def Master_User(Menu,event,values):
    if event =="add_user":
        chk = ms.popup_get_text("Enter password to add user ", password_char='*', size=(10, 1), font=fstyle, no_titlebar=True, keep_on_top=True)
        if chk == "AstA_SIL":
            Menu["add_user2"].update(visible=True)
    if event =="add_wrkdsp":
        Menu["add_discription"].update(visible=True)
    if event =="add_mail":
        Menu["add_mail_user"].update(visible=True)
    if event == "add_user1":
        if values["u_name"] and values["u_password"] !="":
            sql = "INSERT INTO user_details ( user_name,user_password ) VALUES ( '%s','%s')" % (
            values["u_name"], values["u_password"])
            mycursor.execute(sql)
            mydb.commit()
            Menu["user_data"].update(values=MUWFetch())
            Menu["add_user2"].update(visible=False)
    if event == "add_wdsp":
        if values['cc_wrk'] and values['amount'] !="":
            sql = "INSERT INTO cc_work_list ( discription,amount ) VALUES ( '%s','%s')" % (values['cc_wrk'], values['amount'])
            mycursor.execute(sql)
            mydb.commit()
            Menu["wrk_data"].update(values=CCWORKFetch())
            Menu["add_discription"].update(visible=False)
    if event == "add_mail_list":
        if values['ml_name'] and values['designation'] and values['mail_id'] !="":
            sql = "INSERT INTO mail_list (name_,designation,mail_id ) VALUES ( '%s','%s','%s')" % (
            values['designation'], values['designation'],values['mail_id'])
            mycursor.execute(sql)
            mydb.commit()
            Menu["mail_data"].update(values=MAILFetch())
            Menu["add_discription"].update(visible=False)
    if event == "Remove ":
        chk = ms.popup_get_text("Enter password to remove user ", password_char='*', size=(10,1), font=fstyle, no_titlebar=True, keep_on_top=True)
        if chk == "AstA_SIL":
            mycursor.execute("DELETE FROM user_details WHERE UID='%s'" % remove_data(Menu,"user_data",values)[0][0])
            mydb.commit()
            Menu["user_data"].update(values=MUWFetch())
    if event == " Remove":
        chk = ms.popup_ok("Please Confirm to Delete", font=fstyle)
        if chk == "OK":
            mycursor.execute("DELETE FROM cc_work_list WHERE WID='%s'" % remove_data(Menu,"wrk_data",values)[0][0])
            mydb.commit()
            Menu["user_data"].update(values=CCWORKFetch())
    if event == " Remove ":
        chk = ms.popup_ok("Please Confirm to Delete", font=fstyle)
        if chk == "OK":
            mycursor.execute("DELETE FROM mail_list WHERE UID='%s'" % remove_data(Menu,"mail_data",values)[0][0])
            mydb.commit()
            Menu["mail_data"].update(values=MAILFetch())


Menu = ms.Window("Add Employee", [[ms.Column(Master_User_GUI(), scrollable=True, size=(960, 700), element_justification='centre')]], finalize=True)
while True:
    event, values = Menu.read()
    if event == ms.WIN_CLOSED:
        Menu.close()
        break
    Master_User(Menu, event, values)