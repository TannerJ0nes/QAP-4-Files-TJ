# QAP 4 Program for Matplotlib
# Author: Tanner Jones
# Written: March 22nd,2023

# Import Statements
import calendar
import matplotlib.pyplot as plt

x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
y_axis = []

# User input to select the current month in the financal year. Once year is reached auto enters 0's to avoid having
# user enter multiple 0s
while True:
    try:
        curr_month = int(input("Please enter the current month as a number(1-12): "))
    except:
        print("Please enter a valid number")
    else:
        if curr_month < 1 or curr_month > 12:
            print("Please enter a valid month between 1 and 12") # validations to ensure no incorrect numbers entered
        else:
            break

for i in range(1, 13):

    if i <= curr_month:
        while True:
            # using calandar library to display each months full name at end of input statement
            try:
                sales_amount = int(input("Enter the total sales for {}: ".format(calendar.month_name[i])))
            except:
                print("Please enter a valid number") # validations to ensure correct amounts entered for sales
            else:
                if sales_amount < 0:
                    print("Please enter a positive number")
                else:
                    break
        y_axis.append(sales_amount)
    else:
        y_axis.append(0)


bar_graph = plt.bar(x_axis, y_axis)
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.title("Sales for current financial year")

plt.show()