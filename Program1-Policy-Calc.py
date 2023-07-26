# Program Description:     A program to enter and calculate insurance policy info for One Stop Insurance
# Written by:              Bradley Hiscock
# Written on:              July 26/2023

# ********** CONSTANTS **************************

# ********** Imported Libraries *****************

import datetime
import FormatValues
import time
from tqdm import tqdm

# ********** Open the OSICDef.dat file **********

f = open('OSICDef.dat', 'r')
policyNum = int(f.readline())
basicRate = float(f.readline())
addAutoRate = float(f.readline())
exLiaRate = float(f.readline())
glassCoverRate = float(f.readline())
loanerRate = float(f.readline())
hstRate = float(f.readline())
processFee = float(f.readline())

# ********** Defined Functions ******************

# ********** Main Program ***********************
# ---------- Inputs -------------
while True:

    custFirst = input("Enter the customer's first name: ").title()
    custLast = input("Enter the customer's last name: ").title()
    custAdd = input("Enter the customer's address: ").title()
    custCity = input("Enter the city: ").title()

    allowedProv = ["NL", "NB", "PE", "NS"]
    while True:
        custProv = input("Enter the customer's province: ").upper()
        if custProv not in allowedProv:
            print("Error - Customer's province must be NL, NB, PE, or NS.")
        else:
            break

    while True:
        allowed_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        allowed_numbers = set("0123456789")
        custPostal = input("Enter the customer's postal code (L0L0L0): ").upper()

        if custPostal == "":
            print("Error - Postal code cannot be blank.")
        elif len(custPostal) != 6:
            print("Error - Postal code must be 6 characters.")
        elif not set(custPostal[0]).issubset(allowed_letters):
            print("Error - First character in postal code must be a letter (L0L0L0).")
        elif not set(custPostal[2]).issubset(allowed_letters):
            print("Error - Third character in postal code must be a letter (L0L0L0).")
        elif not set(custPostal[4]).issubset(allowed_letters):
            print("Error - Fifth character in postal code must be a letter (L0L0L0).")
        elif not set(custPostal[1]).issubset(allowed_numbers):
            print("Error - Second character in postal code must be a number (L0L0L0).")
        elif not set(custPostal[3]).issubset(allowed_numbers):
            print("Error - Fourth character in postal code must be a number (L0L0L0).")
        elif not set(custPostal[5]).issubset(allowed_numbers):
            print("Error - Sixth character in postal code must be a number (L0L0L0).")
        else:
            break

    custPhone = input("Enter customer's phone number (##########): ")
    custPhoneDsp = f"1+({custPhone[0:3]}){custPhone[3:6]}-{custPhone[6:]}"

    numCars = int(input("Enter the number of cars being insured: "))

    while True:
        exLiability = input("Is extra liability applicable? (Y/N): ").upper()
        if exLiability != "Y" and exLiability != "N":
            print("Error - Extra liability must be Y or N.")
        else:
            break

    while True:
        glassCoverage = input("Does customer need the optional glass coverage? (Y/N): ").upper()
        if glassCoverage != "Y" and glassCoverage != "N":
            print("Error - Optional glass coverage must be Y or N.")
        else:
            break

    while True:
        optLoaner = input("Does customer need the optional loaner car? (Y/N): ").upper()
        if optLoaner != "Y" and optLoaner != "N":
            print("Error - Optional loaner must be Y or N.")
        else:
            break

    payPlansLst = ["Full", "Monthly"]
    while True:
        payPlan = input("Enter customer's payment plan (Full/Monthly): ").title()
        if payPlan not in payPlansLst:
            print("Error - Payment plan must be either Full or Monthly.")
        else:
            break

    # -------------- Calculations ------------------

    insPremium = basicRate + ((basicRate - basicRate * addAutoRate) * (numCars - 1))

    if exLiability == "Y":
        liaCost = exLiaRate * numCars
    else:
        liaCost = 0

    if glassCoverage == "Y":
        glassCost = glassCoverRate * numCars
    else:
        glassCost = 0

    if optLoaner == "Y":
        loanerCost = loanerRate * numCars
    else:
        loanerCost = 0

    totExtras = liaCost + glassCost + loanerCost
    subTot = insPremium + totExtras
    HST = subTot * hstRate
    total = subTot + HST
    monPayment = (total + processFee) / 8

    invDate = datetime.datetime.now()
    nextPay = (invDate.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)

    # ------------------------- Display -----------------------------------

    print()
    print(f"                       One Stop Insurance Co.")
    print(f"                            Policy Info")
    print()
    print(f"                                             Date:         {FormatValues.FDateM(invDate)}")
    print(f"                                             Next Payment: {FormatValues.FDateM(nextPay)}")
    print()
    print(f" {custFirst} {custLast}")
    print(f" {custAdd:<20s}                        Number of rentals: {numCars}")
    print(f" {custCity}, {custProv}, {custPostal}")
    print(f" {custPhoneDsp}                             Insurance Premium: {FormatValues.FDollar2(insPremium):>9s}")
    print(f"                                             Optional Costs: ")
    print(f" Policy #: {policyNum:<4}                               Extra Liability:  {FormatValues.FDollar2(liaCost):>9s}")
    print(f"                                              Glass Coverage:   {FormatValues.FDollar2(glassCost):>9s}")
    print(f"                                              Loaner Car(s):    {FormatValues.FDollar2(loanerCost):>9s}")
    print(f"                                                                ---------")
    print(f"                                              Total Extras:     {FormatValues.FDollar2(totExtras):>9s}")
    print()
    print(f"                                             Subtotal:          {FormatValues.FDollar2(subTot):>9s}")
    print(f"                                             HST:               {FormatValues.FDollar2(HST):>9s}")
    print(f"                                                                ---------")
    print(f"                                             Total:             {FormatValues.FDollar2(total):>9s}")
    print(f"                                             Monthly Payment:   {FormatValues.FDollar2(monPayment):>9s}")
    print()
    print(f"            Thank you for choosing One Stop Insurance Co.!")
    # Save policy info to Policies.dat
    print()
    print("Saving data to Policies.dat ...")

    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)

    f = open("Policies.dat", "a")
    f.write(f"{str(policyNum)}, ")
    f.write(f"{FormatValues.FDateS(invDate)}, ")
    f.write(f"{str(custFirst)}, ")
    f.write(f"{str(custLast)}, ")
    f.write(f"{str(custAdd)}, ")
    f.write(f"{custCity}, ")
    f.write(f"{custProv}, ")
    f.write(f"{custPostal}, ")
    f.write(f"{custPhoneDsp}, ")
    f.write(f"{numCars}, ")
    f.write(f"{exLiability}, ")
    f.write(f"{glassCoverage}, ")
    f.write(f"{optLoaner}, ")
    f.write(f"{payPlan}, ")
    f.write(f"{total}\n")
    f.close()

    print("Data successfully saved!")
    policyNum += 1
    time.sleep(1)

    Continue = input("Would you like to enter another policy? (Y/N): ").upper()
    if Continue == "N":
        f = open("OSICDef.dat", "w")
        f.write(f"{str(policyNum)}\n")
        f.write(f"{str(basicRate)}\n")
        f.write(f"{str(addAutoRate)}\n")
        f.write(f"{str(exLiaRate)}\n")
        f.write(f"{str(glassCoverRate)}\n")
        f.write(f"{str(loanerRate)}\n")
        f.write(f"{str(hstRate)}\n")
        f.write(f"{str(processFee)}\n")
        break
    else:
        pass
