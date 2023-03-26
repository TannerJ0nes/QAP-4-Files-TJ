# QAP 4 Program for ONE STOP INSURANCE COMPANY
# Author: Tanner Jones
# Written: March 20th,2023

# Import Statements
import datetime
import time

# Constants Read from OSICDef.dat file
f = open('OSICDef.dat', 'r')

POLICY_NUM = int(f.readline())
BASIC_PREM_RATE = float(f.readline())
ADD_DISCOUNT_RATE = float(f.readline())
EXTRA_LIABILITY_RATE = float(f.readline())
GLASS_COV_RATE = float(f.readline())
LOANER_RATE = float(f.readline())
HST_RATE = float(f.readline())
MON_PRO_FEE = float(f.readline())

f.close()

# Validation List
valid_province = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "NV", "NW", "YK"]

# Fun with time library
print("Welcome to ONE STOP INSURANCE COMPANY POLICY SYSTEM")
time.sleep(1.5)
print("Please STANDBY as files load and system's initalize's")
time.sleep(1.5)
print(".")
time.sleep(1.5)
print("..")
time.sleep(1.5)
print("...")
time.sleep(1)
print("System's Ready!")
time.sleep(1)

# Start of main program in loop to allow multiple entries. All with validations

while True:

    while True:
        first_name = input("Please Enter Customer's First Name: ").title()
        if first_name == "":
            print("ERROR First name cannot be empty, Please re-enter")
        else:
            break

    while True:
        last_name = input("Enter Customer Last Name: ").title()
        if last_name == "":
            print("ERROR Last name cannot be empty, Please re-enter")
        else:
            break

    while True:
        Street_address = input("Enter Street Address: ").title()
        if Street_address == "":
            print("ERROR Street address cannot be empty, Please re-enter")
        else:
            break

    while True:
        city = input("Enter Customer City: ").title()
        if city == "":
            print("ERROR City cannot be empty, Please re-enter")
        else:
            break

    while True:
        province = input("Enter Province (XX): ").upper()
        if len(province) != 2:
            print("ERROR Please re-enter province as (XX)")
        elif province == "":
            print("ERROR Province field cannot be empty, Please re-enter")
        elif not province in valid_province:
            print("ERROR Please enter a valid province of Canada")
        else:
            break

    while True:
        postal_code = input("Enter Postal Code (A0A 0A0): ").upper()
        if postal_code[3] != " ":
            print("ERROR Please include a space between postal code")
        elif len(postal_code) != 7:
            print("ERROR Please enter postal code as: A0A 0A0")
        else:
            break

    while True:
        phone_num = input("Enter Phone number (Without Spaces):")

        if len(phone_num) != 10:
            print("Please format phone number as 10 digits without spaces")
        elif not phone_num.isdigit():
            print("Please enter a valid phone number")
        else:
            formatted_phone_num = phone_num[:3] + "-" + phone_num[3:6] + "-" + phone_num[6:]
            break

    while True:
        try:
            number_cars = int(input("Number of cars customer want's to insure: "))
        except:
            print("Please enter a valid number.")
        else:
            if number_cars < 1:
                print("Please enter a number greater than 1.")
            else:
                break

    while True:
        extra_insurance = input("Would customer like to purchase extra insurance (Y/N): ").upper()
        if extra_insurance == "Y" or extra_insurance == "N":
            break
        else:
            print("Please select Y for yes, or N for no")

    while True:
        glass_coverage = input("Would customer like to purchase additional glass coverage (Y/N): ").upper()
        if glass_coverage == "Y" or glass_coverage == "N":
            break
        else:
            print("Please select Y for yes, or N for no")

    while True:
        loaner_car = input("Would customer like to purchase additional loaner car coverage (Y/N): ").upper()
        if loaner_car == "Y" or loaner_car == "N":
            break
        else:
            print("Please select Y for yes, or N for no")

    while True:
        pay_method = input("Would the customer like to pay in monthly or yearly installments (M/Y) ").upper()
        if pay_method == "M" or pay_method == "Y":
            break
        else:
            print("Please select M for Monthly, or Y for Yearly")

    if pay_method == "M":
        payment_text = "Monthly"
    else:
        payment_text = "Yearly"

    today = datetime.date.today()
    first_payment = datetime.date(today.year, today.month + 1, 1)
    first_car = BASIC_PREM_RATE
    add_cars = ((number_cars - 1) * BASIC_PREM_RATE) * (1 - ADD_DISCOUNT_RATE)
    basic_prem = first_car + add_cars

    if extra_insurance == "Y":
        extra_insurance_cost = number_cars * EXTRA_LIABILITY_RATE
    else:
        extra_insurance_cost = 0

    if glass_coverage == "Y":
        glass_cov_cost = number_cars * GLASS_COV_RATE
    else:
        glass_cov_cost = 0

    if loaner_car == "Y":
        loaner_car_cost = number_cars * LOANER_RATE
    else:
        loaner_car_cost = 0

    # Calculations for output
    extra_costs = extra_insurance_cost + glass_cov_cost + loaner_car_cost
    total_insurance_premium = basic_prem + extra_costs
    hst = HST_RATE * total_insurance_premium
    total_cost = total_insurance_premium + hst

    if pay_method == "M":
        total_cost += MON_PRO_FEE

    # formatting variables for output

    full_name = (f"{first_name} {last_name}")
    dsp_add_car_cost = "${:,.2f}".format(add_cars)
    dsp_first_car_cost = "${:,.2f}".format(BASIC_PREM_RATE)
    dsp_basic_prem = "${:,.2f}".format(basic_prem)
    dsp_extra_insurance_cost = "${:,.2f}".format(extra_insurance_cost)
    dsp_glass_cov_cost = "${:,.2f}".format(glass_cov_cost)
    dsp_loaner_car_cost = "${:,.2f}".format(loaner_car_cost)
    dsp_hst = "${:,.2f}".format(hst)
    dsp_total_cost = "${:,.2f}".format(total_cost)
    dsp_extra_costs = "${:,.2f}".format(extra_costs)
    dsp_MON_PRO_FEE = "${:,.2f}".format(MON_PRO_FEE)
    dsp_monthly_payment = "${:,.2f}".format(total_cost / 8)

    # More Fun with time

    print("All Information entered...generating receipt..please standby...")
    time.sleep(1.5)
    print(".")
    time.sleep(1.5)
    print("..")
    time.sleep(1.5)
    print("...")
    time.sleep(1)
    print("Done!")
    time.sleep(1)

    # Receipt generation
    print()
    print()
    print("-" * 75)
    print("One Stop Insurance Company".center(75))
    print("Insurance Policy Receipt Record".center(75))
    print()
    time.sleep(0.5)
    print(f"Policy Number: {POLICY_NUM}")
    print("-------------------")
    print()
    print(f"Date Created:         {today}")
    print(f"Client Name:          {full_name}")
    print(f"Phone Number:         {formatted_phone_num}")
    print(f"Address:              {Street_address}, {city}, {province} ")
    print(f"                      {postal_code}")
    print("-" * 75)
    time.sleep(0.5)
    print("            Basic Premium")
    print(f"Number of Cars Insured: {number_cars:>2d}")
    print(f"Payment Frequency:       {payment_text:<7s}")
    print("---------------------------------")
    print(f"First Car Cost:           {dsp_first_car_cost:>7s} ")
    print(f"Additional Car Cost:    {dsp_add_car_cost:>9}")
    print(f"Basic Premium Total:   {dsp_basic_prem:>10}")
    print(f"---------------------------------")
    print("            Extra Fees")
    print(f"Extra Liability:       {dsp_extra_insurance_cost:>10}")
    print(f"Glass Coverage:        {dsp_glass_cov_cost:>10}")
    print(f"Loaner Car:            {dsp_loaner_car_cost:>10}")
    print(f"Total Extra Costs:     {dsp_extra_costs:>10}")
    print(f"---------------------------------")
    time.sleep(0.5)
    print("            Totals")
    print(f"HST:                   {dsp_hst:>10}")
    if pay_method == "M":
        print(f"Processing Fee:            {dsp_MON_PRO_FEE:>6}")
    print(f"Total Cost:            {dsp_total_cost:>10}")
    print()
    print("-" * 75)
    if pay_method == "M":
        print(f"Monthly Payment:       {dsp_monthly_payment:>10}")
    else:
        print(f"Yearly Payment:        {dsp_total_cost:>10}")
    print("-" * 75)
    print(f"Next Payment date: {first_payment}")
    print("-" * 75)

    # Opening Policies.dat file to store information from user input
    f = open("Policies.dat", "a")
    # Writing to file with information below
    f.write("{}, ".format(str(POLICY_NUM)))
    f.write("{}, ".format(first_name))
    f.write("{}, ".format(last_name))
    f.write("{}, ".format(Street_address))
    f.write("{}, ".format(city))
    f.write("{}, ".format(province))
    f.write("{}, ".format(postal_code))
    f.write("{}, ".format(formatted_phone_num))
    f.write("{}, ".format(str(number_cars)))
    f.write("{}, ".format(extra_insurance))
    f.write("{}, ".format(glass_coverage))
    f.write("{}, ".format(loaner_car))
    f.write("{}, ".format(pay_method))

    f.write("{}\n".format(str(total_insurance_premium)))
    f.close()

    print()
    print("Policy information processed and saved.")
    print()

    POLICY_NUM += 1

    # closing defaults files

    f = open("OSICDef.dat", 'w')
    f.write("{}\n".format(str(POLICY_NUM)))
    f.write("{}\n".format(str(BASIC_PREM_RATE)))
    f.write("{}\n".format(str(ADD_DISCOUNT_RATE)))
    f.write("{}\n".format(str(EXTRA_LIABILITY_RATE)))
    f.write("{}\n".format(str(GLASS_COV_RATE)))
    f.write("{}\n".format(str(LOANER_RATE)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(MON_PRO_FEE)))
    f.close()

    # asking if want to continue loop
    continue_question = input("Would you like to start another Invoice (Y/N):  ").upper()

    if continue_question == "Y":
        print("Starting new Policy Application...")
        time.sleep(2)
        continue

    else:
        print("Thank you for using ONE STOP INSURANCE COMPANY POLICY SYSTEM")
        time.sleep(1.5)
        print("Please STANDBY as files save and system's shuts down")
        time.sleep(1.5)
        print(".")
        time.sleep(1.5)
        print("..")
        time.sleep(1.5)
        print("...")
        time.sleep(1)
        print("Shutting Down...GOODBYE :)")
        time.sleep(1)
        exit()
