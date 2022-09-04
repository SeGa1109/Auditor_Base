from Env import *
def WageCalcLay():
    head=['Emp Code','Name','F/S Name','Days Present','S1','S2','S3','Wage','OT','OT Wages','Incentive','Gross Wages','PF','ESI','Adv.','Canteen','Net Wages']
    headwidth=[12,25,25,5,5,5,5,10,5,10,10,15,10,10,10,10,20]
    TL_WCEXP=[[
    ms.Table(values=[], headings=head,
                justification='centre', enable_events=True,
                auto_size_columns=False,
                row_height=20,
                col_widths=headwidth,
                num_rows=100,
                font=fstyle,
                enable_click_events=True, key="TL_WC")
    ]]
    layout=[
        [ms.Input(todatemy,font=fstyle,size=(10,1),key='wcdateinp'),ms.CalendarButton(" ",target='wcdateinp',format="%m-%Y"),
         ms.Button("Generate",key='wcgen',font=fstyle),ms.Sizer(400,0), ms.Text("Wages Report Generation",font=fstylehd ),ms.Sizer(500,0),
         ms.Button("Export",key='wcexp',font=fstyle)],
       [ ms.Frame("Output",layout=[[ms.Column(TL_WCEXP,scrollable=True,size=(swi-50,shi-80),)]],font=fstyle,size=(swi-50,shi-80))
    ]
    ]
    return layout

def WageCalcFn(Menu,event,values):
    if event == 'wcgen':
        incentive_chk=int(ms.popup_get_text("Enter the number of days for incentive addition",no_titlebar=True,font=fstyle,location=(30,100)))
        incentive_amnt=float(ms.popup_get_text("Incentive Amount",no_titlebar=True,font=fstyle,location=(30,100)))
        data = attendance_fetch(values['wcdateinp'])
        print(data)
        wagedata = wage_fetch()
        wage_proc_data=[]
        #print(data)
        for step in data:
            #print(step)
            temp=[]
            for i in range (3):#EMP Details addition
                temp.append(step[i])
            chk = list(step[3].split(","))#Shift Check
            print(chk)
            if chk[0] not in ['P','A']:# if Emp is Shift resource
                wagetemp=wagedata.get(step[0])
                print(wagetemp)
                temp.append("NA")
                S1,S2,S3,OT=0,0,0,0
                CE=0.0
                for i in range (4,len(step)):# Custom Shift Calc
                    i=list(step[i].split(","))
                    if i[0] == '1':
                        S1+=1
                    if i[0] == '2':
                        S2+=1
                    if i[0] == '3':
                        S3+=1
                    OT+=int(i[1]) # OT Addition
                    CE+=float(i[2]) # CE Addition
                temp.append(S1)
                temp.append(S2)
                temp.append(S3)
                wage = (S1*wagetemp[0])+(S2*wagetemp[1])+(S3*wagetemp[2]) # Wage Calc
                temp.append(wage)
                ot_wage = (OT / 8 * wagetemp[0])  # OT Calc
                if step[3] == "yes":
                    incentive = 0.0
                elif S1 + S2 + S3 >= incentive_chk:
                    incentive = incentive_amnt
                else:
                    incentive = 0.0
            else:
                wagetemp = wagedata.get(step[0])
                DP,OT=0,0
                CE = 0.0
                for i in range(4, len(step)):  # DP Calc
                    i = list(step[i].split(","))
                    if i[0] == 'P':
                        DP+=1
                    OT+=int(i[1]) # OT Addition
                    CE+=float(i[2]) # CE Addition
                temp.append(DP)
                temp.append("NA")
                temp.append("NA")
                temp.append("NA")
                wage = DP*wagetemp
                temp.append(wage)
                ot_wage = (OT / 8 * wagetemp)
                if step[3]=="yes":
                    incentive=0.0
                elif DP >= incentive_chk:
                    incentive = incentive_amnt
                else:
                    incentive = 0.0

            temp.append(OT)
            temp.append(ot_wage)
            temp.append("NA" if step[3]=="yes" else incentive)
            gross_wage=wage+ot_wage+incentive
            temp.append(gross_wage)
            PF=round(gross_wage*12/100,0)#PF Calculation
            temp.append(PF)
            ESI=round(gross_wage*0.75/100,0)#ESI Calculation
            temp.append(ESI)
            ADV=0.0#Advance Calc
            temp.append(ADV)
            temp.append(CE)#Canteen Expense Addition
            netwage=gross_wage-PF-ESI-ADV-CE
            temp.append(netwage)
            wage_proc_data.append(temp)

        Menu['TL_WC'].update(values=wage_proc_data)

