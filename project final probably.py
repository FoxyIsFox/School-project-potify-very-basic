def payment():
    print('._____________________________________________.')
    print("|                   DOTIFY                    |")
    print("|                                             |")
    print("| Modes of payment:                           |")
    print("| 1)Credit card                               |")
    print("| 2)Debit card                                |")
    print("| 3)UPI/Wallet                                |")
    print('|_____________________________________________|')
    while True:
        payments = int(input(":"))
        if payments == 1:
            while True:
                transac = "Credit card"
                print("You chose: ",transac)
                print()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your card number (12 digits):  |")
                print('|_____________________________________________|')
                paymentcredit = input(':')
                if not paymentcredit.isdigit or len(paymentcredit) !=12:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Invalid card number. Please enter exactly   |")
                    print("| 12 digits.                                  |")
                    print('|_____________________________________________|')
                    continue
                print()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your CVC number (3 digits):    |")
                print('|_____________________________________________|')
                paymentcvc = input(":")
                if not paymentcvc.isdigit or len(paymentcvc) !=3:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Invalid CVC number. Please enter exactly    |")
                    print("| 3 digits                                    |")
                    print('|_____________________________________________|')
                    continue
                print()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Are these your card details?                |")
                print("| 1) Yes                                      |")
                print("| 2) No                                       |")
                print('|_____________________________________________|')
                confirmdetail = int(input(":"))
                if confirmdetail == 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif confirmdetail == 1:
                    if planchose == "Duo plan":
                        billd()
                        break
                    elif planchose == "Family plan":
                        billf()
                        break
                    else:
                        bill()
                        break
                else:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Enter a valid option                        |")
                    print('|_____________________________________________|')
                    continue

        elif payments == 2:
            while True:
                transac = "Debit card"
                print("You chose: ",transac)
                print()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your card number (12 digits):  |")
                print('|_____________________________________________|')
                paymentcredit = input(':')
                if not paymentcredit.isdigit or len(paymentcredit) !=12:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Invalid card number. Please enter exactly   |")
                    print("| 12 digits.                                  |")
                    print('|_____________________________________________|')
                    continue
                print()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your CVC number (3 digits):    |")
                print('|_____________________________________________|')
                paymentcvc = input(":")
                if not paymentcvc.isdigit or len(paymentcvc) !=3:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Invalid CVC number. Please enter exactly    |")
                    print("| 3 digits                                    |")
                    print('|_____________________________________________|')
                    continue
                print()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Are these your card details?                |")
                print("| 1) Yes                                      |")
                print("| 2) No                                       |")
                print('|_____________________________________________|')
                confirmdetail = int(input(":"))
                if confirmdetail == 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif confirmdetail == 1:
                    if planchose == "Duo plan":
                        billd()
                        break
                    elif planchose == "Family plan":
                        billf()
                        break
                    else:
                        bill()
                        break 
                else:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Enter a valid option                        |")
                    print('|_____________________________________________|')
                    continue
                
        elif payments == 3:
            while True:
                transac = "UPI"
                print("You chose: ",transac)
                print()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your UPI ID:                   |")
                print('|_____________________________________________|')
                paymentupi = input()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Is your UPI detail?                         |")
                print("| 1) Yes                                      |")
                print("| 2) No                                       |")
                print('|_____________________________________________|')
                paymentconfirm = int(input(":"))
                if paymentconfirm == 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Enter again                                 |")
                    print('|_____________________________________________|')
                    continue
                elif paymentconfirm == 1:
                    if planchose == "Duo plan":
                        billd()
                        break
                    elif planchose == "Family plan":
                        billf()
                        break
                    else:
                        bill()
                        break
                else:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Enter a valid option                        |")
                    print('|_____________________________________________|')
                    continue
                
        return

def bill():
    print('*******************Bill*******************')
    print('Your registered Gmail: ',gmail)
    print('Your plan: ',planchose)
    print('Your mode of transaction: ',transac)
    print('Your total bill:',billamount)
    print('******************************************')
    return

def billd():
    print('*******************Bill*******************')
    print('Your first registered Gmail: ',gmail)
    print('Your second registered gmail:',gmail2)
    print('Your plan: ',planchose)
    print('Your mode of transaction: ',transac)
    print('Your total bill:',billamount)
    print('******************************************')
    return

def billf():
    print('*******************Bill*******************')
    print('Your first registered Gmail: ',gmail)
    print('Your second registered gmail:',gmail2)
    print('Your third registered gmail:',gmail3)
    print('Your forth registered gmail:',gmail4)
    print('Your plan: ',planchose)
    print('Your mode of transaction: ',transac)
    print('Your total bill:',billamount)
    print('******************************************')
    return

def currectplanchose():
    if planchose == "Duo plan":
        print('*******************Plan*******************')
        print('Your first registered Gmail: ',gmail)
        print('Your second registered gmail:',gmail2)
        print('Your plan: ',planchose)
        print('Your mode of transaction: ',transac)
        print('Your total bill:',billamount)
        print('******************************************')  

    elif planchose == "Family plan":
        print('*******************Bill*******************')
        print('Your first registered Gmail: ',gmail)
        print('Your second registered gmail:',gmail2)
        print('Your third registered gmail:',gmail3)
        print('Your forth registered gmail:',gmail4)
        print('Your plan: ',planchose)
        print('Your mode of transaction: ',transac)
        print('Your total bill:',billamount)
        print('******************************************')

    elif planchose == "Individual plan":
        print('*******************Plan*******************')
        print('Your registered Gmail: ',gmail)
        print('Your plan: ',planchose)
        print('Your mode of transaction: ',transac)
        print('Your total bill:',billamount)
        print('******************************************')
    
    elif planchose =="Student plan":
        print('*******************Plan*******************')
        print('Your registered Gmail: ',gmail)
        print('Your plan: ',planchose)
        print('Your mode of transaction: ',transac)
        print('Your total bill:',billamount)
        print('******************************************')
    
def studentid():
    print('._____________________________________________.')
    print("|                   DOTIFY                    |")
    print("|                                             |")
    print("| Please enter your student ID before further |")
    print("| processes                                   |")
    print("| eg : 1234-1234-1234-1234                    |")
    print('|_____________________________________________|')
    print()
    while True:
        studentnumber = input(': ')
        if studentnumber.isdigit():
            if len(studentnumber)>16 or len(studentnumber)<16:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Invalid ID,please enter a valid ID          |")
                print('|_____________________________________________|')

                continue
            elif len(studentnumber) == 16:
                break
        else:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid ID,please enter a valid ID          |")
            print('|_____________________________________________|')
            continue
    print("You typed: ",studentnumber)

optionswitch =1
gmail = ""
planchose = ""
transac = ""
billamount = 0

print('._____________________________________________.')
print("|                   DOTIFY                    |")
print("|             Welcome to Dotify               |")
print('|_____________________________________________|')
while True:
    print('._____________________________________________.')
    print("|                   DOTIFY                    |")
    print("|                                             |")
    print("| What would you like to do                   |")
    print("| 1)Your plan                                 |")
    print("| 2)Know morw about the plans                 |")
    print("| 3)Terms and Conditions                      |")
    print("| 4)Playlists                                 |")
    print("| 5)Exit                                      |")
    print('|_____________________________________________|')
    Options = int(input(':'))
    if Options == 1:
        if optionswitch == 1:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Do you have an account?                     |")
            print("| 1)yes                                       |")
            print("| 2)no                                        |")
            print('|_____________________________________________|')
            accountyesorna = int(input(":"))
            while True:
                if accountyesorna == 2:
                    while True:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Enter your name:                            |")
                        print('|_____________________________________________|')
                        name = input(': ')
                        if name.isnumeric():
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Invalid, enter a valid name                 |")
                            print('|_____________________________________________|')
                            continue
                        else:
                            break
                    while True:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Enter your gmail:                           |")
                        print('|_____________________________________________|')
                        gmail = input(': ')
                        if "@" not in gmail:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Invalid, enter a valid gmail                |")
                            print('|_____________________________________________|')
                            continue
                        elif "@" in gmail:
                            break
                    while True:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Enter your phone no:                        |")
                        print('|_____________________________________________|')
                        no = input(': ')
                        if no.isdigit():
                            if len(no)>10 or len(no)<10:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid phone number         |")
                                print('|_____________________________________________|')
                                continue
                            elif len(no) == 10:
                                break
                        else:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Invalid,please enter a valid number         |")
                            print('|_____________________________________________|')
                            continue
                    print()
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Which music plan would you like to have     |")
                    print("| 1)Student plan at rupees 49                 |")
                    print("| 2)Individual plan at rupees 99              |")
                    print("| 3)Duo plan at rupees 199                    |")
                    print("| 4)Family plan at rupees 399                 |")
                    print('|_____________________________________________|')
                    newplan = int(input(":"))
                    if newplan == 1:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Student plan                |")
                        print("| 8 hours non stop ad free music              |")
                        print("| 15 song skip tokens                         |")
                        print("| Free podcasts                               |")
                        print('|_____________________________________________|')
                        print()
                        studentid()
                        optionswitch = optionswitch+1
                        planchose = "Student plan"
                        billamount = billamount+49
                        payment()
                    elif newplan == 2:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Individual plan             |")
                        print("| 12 hours non stop ad free music             |")
                        print("| 30 song skip tokens                         |")
                        print("| Custom playlists                            |")
                        print('|_____________________________________________|')
                        print()
                        optionswitch = optionswitch+1
                        planchose = "Individual plan"
                        billamount = billamount+99
                        payment()
                    elif newplan == 3:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Duo plan                    |")
                        print("| 24 hours non stop ad free music             |")
                        print("| Free chatting services                      |")
                        print("| Free mashup playlists                       |")
                        print('|_____________________________________________|')
                        print()
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your second gmail:                    |")
                            print('|_____________________________________________|')
                            gmail2 = input(': ')
                            if "@" not in gmail2 or gmail2 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail2:
                                break
                        optionswitch = optionswitch+1
                        planchose = "Duo plan"
                        billamount = billamount+199
                        payment()
                    elif newplan == 4:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Family plan                 |")
                        print("| Free buffet of dholakpur                    |")
                        print('|_____________________________________________|')
                        print()
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your second gmail:                    |")
                            print('|_____________________________________________|')
                            gmail2 = input(': ')
                            if "@" not in gmail2 or gmail2 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail2:
                                break
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your third gmail:                     |")
                            print('|_____________________________________________|')
                            gmail3 = input(': ')
                            if "@" not in gmail3 or gmail3 == gmail2 or gmail3 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail3:
                                break
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your forth gmail:                     |")
                            print('|_____________________________________________|')
                            gmail4 = input(': ')
                            if "@" not in gmail4 or gmail4 == gmail3 or gmail4 == gmail2 or gmail4 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail4:
                                break
                        optionswitch = optionswitch+1
                        planchose = "Family plan"
                        billamount = billamount+399
                        payment()
                    break
                
                elif accountyesorna == 1:
                    while True:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Enter your gmail:                           |")
                        print('|_____________________________________________|')
                        gmail = input(': ')
                        if "@" not in gmail:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Invalid, enter a valid gmail                |")
                            print('|_____________________________________________|')
                            continue
                        elif "@" in gmail:
                            break
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Whats your current plan:                    |")
                    print("| 1)Student plan                              |")
                    print("| 2)Individual plan                           |")
                    print("| 3)Duo plan                                  |")
                    print("| 4)Family plan                               |")
                    print('|_____________________________________________|')
                    plan = int(input(':'))
                    if plan == 1:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Student plan                |")
                        print("| 8 hours non stop ad free music              |")
                        print("| 15 song skip tokens                         |")
                        print("| Free podcasts                               |")
                        print('|_____________________________________________|')
                        print()
                        studentid()
                        optionswitch = optionswitch+1
                        planchose = "Student plan"
                        billamount = billamount+49
                        payment()
                    elif plan == 2:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Individual plan             |")
                        print("| 12 hours non stop ad free music             |")
                        print("| 30 song skip tokens                         |")
                        print("| Custom playlists                            |")
                        print('|_____________________________________________|')
                        print()
                        optionswitch = optionswitch+1
                        planchose = "Individual plan"
                        billamount = billamount+99
                        payment()
                    elif plan == 3:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Duo plan                    |")
                        print("| 24 hours non stop ad free music             |")
                        print("| Free chatting services                      |")
                        print("| Free mashup playlists                       |")
                        print('|_____________________________________________|')
                        print()
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your second gmail:                    |")
                            print('|_____________________________________________|')
                            gmail2 = input(': ')
                            if "@" not in gmail2 or gmail2 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail2:
                                break
                        optionswitch = optionswitch+1
                        planchose = "Duo plan"
                        billamount = billamount+199
                        payment()
                    elif plan == 4:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Family plan                 |")
                        print("| Free buffet of dholakpur                    |")
                        print('|_____________________________________________|')
                        print()
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your second gmail:                    |")
                            print('|_____________________________________________|')
                            gmail2 = input(': ')
                            if "@" not in gmail2:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail2:
                                break
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your third gmail:                     |")
                            print('|_____________________________________________|')
                            gmail3 = input(': ')
                            if "@" not in gmail3 or gmail3 == gmail2 or gmail3 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail3:
                                break
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your forth gmail:                     |")
                            print('|_____________________________________________|')
                            gmail4 = input(': ')
                            if "@" not in gmail4 or gmail4 == gmail3 or gmail4 == gmail2 or gmail4 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail4:
                                break
                        optionswitch = optionswitch+1
                        planchose = "Family plan"
                        billamount = billamount+399
                        payment()
                break
        elif optionswitch == 2:
            currectplanchose()
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Would like to upgrade/update your plan      |")
            print("| 1)yes                                       |")
            print("| 2)no                                        |")
            print('|_____________________________________________|')
            ugradeyesorno = int(input(":"))
            if ugradeyesorno == 1:
                if planchose == "Student plan":
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Would you like to upgrade/change your plan  |")
                    print("| to                                          |")
                    print("| 1)Individual plan                           |")
                    print("| 2)Duo plan                                  |")
                    print("| 3)Family plan                               |")
                    print('|_____________________________________________|')
                    choiceofupdrage = int(input(':'))
                    if choiceofupdrage == 1:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Individual plan             |")
                        print("| 12 hours non stop ad free music             |")
                        print("| 30 song skip tokens                         |")
                        print("| Custom playlists                            |")
                        print('|_____________________________________________|')
                        planchose = "Individual plan"
                        billamount = billamount+50
                        payment()
                    if choiceofupdrage == 2:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Duo plan                    |")
                        print("| 24 hours non stop ad free music             |")
                        print("| Free chatting services                      |")
                        print("| Free mashup playlists                       |")
                        print('|_____________________________________________|')
                        print()
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your second gmail:                    |")
                            print('|_____________________________________________|')
                            gmail2 = input(': ')
                            if "@" not in gmail2 or gmail2 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail2:
                                break
                        planchose = "Duo plan"
                        billamount = billamount+149
                        payment()
                    if choiceofupdrage == 3:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Family plan                 |")
                        print("| Free buffet of dholakpur                    |")
                        print('|_____________________________________________|')
                        print()
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your second gmail:                    |")
                            print('|_____________________________________________|')
                            gmail2 = input(': ')
                            if "@" not in gmail2:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail2:
                                break
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your third gmail:                     |")
                            print('|_____________________________________________|')
                            gmail3 = input(': ')
                            if "@" not in gmail3 or gmail3 == gmail2 or gmail3 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail3:
                                break
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your forth gmail:                     |")
                            print('|_____________________________________________|')
                            gmail4 = input(': ')
                            if "@" not in gmail4 or gmail4 == gmail3 or gmail4 == gmail2 or gmail4 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail4:
                                break
                        planchose = "Family plan"
                        billamount = billamount+349
                        payment()
                elif planchose ==  "Individual plan":
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Would you like to upgrade/change your plan  |")
                    print("| to                                          |")
                    print("| 1)Student plan                              |")
                    print("| 2)Duo plan                                  |")
                    print("| 3)Family plan                               |")
                    print('|_____________________________________________|')
                    choiceofupdrage = int(input(':'))
                    if choiceofupdrage == 1:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Student plan                |")
                        print("| 8 hours non stop ad free musics             |")
                        print("| 15 Song skip token                          |")
                        print("| Free podcasts                               |")
                        print('|_____________________________________________|')
                        print()
                        studentid()
                        planchose = "Student plan"
                        billamount = billamount-50
                        payment()
                    if choiceofupdrage == 2:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Duo plan                    |")
                        print("| 24 hours non stop ad free music             |")
                        print("| Free chatting services                      |")
                        print("| Free mashup playlists                       |")
                        print('|_____________________________________________|')
                        print()
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your second gmail:                    |")
                            print('|_____________________________________________|')
                            gmail2 = input(': ')
                            if "@" not in gmail2 or gmail2 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail2:
                                break
                        planchose = "Duo plan"
                        billamount = billamount+100
                        payment()
                    if choiceofupdrage == 3:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Family plan                 |")
                        print("| Free buffet of dholakpur                    |")
                        print('|_____________________________________________|')
                        print()
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your second gmail:                    |")
                            print('|_____________________________________________|')
                            gmail2 = input(': ')
                            if "@" not in gmail2:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail2:
                                break
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your third gmail:                     |")
                            print('|_____________________________________________|')
                            gmail3 = input(': ')
                            if "@" not in gmail3 or gmail3 == gmail2 or gmail3 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail3:
                                break
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your forth gmail:                     |")
                            print('|_____________________________________________|')
                            gmail4 = input(': ')
                            if "@" not in gmail4 or gmail4 == gmail3 or gmail4 == gmail2 or gmail4 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail4:
                                break
                        planchose = "Family plan"
                        billamount = billamount+300
                        payment()
                elif planchose == "Duo plan":
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Would you like to upgrade/change your plan  |")
                    print("| to                                          |")
                    print("| 1)Student plan                              |")
                    print("| 2)Individual plan                           |")
                    print("| 3)Family plan                               |")
                    print('|_____________________________________________|')
                    choiceofupdrage = int(input(':'))
                    if choiceofupdrage == 1:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Student plan                |")
                        print("| 8 hours non stop ad free musics             |")
                        print("| 15 Song skip token                          |")
                        print("| Free podcasts                               |")
                        print('|_____________________________________________|')
                        print()
                        studentid()
                        planchose = "Student plan"
                        billamount = billamount-150
                        payment()
                    if choiceofupdrage == 2:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Individual plan             |")
                        print("| 12 hours non stop ad free music             |")
                        print("| 30 song skip tokens                         |")
                        print("| Custom playlists                            |")
                        print('|_____________________________________________|')
                        planchose = "Individual plan"
                        billamount = billamount-100
                        payment()
                    if choiceofupdrage == 3:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Family plan                 |")
                        print("| Free buffet of dholakpur                    |")
                        print('|_____________________________________________|')
                        print()
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your second gmail:                    |")
                            print('|_____________________________________________|')
                            gmail2 = input(': ')
                            if "@" not in gmail2:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail2:
                                break
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your third gmail:                     |")
                            print('|_____________________________________________|')
                            gmail3 = input(': ')
                            if "@" not in gmail3 or gmail3 == gmail2 or gmail3 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail3:
                                break
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your forth gmail:                     |")
                            print('|_____________________________________________|')
                            gmail4 = input(': ')
                            if "@" not in gmail4 or gmail4 == gmail3 or gmail4 == gmail2 or gmail4 == gmail:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail4:
                                break
                        planchose = "Family plan"
                        billamount = billamount+200
                        payment()
                elif planchose == "Family plan":
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Would you like to upgrade/change your plan  |")
                    print("| to                                          |")
                    print("| 1)Student plan                              |")
                    print("| 2)Individual plan                           |")
                    print("| 3)Duo plan                                  |")
                    print('|_____________________________________________|')
                    choiceofupdrage = int(input(':'))
                    if choiceofupdrage == 1:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Student plan                |")
                        print("| 8 hours non stop ad free musics             |")
                        print("| 15 Song skip token                          |")
                        print("| Free podcasts                               |")
                        print('|_____________________________________________|')
                        print()
                        studentid()
                        planchose = "Student plan"
                        billamount = billamount-350
                        payment()
                    if choiceofupdrage == 2:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Individual plan             |")
                        print("| 12 hours non stop ad free music             |")
                        print("| 30 song skip tokens                         |")
                        print("| Custom playlists                            |")
                        print('|_____________________________________________|')
                        planchose = "Individual plan"
                        billamount = billamount-300
                        payment()
                    if choiceofupdrage == 3:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Welcome spotify Duo plan                    |")
                        print("| 24 hours non stop ad free music             |")
                        print("| Free chatting services                      |")
                        print("| Free mashup playlists                       |")
                        print('|_____________________________________________|')
                        print()
                        while True:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Enter your second gmail:                    |")
                            print('|_____________________________________________|')
                            gmail2 = input(': ')
                            if "@" not in gmail2:
                                print('._____________________________________________.')
                                print("|                   DOTIFY                    |")
                                print("|                                             |")
                                print("| Invalid, enter a valid gmail                |")
                                print('|_____________________________________________|')
                                continue
                            elif "@" in gmail2:
                                break
                        planchose = "Duo plan"
                        billamount = billamount-200
                        payment()
            elif ugradeyesorno == 2:
                print()

    elif Options == 2:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Student plan : at rupees 49                 |")
        print("| 8 hours non stop ad free musics             |")
        print("| 15 Song skip token                          |")
        print("| Free podcasts                               |")
        print("|                                             |")
        print("| Individual plan : at rupees 99              |")
        print("| 12 hours non stop ad free music             |")
        print("| 30 song skip tokens                         |")
        print("| Custom playlists                            |")
        print("|                                             |")
        print("| Duo plan : at rupees 199                    |")
        print("| 24 hours non stop ad free music             |")
        print("| Free chatting services                      |")
        print("| Free mashup playlists                       |")
        print("|                                             |")
        print("| Family plan : at rupees 399                 |")
        print("| Free buffet of dholakpur                    |")
        print('|_____________________________________________|')

    elif Options == 3:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("| Terms & Conditions By using this service,   |")
        print("| you agree to stream content for personal    |")
        print("| use only.                                   |")
        print("| No redistribution, resale, or public        |")
        print("| performance allowed. Content may be         |")
        print("| removed without notice.                     |")
        print("| We are not liable for data loss or service  |")
        print("| interruptions. Continued use implies        |")
        print("| acceptance of updates.                      |")
        print("| All rights reserved by respective creators. |")
        print('|_____________________________________________|')
    
    elif Options == 4:
        while True:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Playlists                                   |")
            print("| What type of playlists would you like:      |")
            print("| 1)Pop                                       |")
            print("| 2)Rap                                       |")
            print("| 3)Romance                                   |")
            print("| 4)Retro                                     |")
            print("| 5)Indie                                     |")
            print("| 6)Exit                                      |")
            print('|_____________________________________________|')
            playlist = int(input(":"))
            if playlist == 1:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Playlists                                   |")
                print("| For Pop                                     |")
                print("|                                             |")
                print("| 1)Dua lipa                                  |")
                print("|   1)Levatating                              |")
                print("|   2)Don't start now                         |")
                print("|   3)Fever                                   |")
                print("|   4)Love again                              |")
                print("|   5)Pretty please                           |")
                print("|                                             |")
                print("| 2)Sabrina Carpenter                         |")
                print("|   1)Espressso                               |")
                print("|   2)Please please please                    |")
                print("|   3)Manchild                                |")
                print("|   4)Taste                                   |")
                print("|   5)Juno                                    |")
                print("|                                             |")
                print("| 3)Katy perry                                |")
                print("|   1)Roar                                    |")
                print("|   2)California gurls                        |")
                print("|   3)Harleys in hawaii                       |")
                print("|   4)Dark horse                              |")
                print("|   5)Firewwork                               |")
                print("|                                             |")
                print("| 4)Weeknd                                    |")
                print("|   1)Blinding lights                         |")
                print("|   2)Starboy                                 |")
                print("|   3)Die for you                             |")
                print("|   4)Timeless                                |")
                print("|   5)Sao Paulo                               |")
                print("|                                             |")
                print("| More coming soon                            |")
                print('|_____________________________________________|')

            elif playlist == 2:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Playlists                                   |")
                print("| For Rap                                     |")
                print("|                                             |")
                print("| 1)Eminem                                    |")
                print("|   1)Mocking bird                            |")
                print("|   2)Real slim shady                         |")
                print("|   3)Without me                              |")
                print("|   4)Rap god                                 |")
                print("|   5)Godzilla                                |")
                print("|                                             |")
                print("| 2)Kendrick lamar                            |")
                print("|   1)Not like us                             |")
                print("|   2)Luther                                  |")
                print("|   3)TV off                                  |")
                print("|   4)Alright                                 |")
                print("|   5)Black panther                           |")
                print("|                                             |")
                print("| 3)Drake                                     |")
                print("|   1)Nokia                                   |")
                print("|   2)One dance                               |")
                print("|   3)God's plan                              |")
                print("|   4)Passionfruit                            |")
                print("|   5)Rich flex                               |")
                print("|                                             |")
                print("| More coming soon                            |")
                print('|_____________________________________________|')

            elif playlist == 3:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Playlists                                   |")
                print("| For Romance                                 |")
                print("|                                             |")
                print("| 1)D4vd                                      |")
                print("|   1)Here with me                            |")
                print("|   2)Romantic homocide                       |")
                print("|   3)Feel it                                 |")
                print("|   4)Sleep well                              |")
                print("|   5)You and i                               |")
                print("|                                             |")
                print("| 2)Boywithuke                                |")
                print("|   1)She said no                             |")
                print("|   2)Understand                              |")
                print("|   3)Two moons                               |")
                print("|   4)Prairies                                |")
                print("|   5)Heart of ice                            |")
                print("|                                             |")
                print("| 3)Bruno mars                                |")
                print("|   1)Talking to the moon                     |")
                print("|   2)Marry you                               |")
                print("|   3)Tressure                                |")
                print("|   4)When i was your man                     |")
                print("|   5)Grenade                                 |")
                print("|                                             |")
                print("| More coming soon                            |")
                print('|_____________________________________________|')

            elif playlist == 4:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Playlists                                   |")
                print("| For Retro                                   |")
                print("|                                             |")
                print("| 1)Michel jackson                            |")
                print("|   1)Billie jean                             |")
                print("|   2)Beat it                                 |")
                print("|   3)Smooth criminal                         |")
                print("|   4)Triller                                 |")
                print("|   5)Rock with you                           |")
                print("|                                             |")
                print("| More coming soon                            |")
                print('|_____________________________________________|')

            elif playlist == 5:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Playlists                                   |")
                print("| For Indie                                   |")
                print("|                                             |")
                print("| 1)Ovg!                                      |")
                print("|   1)Virginity syndrome                      |")
                print("|   2)Hoes no jutsu                           |")
                print("|   3)Death lotto                             |")
                print("|   4)Second chance                           |")
                print("|   5)Void vispers                            |")
                print("|                                             |")
                print("| 2)1nonly                                    |")
                print("|   1)Stay with me                            |")
                print("|   2)Shakira                                 |")
                print("|   3)Step back                               |")
                print("|   4)Zoom                                    |")
                print("|   5)Dance                                   |")
                print("|                                             |")
                print("| 3)Ciscaux                                   |")
                print("|   1)Rose                                    |")
                print("|   2)What a waste                            |")
                print("|   3)No offense                              |")
                print("|   4)Move                                    |")
                print("|   5)Bunny girl                              |")
                print("|                                             |")
                print("| More coming soon                            |")
                print('|_____________________________________________|')

            elif playlist == 6:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("|  Thank you                                  |")
                print("|  For checking out our playlists             |")
                print('|_____________________________________________|')
                break
            else:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter a valid option                 |")
                print('|_____________________________________________|')
                continue

    elif Options == 5:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Thank you for choosing dotify               |")
        print('|_____________________________________________|')
        break

    else:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Enter a valid option                        |")
        print('|_____________________________________________|')
        continue
#to do list
#errors prevention
#documutaion
