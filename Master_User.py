from Env import *

def master_user_GUI():

    layout_1=[[ms.Text("Master User"),ms.Sizer(20,0),ms.Button("Add",key="add_user")],
              [ms.Frame("Master User",
                        [[ms.Table(values=CCWFetch(),
                                   headings=["UID", "Name", "Password"],
                                   justification='centre', enable_events=True, auto_size_columns=False,
                                   row_height=30,
                                   col_widths=[10, 20, 20],
                                   right_click_selects=True,
                                   right_click_menu=[[], ["Remove"]],
                                   enable_click_events=True, size=(swi - 100, shi - 300), key="user_data",
                                   font=fstyle)]],
                        font=fstyle, element_justification='center')],
              [ms.Frame("Adding Mater_User", [
                  [ms.Text("Name", size=(20, 1)), ms.Sizer(45, 0),ms.Text("Password", size=(20, 1))],
                  [ms.Input("", size=(20, 1), do_not_clear=False, key='m_name', font=fstyle), ms.Sizer(5, 0),
                   ms.Input("", size=(20, 1), do_not_clear=False, key='m_password', font=fstyle),
                   ms.Button("Add", font=fstyle, key="add_user")]], visible=False, key="add_user2")]]
    layout_2=[[ms.Text("Work Discription"),ms.Sizer(20,0),ms.Button("Add",key="add_wrkdsp")],
              [ms.Frame("Work Discription",
                        [[ms.Table(values=[["","",""]],
                                   headings=["WID","Discription", "Amount"],
                                   justification='centre', enable_events=True, auto_size_columns=False,
                                   row_height=30,
                                   col_widths=[10, 35,20],
                                   right_click_selects=True,
                                   right_click_menu=[[], ["Remove"]],
                                   enable_click_events=True, size=(swi - 100, shi - 300), key="wrk_data",
                                   font=fstyle)]],
                font=fstyle, element_justification='center')],
              [ms.Frame("Adding Work", [
                  [ms.Text("Discription", size=(20, 1)),ms.Text("Amount", size=(20, 1))],
                  [ms.Multiline("", size=(30, 3), do_not_clear=False, key='cc_wrk', font=fstyle),
                   ms.Input("", size=(20, 1), do_not_clear=False, key='amount', font=fstyle),
                   ms.Button("Add", font=fstyle, key="add_wdsp")]], visible=False, key="add_discription")]]
    layout_3 = [[ms.Text("Mail list"), ms.Sizer(20, 0), ms.Button("Add", key="add_wrkdsp")],
                [ms.Frame("Mail list",
                          [[ms.Table(values=[["", "", ""]],
                                     headings=["UID","Name","Designation","Mai ID"],
                                     justification='centre', enable_events=True, auto_size_columns=False,
                                     row_height=30,
                                     col_widths=[10, 20, 20, 20],
                                     right_click_selects=True,
                                     right_click_menu=[[], ["Remove"]],
                                     enable_click_events=True, size=(swi - 100, shi - 300), key="wrk_data",
                                     font=fstyle)]],
                          font=fstyle, element_justification='center')],
                [ms.Frame("Adding Mail_User", [
                    [ms.Text("Name", size=(20, 1)),ms.Text("Designation", size=(20, 1)), ms.Text("Mail ID", size=(20, 1))],
                    [ms.Input("", size=(30, 3), do_not_clear=False, key='ml_name', font=fstyle),
                     ms.Input("", size=(20, 1), do_not_clear=False, key='designation', font=fstyle),
                     ms.Input("", size=(20, 1), do_not_clear=False, key='mail_id', font=fstyle),
                     ms.Button("Add", font=fstyle, key="add_mail_list")]], visible=False, key="add_mail_user")]]
    layout=[[ms.TabGroup([[ms.Tab("Master User",layout_1)],[ms.Tab("Work Discription",layout_2)],[ms.Tab("Mail ID",layout_3)]])]]
    return layout

