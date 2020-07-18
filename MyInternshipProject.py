
# ===================== Menu Funtion ========================
import getpass


def menu():
    print("CHOOSE ANY OPTION :-")
    print("     1. Add New Account.")
    print("     2. Check Account.")
    print("     3. Withdraw Amount.")
    print("     4. Deposite Amount.")
    print("     5. Transfer Account to Account.")
    print("     6. View All User.")
    print("     7. Quit.")

# ================= Add Account ============================
def addAccount(fp):
    print("Enter Details for New Account :-")
    name = input("      Enter Your First Name : ")
    f = input("      Enter your age : ")
    balance = input("      Enter Initial Balance : Rs.")
    phnNumber = input("      Enter Your Phone Number : ")
    pin = input("      Enter your 4 digit pin : ")

    #####Automatic Account Number generater##############
    fp.seek(0, 0)
    if fp.read() == '':
        AccountNumber = 1111
    else:
        comp = 1111
        fp.seek(0, 0)
        q = fp.readlines()
        for a in q:
            last = int(a.strip().split()[1])
            if last > comp:
                comp = last

        AccountNumber = comp + 1
    #########################################
    accountNumber = str(AccountNumber)

    fp.write(name + " " + accountNumber + " " + f + " " + balance + " " + phnNumber + " " + pin + "\n")
    print("\n**Account Succesfull Created And Activated!")
    print("Your Account Number is : "+accountNumber)

    try:
        msg1 = "Mr." + name + ' Your Account is Activated.'
        msg2 = "Your Account Number is : " + accountNumber;
        message(phnNumber,msg1,msg2)
    except Exception:
        pass;

# ================View Account ============================
def checkAccount(fp):
    out = ''
    accNum = int(input("Enter Account Number : "))
    fp.seek(0, 0)
    data = list(enumerate(fp.readlines()))
    le = data[-1][0]
    for x in range(le,-1,-1):
        nm = data[x][1].split()[1]
        if int(nm)==accNum:
            print("  @Account Founded.")
            print("     *Account Owner Name : Mr." + data[x][1].split()[0].upper())
            print("     *Account Owner Age : " + data[x][1].split()[2] + "yr")
            print("     *Account Balance : Rs." + data[x][1].split()[3])
            print("     *Phone Number : " + data[x][1].split()[4])
            out = ''
            break
        else:
            out = "No Such Account!"

    print(out)

# =====================WithDraw Funtion========================
def withDraw(fp):
    fp.seek(0,0)
    out = ''
    accNum = int(input("Enter Account Number : "))
    fp.seek(0, 0)
    data = list(enumerate(fp.readlines()))
    le = data[-1][0]
    cret = ''
    for x in range(le,-1,-1):
        nm = data[x][1].split()[1]
        if int(nm)==accNum:
            store = data[x][1];
            print("  @Account Founded.")
            print("     *Account Owner Name : Mr." + data[x][1].split()[0].upper())
            print("")
            k = float(data[x][1].split()[3])
            pin = input("Enter 4 digit PIN : ")
            if pin == store.split()[5]:
                print("     ---> PIN Matched!")
                print("")
                amt = float(input("Enter Amount to be Withdraw : Rs."))
                if amt<float(store.split()[3]):
                    netAmt = float(store.split()[3]) - amt
                    amou = str(netAmt)
                    ha = store.split()
                    ha.pop(3)
                    ha.insert(3,amou)
                    for q in ha:
                        cret += q + " "
                    fp.write(cret+"\n")
                    print(f"    *Rs.{amt} is Successfull Withdraw from Your Account.")
                    print(f"     Your Remaining Balance is Rs.{ha[3]}.")
                    try:
                        msg1 = "Mr." + data[x][1].split()[0] + '. Rs.' + str(amt) + ' is Withdraw from Your Account.'
                        msg2 = "Your Remaining Balance is  Rs." + str(ha[3]);
                        message(data[x][1].split()[4], msg1, msg2)
                    except Exception:
                        pass
                else:
                    print("UnSufficient Balance!")
            else:
                print("Wrong PIN!")
            break
        else:
            out = "No Such Account!"

# =====================Deposite funtion========================
def deposite(fp):
    fp.seek(0,0)
    out = ''
    accNum = int(input("Enter Account Number : "))
    fp.seek(0, 0)
    data = list(enumerate(fp.readlines()))
    le = data[-1][0]
    cret = ''
    for x in range(le,-1,-1):
        nm = data[x][1].split()[1]
        if int(nm)==accNum:
            store = data[x][1];
            print("  @Account Founded.")
            print("     *Account Owner Name : Mr." + data[x][1].split()[0].upper())
            k = float(data[x][1].split()[3])
            print("")
            pin = input("Enter 4 digit PIN : ")
            if pin == store.split()[5]:
                print("     ---> PIN Matched!")
                print("")
                amt = float(input("Enter Amount to be Deposite : Rs."))
                netAmt = float(store.split()[3]) + amt
                amou = str(netAmt)
                ha = store.split()
                ha.pop(3)
                ha.insert(3,amou)
                for q in ha:
                    cret += q + " "
                fp.write(cret+"\n")
                print(f"    *Rs.{amt} is Successfull Deposite from Your Account.")
                print(f"     Now, Your Balance is Rs.{ha[3]}.")
                try:
                    msg1 = "Mr." + data[x][1].split()[0].upper() + '. Rs.' + str(amt) + ' is Deposited in Your Account.'
                    msg2 = "Now, Your Balance is  Rs." + str(ha[3]);
                    message(data[x][1].split()[4], msg1, msg2)
                except Exception:
                    pass
                break
            else:
                out = 'Wrong PIN!'
            break
        else:
            out = "No Such Account!"
    print(out)
# =====================Transfer Amount========================
def transfer(fp):
    fp.seek(0, 0)
    out = ''
    accNum = int(input("Enter Account Number : "))
    fp.seek(0, 0)
    data = list(enumerate(fp.readlines()))
    le = data[-1][0]
    for x in range(le, -1, -1):
        nm = data[x][1].split()[1]
        if int(nm) == accNum:
            store = data[x][1];
            print("  @Account Founded.")
            print("     *Account Owner Name : Mr." + data[x][1].split()[0].upper())
            k = float(data[x][1].split()[3])
            pin = input("Enter 4 digit PIN : ")
            if pin == store.split()[5]:
                print("     ---> PIN Matched!")
                print("")
                fp.seek(0,0)
                datarec = list(enumerate(fp.readlines()))
                lerec = datarec[-1][0]
                accNumrec = int(input("Enter Account Number You want to Transfer : "))
                for y in range(lerec, -1, -1):
                    nmRec = data[y][1].split()[1]
                    if int(nmRec) == accNumrec:
                        storeRec = datarec[y][1];
                        print("  @Account Founded.")
                        print("     *Account Owner Name : Mr." + datarec[y][1].split()[0].upper())
                        print("")
                        sendAmt = float(input("Enter Amount to be Transfer : Rs."))

                        #Add amt
                        cret = ''
                        netAmt = float(storeRec.split()[3]) + sendAmt
                        amou = str(netAmt)
                        haRec = storeRec.split()
                        haRec.pop(3)
                        haRec.insert(3, amou)
                        for q in haRec:
                            cret += q + " "
                        fp.write(cret + "\n")

                        #reomve amt
                        cret = ''
                        netAmt = float(store.split()[3]) - sendAmt
                        amou = str(netAmt)
                        ha = store.split()
                        ha.pop(3)
                        ha.insert(3, amou)
                        for q in ha:
                            cret += q + " "
                        fp.write(cret + "\n")
                        print(f"    **Transaction Successful!")
                        print(f"    *Rs.{sendAmt} is transferd from Your Account.")
                        print(f"     Now, Your Remaining Balace is Rs.{ha[3]}.")
                        out = ''
                        break
                    else:
                        out = 'No such Account Found!'
            else:
                out = 'Wrong PIN!'
            break
        else:
            out = 'No such Account Found!'
    print(out)
# =====================All User===============================
def viewUser(fp):
    print("------------------------------------------")
    print("Sr.No     Name         Age        Balance")
    print("------------------------------------------")
    fp.seek(0, 0)
    data = list(enumerate(fp.readlines()))
    comp = 1111
    fp.seek(0, 0)
    q = fp.readlines()
    for a in q:
        last = int(a.strip().split()[1])
        if last > comp:
            comp = last
    aNo = []
    for x in range(1111,comp+1):
        aNo.append(x)
    fp.seek(0,0)
    data = list(enumerate(fp.readlines()))
    for o in range(len(aNo)):
        for a in range(data[-1][0],-1,-1):
            if int(data[a][1].strip().split()[1])==aNo[o]:
                print(data[a][1].strip().split()[1]+"   "+data[a][1].strip().split()[0].upper().center(12) +
                      " " + data[a][1].strip().split()[2].center(10) +
                      "    " + data[a][1].strip().split()[3])
                break

    print(" ")
# =====================Clear Console==========================
import os
clear = lambda : os.system("cls")

def consoleClear():
    hp = True
    while hp:
        print(" ")
        exit = input("Press 'y' for Main Menu : ")
        if exit == 'y':
            clear()
            hp = False
        else:
            print("Wrong!")
# =====================Message On Phone========================

def message(number,msg1,msg2):
    account_sid = '---TwilioID----------'
    auth_token = '---TwilioToken--------'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='--TwilioPhoneNumber',
        to = number,
        body= msg1 + "\n" + msg2 + u'\U0001f680'
    )


# =====================Main Funtion ===========================
# import getpass
from twilio.rest import Client
fp = open("one.txt","a+")
print(" ")
fp.seek(0,0)
AccountNum = 1111
AccountCounter = 0
quit = True
while quit:
    clear()
    print("\n                               Welcome to MyBanking")
    print("--------------------------------------------------------------------------------")
    menu()
    opt = int(input("\nEnter Your Option : "))
    print(" ")
    if opt==1:
        AccountCounter += 1
        addAccount(fp)
        consoleClear()
    elif opt==2:
        checkAccount(fp)
        consoleClear()
    elif opt==3:
        withDraw(fp)
        consoleClear()
    elif opt==4:
        deposite(fp)
        consoleClear()
    elif opt==5:
        transfer(fp)
        consoleClear()
    elif opt==6:
        viewUser(fp)
        consoleClear()
    elif opt==7:
        quit=False
    else:
        print("Invalid Selection!")


