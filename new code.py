def Mode_of_Payment_stu():#Payment methods for 
    print()
    print('._____________________________________________.')
    print("|                   DOTIFY                    |")
    print("|                                             |")
    print("| Modes of payment:                           |")
    print("| 1)Credit card                               |")
    print("| 2)Debit card                                |")
    print("| 3)UPI/Wallet                                |")
    print('|_____________________________________________|')
    while True:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Enter what you want to proceed with:        |")
        print('|_____________________________________________|')
        paymentstudent = int(input(": "))
        print()
        if paymentstudent == 1:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your card number (12 digits):  |")
                print('|_____________________________________________|')
                paymentstudentcardnumber = input(": ")
                if not paymentstudentcardnumber.isdigit() or len(paymentstudentcardnumber) != 12:
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
                paymentstudentcvcnumber = input(': ')
                if not paymentstudentcvcnumber.isdigit() or len(paymentstudentcvcnumber) != 3:
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
                print()
                print('Card number: ', paymentstudentcardnumber)
                print('Card CVC number: ', paymentstudentcvcnumber)   
                print()  
                comfirmpaymentstudentcreditcard = int(input(': ')) 
                print()
                if comfirmpaymentstudentcreditcard == 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentstudentcreditcard == 1:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Spotify Student plan.            |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmail: ',gmail)
                    print('Your plan: Student')
                    print('Your mode of transaction: Credit card')
                    print('Your total bill: 49')
                    print('******************************************')
                    break
            break
        elif paymentstudent == 2:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your debit card number         |")
                print("| (12 digits):                                |")
                print('|_____________________________________________|')
                paymentstudentdebitnumber = input(": ")
                if not paymentstudentdebitnumber.isdigit() or len(paymentstudentdebitnumber) != 12:
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
                paymentstudentcvcdnumber = input(': ')
                if not paymentstudentcvcdnumber.isdigit() or len(paymentstudentcvcdnumber) != 3:
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
                print()
                print('Debit card number: ', paymentstudentdebitnumber)
                print('Card CVC number: ', paymentstudentcvcdnumber)   
                print() 
                comfirmpaymentstudentdebitcard = int(input(': ')) 
                print()
                if comfirmpaymentstudentdebitcard == 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentstudentdebitcard == 1:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Spotify Student plan.            |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmail: ',gmail)
                    print('Your plan: Student')
                    print('Your mode of transaction: Debit card')
                    print('Your total bill: 49')
                    print('******************************************')
                    break
            break
        elif paymentstudent == 3:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your UPI ID:                   |")
                print('|_____________________________________________|')
                paymentstudentUPIID = input(": ")
                print()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Are these your card details?                |")
                print("| 1) Yes                                      |")
                print("| 2) No                                       |")
                print('|_____________________________________________|')
                comfirmpaymentSUPIID = int(input(': ')) 
                print()
                if comfirmpaymentSUPIID== 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentSUPIID == 1:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Spotify Student plan.            |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmail: ',gmail)
                    print('Your plan: Student')
                    print('Your mode of transaction: UPI/Wallet')
                    print('Your total bill: 49')
                    print('******************************************')
                    break
            break
        else:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid input                               |")
            print('|_____________________________________________|')
            continue
    return 
def Mode_of_Payment_indi():#Payment methods for indivual

    print("| Modes of payment:                           |")
    print("| 1)Credit card                               |")
    print("| 2)Debit card                                |")
    print("| 3)UPI/Wallet                                |")
    print('|_____________________________________________|')
    while True:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Enter what you want to proceed with:        |")
        print('|_____________________________________________|')
        paymentindividual = int(input(": "))
        print()
        if paymentindividual == 1:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your card number (12 digits):  |")
                print('|_____________________________________________|')
                paymentindividualcardnumber = input(": ")
                if not paymentindividualcardnumber.isdigit() or len(paymentindividualcardnumber) != 12:
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
                paymentindividualcvcnumber = input(': ')
                if not paymentindividualcvcnumber.isdigit() or len(paymentindividualcvcnumber) != 3:
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
                print() 
                print('Card number: ', paymentindividualcardnumber)
                print('Card CVC number: ', paymentindividualcvcnumber)   
                print()  
                comfirmpaymentindividualcreditcard = int(input(': ')) 
                print()
                if comfirmpaymentindividualcreditcard == 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentindividualcreditcard == 1:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Spotify Individual plan.         |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmail: ',gmail)
                    print('Your plan: Individual')
                    print('Your mode of transaction: Credit card')
                    print('Your total bill: 119')
                    print('******************************************')
                    break
            break
        elif paymentindividual == 2:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your debit card number         |")
                print("| (12 digits):                                |")
                print('|_____________________________________________|')
                print()
                paymentindividualdebitnumber = input(": ")
                if not paymentindividualdebitnumber.isdigit() or len(paymentindividualdebitnumber) != 12:
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
                paymentindividualcvcdnumber = input(': ')
                if not paymentindividualcvcdnumber.isdigit() or len(paymentindividualcvcdnumber) != 3:
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
                print()
                print('Debit card number: ', paymentindividualdebitnumber)
                print('Card CVC number: ', paymentindividualcvcdnumber)   
                print()  
                comfirmpaymentIndividualdebitcard = int(input(': ')) 
                print()
                if comfirmpaymentIndividualdebitcard == 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentIndividualdebitcard == 1:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Spotify Individual plan.         |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmail: ',gmail)
                    print('Your plan: Individual')
                    print('Your mode of transaction: Debit card')
                    print('Your total bill: 119')
                    print('******************************************')
                    
                    break
            break
        elif paymentindividual == 3:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your UPI ID:                   |")
                print('|_____________________________________________|')
                paymentindividualUPIID = input(": ")
                print()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Are these your card details?                |")
                print("| 1) Yes                                      |")
                print("| 2) No                                       |")
                print('|_____________________________________________|')
                comfirmpaymentIUPIID = int(input(': ')) 
                print()
                if comfirmpaymentIUPIID== 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentIUPIID:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Spotify Individual plan.         |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmail: ',gmail)
                    print('Your plan: Individual')
                    print('Your mode of transaction: UPI/Wallet')
                    print('Your total bill: 119')
                    print('******************************************')
                    break
            break
        else:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid input                               |")
            print('|_____________________________________________|')
            continue
    return 
def Mode_of_Payment_Duo():#Payment methods for duo
    while True:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Enter your second gmail:                    |")
            print('|_____________________________________________|')
            gd1 = input(': ')
            if "@" not in gd1 or gd1==gmail:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Invalid input                               |")
                print('|_____________________________________________|')
                continue
            elif "@" in gd1:
                break
    while True:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Modes of payment:                           |")
        print("| 1)Credit card                               |")
        print("| 2)Debit card                                |")
        print("| 3)UPI/Wallet                                |")
        print('|_____________________________________________|')
        print()
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Enter what you want to proceed with:        |")
        print('|_____________________________________________|')
        paymentduo = int(input(": "))
        print()
        if paymentduo == 1:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your card number (12 digits):  |")
                print('|_____________________________________________|')
                paymentduocardnumber = input(": ")
                if not paymentduocardnumber.isdigit() or len(paymentduocardnumber) != 12:
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
                paymentduocvcnumber = input(': ')
                if not paymentduocvcnumber.isdigit() or len(paymentduocvcnumber) != 3:
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
                print()  
                print('Card number: ', paymentduocardnumber)
                print('Card CVC number: ', paymentduocvcnumber)   
                print()  
                comfirmpaymentduocreditcard = int(input(': ')) 
                print()
                if comfirmpaymentduocreditcard == 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentduocreditcard == 1:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Spotify Duo plan.                |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmails: ',gmail,"\nSecond gmail: ",gd1)
                    print('Your plan: Duo')
                    print('Your mode of transaction: Credit card')
                    print('Your total bill: 219')
                    print('******************************************')
                    break
            break
        elif paymentduo == 2:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your debit card number         |")
                print("| (12 digits):                                |")
                print('|_____________________________________________|')
                print()
                paymentduodebitnumber = input(": ")
                if not paymentduodebitnumber.isdigit() or len(paymentduodebitnumber) != 12:
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
                paymentduocvcdnumber = input(': ')
                if not paymentduocvcdnumber.isdigit() or len(paymentduocvcdnumber) != 3:
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
                print() 
                print('Debit card number: ', paymentduodebitnumber)
                print('Card CVC number: ', paymentduocvcdnumber)   
                print()  
                comfirmpaymentduodebitcard = int(input(': ')) 
                print()
                if comfirmpaymentduodebitcard == 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentduodebitcard == 1:
                    #bill
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Duo plan.                        |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmails: ',gmail,"\nSecond gmail: ",gd1)
                    print('Your plan: Duo')
                    print('Your mode of transaction: Debit card')
                    print('Your total bill: 219')
                    print('******************************************')
                    break
            break
        elif paymentduo == 3:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your UPI ID:                   |")
                print('|_____________________________________________|')
                paymentduoUPIID = input(": ")
                print()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Are these your UPI details?                 |")
                print("| 1) Yes                                      |")
                print("| 2) No                                       |")
                print('|_____________________________________________|')
                comfirmpaymentDUPIID = int(input(': ')) 
                print() 
                if comfirmpaymentDUPIID== 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again:            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentDUPIID == 1:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Duo plan.                        |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmails: ',gmail,"\nSecond gmail: ",gd1)
                    print('Your plan: Duo')
                    print('Your mode of transaction: UPI/Wallet')
                    print('Your total bill: 219')
                    print('******************************************')
                    break
            break
        else:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid input                               |")
            print('|_____________________________________________|')
            continue
    return
def Mode_of_Payment_Fam():#Payment methods for family
    while True:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Enter your second gmail:                    |")
        print('|_____________________________________________|')
        gf2 = input(': ')
        if "@" not in gf2 or gf2==gmail:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid input                               |")
            print('|_____________________________________________|')
            continue
        elif "@" in gf2:
            break
    while True:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Enter your third gmail:                     |")
        print('|_____________________________________________|')
        gf3 = input(': ')
        if "@" not in gf3 or gf2==gf3 or gf3==gmail:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid input                               |")
            print('|_____________________________________________|')
            continue
        elif "@" in gf3:
            break
    while True:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Enter your forth  gmail:                    |")
        print('|_____________________________________________|')
        gf4 = input(': ')
        if "@" not in gf4 or gf2==gf4 or gf3==gf4 or gf4==gmail:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid input                               |")
            print('|_____________________________________________|')
            continue
        elif "@" in gf4:
            break
    while True:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Modes of payment:                           |")
        print("| 1)Credit card                               |")
        print("| 2)Debit card                                |")
        print("| 3)UPI/Wallet                                |")
        print('|_____________________________________________|')
        print()
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Enter what you want to proceed with:        |")
        print('|_____________________________________________|')
        paymentfamily = int(input(": "))
        if paymentfamily == 1:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your card number (12 digits):  |")
                print('|_____________________________________________|')
                paymentfamilycardnumber = input(": ")
                if not paymentfamilycardnumber.isdigit() or len(paymentfamilycardnumber) != 12:
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
                paymentfamilycvcnumber = input(': ')
                if not paymentfamilycvcnumber.isdigit() or len(paymentfamilycvcnumber) != 3:
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
                print()
                print('Card number: ', paymentfamilycardnumber)
                print('Card CVC number: ', paymentfamilycvcnumber)
                print()  
                comfirmpaymentfamilycreditcard = int(input(': ')) 
                print()
                if comfirmpaymentfamilycreditcard == 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentfamilycreditcard == 1:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Spotify Family plan.             |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmails:',gmail,"\nSecond gmail: ",gf2,"\nThird gmail: ",gf3,"\nForth gmail: ",gf4)
                    print('Your plan: Family')
                    print('Your mode of transaction: Credit card')
                    print('Your total bill: 419')
                    print('******************************************')
                    break
            break
        elif paymentfamily == 2:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your debit card number         |")
                print("| (12 digits):                                |")
                print('|_____________________________________________|')
                print()
                paymentfamilydebitnumber = input(": ")
                if not paymentfamilydebitnumber.isdigit() or len(paymentfamilydebitnumber) != 12:
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
                paymentfamilycvcdnumber = input(': ')
                if not paymentfamilycvcdnumber.isdigit() or len(paymentfamilycvcdnumber) != 3:
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
                print() 
                print('Debit card number: ', paymentfamilydebitnumber)
                print('Card CVC number: ', paymentfamilycvcdnumber)   
                print()  
                comfirmpaymentfamdebitcard = int(input(': ')) 
                print()
                if comfirmpaymentfamdebitcard == 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again.            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentfamdebitcard == 1:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Family plan.                     |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmails: ',gmail,"\nSecond gmail: ",gf2,"\nThird gmail: ",gf3,"\nForth gmail: ",gf4)
                    print('Your plan: Family')
                    print('Your mode of transaction: Debit card')
                    print('Your total bill: 419')
                    print('******************************************')
                    break
            break
        elif paymentfamily == 3:
            while True:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Please enter your UPI ID:                   |")
                print('|_____________________________________________|')
                paymentfamilyUPIID = input(": ")
                print()
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Are these your UPI details?                 |")
                print("| 1) Yes                                      |")
                print("| 2) No                                       |")
                print('|_____________________________________________|')
                comfirmpaymentFUPIID = int(input(': ')) 
                print()
                if comfirmpaymentFUPIID== 2:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Please enter your details again:            |")
                    print('|_____________________________________________|')
                    continue
                elif comfirmpaymentFUPIID == 1:
                    print('._____________________________________________.')
                    print("|                   DOTIFY                    |")
                    print("|                                             |")
                    print("| Your transaction has been made.             |")
                    print("| Thank you for choosing Spotify.             |")
                    print("| Enjoy your Family plan.                     |")
                    print('|_____________________________________________|')
                    print()
                    print('*******************Bill*******************')
                    print('Your registered Gmails: ',gmail,"\nSecond gmail: ",gf2,"\nThird gmail: ",gf3,"\nForth gmail: ",gf4)
                    print('Your plan: Family')
                    print('Your mode of transaction: UPI/Wallet')
                    print('Your total bill: 419')
                    print('******************************************')
                    break
            break
        else:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid input                               |")
            print('|_____________________________________________|')
            continue
    return

#where it all began lol...

print('._____________________________________________.')
print("|              Welcome to Dotify              |")
print("|                                             |")
print("|                                             |")
print("| Do you have an account?                     |")
print("| 1)yes                                       |")
print("| 2)no                                        |")
print('|_____________________________________________|')
acc = int(input(': '))
if acc == 1:
    print('._____________________________________________.')
    print("|                   DOTIFY                    |")
    print("|                                             |")
    print("| What would like to see                      |")
    print("| 1)More about your plan/Upgrade              |")
    print("| 2)Terms and conditions of potify            |")
    print("| 3)Exit                                      |")
    print('|_____________________________________________|')
    plans = int(input(': '))
    if plans == 1:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Please re-enter your gmail for security     |")
        print("| reasons                                     |")
        print('|_____________________________________________|')#cheeky way to ask for gmail
        while True:
            gmail = input(': ')
            if "@" not in gmail:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Invalid input                               |")
                print('|_____________________________________________|')
                continue
            elif "@" in gmail:
                break
        print()
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Whats your current plan:                    |")
        print("| 1)Student plan                              |")
        print("| 2)Individual plan                           |")
        print("| 3)Duo plan                                  |")
        print("| 4)Family plan                               |")
        print('|_____________________________________________|')
        planinside = int(input(": "))#plan inside upgrade
        if planinside == 1:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Welcome spotify Student plan                |")
            print("| 8 hours non stop ad free musics             |")
            print("| 15 Song skip token                          |")
            print("| Free podcasts                               |")
            print("|                                             |")
            print("| Would you like to upgrade/change your plan  |")
            print("| to                                          |")
            print("| 1)Individual plan                           |")
            print("| 2)Duo plan                                  |")
            print("| 3)Family plan                               |")
            print("| 4)No, i am good                             |")
            print('|_____________________________________________|')
            planinsidestu = int(input(': '))#student 
            if planinsidestu == 1:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Individual plan             |")
                print("| 12 hours non stop ad free music             |")
                print("| 30 song skip tokens                         |")
                print("| Custom playlists                            |")
                print("|                                             |")
                Mode_of_Payment_indi()

            elif planinsidestu == 2:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Duo plan                    |")
                print("| 24 hours non stop ad free music             |")
                print("| Free chatting services                      |")
                print("| Free mashup playlists                       |")
                print('|_____________________________________________|')
                Mode_of_Payment_Duo()

            elif planinsidestu == 3:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Family plan                 |")
                print("| Free buffet of dholakpur                    |")
                print('|_____________________________________________|')
                Mode_of_Payment_Fam()
            
            elif planinsidestu == 4:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Thank you for choosing spotify              |")
                print('|_____________________________________________|')

            else:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Invalid input                               |")
                print('|_____________________________________________|')
        elif planinside == 2:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Welcome spotify Individual plan             |")
            print("| 12 hours non stop ad free music             |")
            print("| 30 song skip tokens                         |")
            print("| Custom playlists                            |")
            print("|                                             |")
            print("| Would you like to upgrade/change your plan  |")
            print("| to                                          |")
            print("| 1)Student plan                              |")
            print("| 2)Duo plan                                  |")
            print("| 3)Family plan                               |")
            print("| 4)No, i am good                             |")
            print('|_____________________________________________|')
            planinsideindi = int(input(': '))
            
            if planinsideindi == 1:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Student plan                |")
                print("| 8 hours non stop ad free musics             |")
                print("| 15 Song skip token                          |")
                print("| Free podcasts                               |")
                print("| Please enter your student ID before further |")
                print("|                                             |")
                print("| processes                                   |")
                print("| eg : 1234-1234-1234-1234                    |")
                print('|_____________________________________________|')
                while True:
                    studentnumber = input(': ')
                    if studentnumber.isdigit():
                        if len(studentnumber)>16 or len(studentnumber)<16:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Invalid input                               |")
                            print('|_____________________________________________|')
                            continue
                        elif len(studentnumber) == 16:
                            break
                    else:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Invalid input                               |")
                        print('|_____________________________________________|')
                        continue
                print("You typed: ",studentnumber)
                Mode_of_Payment_stu()

            elif planinsideindi == 2:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Duo plan                    |")
                print("| 24 hours non stop ad free music             |")
                print("| Free chatting services                      |")
                print("| Free mashup playlists                       |")
                print('|_____________________________________________|')
                Mode_of_Payment_Duo()

            elif planinsideindi == 3:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Family plan                 |")
                print("| Free buffet of dholakpur                    |")
                print('|_____________________________________________|')
                Mode_of_Payment_Fam()

            elif planinsideindi == 4:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Thank you for choosing spotify              |")
                print('|_____________________________________________|')
            else:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Invalid input                               |")
                print('|_____________________________________________|')
                
        elif planinside == 3:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Welcome spotify Duo plan                    |")
            print("| 24 hours non stop ad free music             |")
            print("| Free chatting services                      |")
            print("| Free mashup playlists                       |")
            print("|                                             |")
            print("| Would you like to upgrade/change your plan  |")
            print("| to                                          |")
            print("| 1)Student plan                              |")
            print("| 2)Indiviual plan                            |")
            print("| 3)Family plan                               |")
            print("| 4)No, i am good                             |")
            print('|_____________________________________________|')
            planinsideduo = int(input(': '))
            if planinsideduo == 1:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Student plan                |")
                print("| 8 hours non stop ad free musics             |")
                print("| 15 Song skip token                          |")
                print("| Free podcasts                               |")
                print("| Please enter your student ID before further |")
                print("|                                             |")
                print("| processes                                   |")
                print("| eg : 1234-1234-1234-1234                    |")
                print('|_____________________________________________|')
                while True:
                    studentnumber = input(': ')
                    if studentnumber.isdigit():
                        if len(studentnumber)>16 or len(studentnumber)<16:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Invalid input                               |")
                            print('|_____________________________________________|')
                            continue
                        elif len(studentnumber) == 16:
                            break
                    else:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Invalid input                               |")
                        print('|_____________________________________________|')
                        continue
                print("You typed: ",studentnumber)
                Mode_of_Payment_stu()

            elif planinsideduo == 2:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Individual plan             |")
                print("| 12 hours non stop ad free music             |")
                print("| 30 song skip tokens                         |")
                print("| Custom playlists                            |")
                print("|                                             |")
                Mode_of_Payment_indi()

            elif planinsideduo == 3:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Family plan                 |")
                print("| Free buffet of dholakpur                    |")
                print('|_____________________________________________|')
                Mode_of_Payment_Fam()

            elif planinsideduo == 4:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Thank you for choosing spotify              |")
                print('|_____________________________________________|')
            else:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Invalid input                               |")
                print('|_____________________________________________|')

        elif planinside == 4:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Welcome spotify Family plan                 |")
            print("| Free buffet of dholakpur                    |")
            print("|                                             |")
            print("| Would you like to upgrade/change your plan  |")
            print("| to                                          |")
            print("| 1)Student plan                              |")
            print("| 2)Indiviual plan                            |")
            print("| 3)Duo plan                                  |")
            print("| 4)No, i am good                             |")
            print('|_____________________________________________|')
            planinsidefam = int(input(': '))
            if planinsidefam == 1:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Student plan                |")
                print("| 8 hours non stop ad free musics             |")
                print("| 15 Song skip token                          |")
                print("| Free podcasts                               |")
                print("| Please enter your student ID before further |")
                print("|                                             |")
                print("| processes                                   |")
                print("| eg : 1234-1234-1234-1234                    |")
                print('|_____________________________________________|')
                while True:
                    studentnumber = input(': ')
                    if studentnumber.isdigit():
                        if len(studentnumber)>16 or len(studentnumber)<16:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Invalid input                               |")
                            print('|_____________________________________________|')
                            continue
                        elif len(studentnumber) == 16:
                            break
                    else:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Invalid input                               |")
                        print('|_____________________________________________|')
                        continue
                print("You typed: ",studentnumber)
                Mode_of_Payment_stu()

            elif planinsidefam == 2:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Individual plan             |")
                print("| 12 hours non stop ad free music             |")
                print("| 30 song skip tokens                         |")
                print("| Custom playlists                            |")
                print("|                                             |")
                Mode_of_Payment_indi()

            elif planinsidefam == 3:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Welcome spotify Duo plan                    |")
                print("| 24 hours non stop ad free music             |")
                print("| Free chatting services                      |")
                print("| Free mashup playlists                       |")
                print('|_____________________________________________|')
                Mode_of_Payment_Duo()

            elif planinsidefam == 4:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Thank you for choosing spotify              |")
                print('|_____________________________________________|')
            else:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Invalid input                               |")
                print('|_____________________________________________|')
        else:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid input                               |")
            print('|_____________________________________________|')
    elif plans == 2:
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
    else:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Come around again                           |")
        print('|_____________________________________________|')

elif acc == 2: #new account
    #Taking Information From the Customer
    while True:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Enter your name                             |")
        print('|_____________________________________________|')
        name = input(': ')
        if name.isnumeric():
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid input                               |")
            print('|_____________________________________________|')
            continue
        else:
            break
    while True:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Enter your gmail                            |")
        print('|_____________________________________________|')
        gmail = input(': ')
        if "@" not in gmail:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid input                               |")
            print('|_____________________________________________|')
            continue
        elif "@" in gmail:
            break
    while True:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Enter your phone no                         |")
        print('|_____________________________________________|')
        no = input(': ')
        if no.isdigit():
            if len(no)>10 or len(no)<10:
                print('._____________________________________________.')
                print("|                   DOTIFY                    |")
                print("|                                             |")
                print("| Invalid input                               |")
                print('|_____________________________________________|')
                continue
            elif len(no) == 10:
                break
        else:
            print('._____________________________________________.')
            print("|                   DOTIFY                    |")
            print("|                                             |")
            print("| Invalid input                               |")
            print('|_____________________________________________|')
            continue
    print()
    #Plan Options
    print('._____________________________________________.')
    print("|                   DOTIFY                    |")
    print("|                                             |")
    print("| Which music plan would you like to have     |")
    print("| 1)Student plan                              |")
    print("| 2)Individual plan                           |")
    print("| 3)Duo plan                                  |")
    print("| 4)Family plan                               |")
    print('|_____________________________________________|')
    print()
    #Yapping
    plan = int(input(': '))
    if plan == 1:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Welcome spotify Student plan                |")
        print("| 8 hours non stop ad free musics             |")
        print("| 15 Song skip token                          |")
        print("| Free podcasts                               |")
        print("| Please enter your student ID before further |")
        print("|                                             |")
        print("| processes                                   |")
        print("| eg : 1234-1234-1234-1234                    |")
        print('|_____________________________________________|')
        while True:
                    studentnumber = input(': ')
                    if studentnumber.isdigit():
                        if len(studentnumber)>16 or len(studentnumber)<16:
                            print('._____________________________________________.')
                            print("|                   DOTIFY                    |")
                            print("|                                             |")
                            print("| Invalid input                               |")
                            print('|_____________________________________________|')
                            continue
                        elif len(studentnumber) == 16:
                            break
                    else:
                        print('._____________________________________________.')
                        print("|                   DOTIFY                    |")
                        print("|                                             |")
                        print("| Invalid input                               |")
                        print('|_____________________________________________|')
                        continue
        print("You typed: ",studentnumber)
        Mode_of_Payment_stu()

    elif plan == 2:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Welcome spotify Individual plan             |")
        print("| 12 hours non stop ad free music             |")
        print("| 30 song skip tokens                         |")
        print("| Custom playlists                            |")
        print("|                                             |")
        Mode_of_Payment_indi()

    elif plan == 3:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Welcome spotify Duo plan                    |")
        print("| 24 hours non stop ad free music             |")
        print("| Free chatting services                      |")
        print("| Free mashup playlists                       |")
        print('|_____________________________________________|')
        Mode_of_Payment_Duo()

    elif plan == 4:
        print('._____________________________________________.')
        print("|                   DOTIFY                    |")
        print("|                                             |")
        print("| Welcome spotify Family plan                 |")
        print("| Free buffet of dholakpur                    |")
        print('|_____________________________________________|')
        Mode_of_Payment_Fam()


# THE END
#Collabaration of  CO-pilot(shaurya) and ChatGPT(vansh)
print('''        ⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡼⠙⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⠃⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡎⠀⠀⠀⢹⣿⣆⠀⠀⠀⠀⠀⣼⣿⠁⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⠞⢻⣿⡆⠀⠀⠀⢰⣿⣿⡀⠀⠀⢹⡄⠀⠀⠀⠀⢀⣤⣤⡄⠀⠀⣀⣤⣤⣀
⠀⠀⠀⠀⠀⠀⡇⠀⢰⠋⠀⠈⣿⣿⡄⠀⠀⣾⣿⡇⠹⡄⠀⢨⡇⠀⠀⠀⢸⣿⣿⣿⣿⣾⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⡇⢀⡏⠀⢀⣴⣿⣿⣿⣿⣾⣿⣿⣧⡀⢳⠀⢸⡁⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀
⠀⠀⠀⠀⠀⠀⢣⠸⣅⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡀⣸⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣦⣿⣿⡿⠛⠻⢿⣿⣿⣿⣿⡟⠉⠙⢿⣿⣇⠀⠀⠀⣀⣠⡄⠀⠀⠀⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⡿⠀⠀⣿⡟⣿⣿⣿⣿⢸⣷⠀⠈⣿⣿⣤⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠚⠉⠉⠉⠙⠒⠲⣿⣿⣷⠀⠀⠙⢡⣿⣿⣽⣿⣌⠁⠀⣰⣿⣿⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⠽⢿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠉⠑⠒⠠⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⠴⠚⠉⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')	
print('Tank you cat')
