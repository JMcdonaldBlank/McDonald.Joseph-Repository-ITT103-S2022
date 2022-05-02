"""
Author: Joseph McDonald
Date Created: 04/30/2022
Course: ITT103
Purpose: This Python code is made to solve a company's problem. JamEx Limited
requires a program to calculate and print the commission received by a
salesperson. 

JamEx Limited requires a program to calculate and print the commission received by a
salesperson. The program should process an undetermined number of salespersons and
appropriately terminate by a predefined input. The commission rate is based on two factors,
the amount of sales and the class to which a salesperson belongs. The input will be the
salesperson number, sales amount and class. The commission rate will be based on the
following criteria:

Class=1
If sales is equal to or less than $1000, the rate is 6 percent.
If sales is greater than $1000 but less than $2000, the rate is 7 percent.
If the sales is $2000 or greater, the rate is 10 percent.

Class = 2
If the sales is less than $1000, the rate is 4 percent.
If the sales is $1000 or greater, the rate is 6 percent.

Class = 3
The rate is 4.5 percent for all sales amount
Class= any other value
Output an appropriate error message.
"""

class1_a = 0.06 # if sales is equal to or less than $1000, the rate is 6 percent.
class1_b = 0.07 # if sales is greater than $1000 but less than $2000, the rate is 7 percent.
class1_c = 0.10 # if the sales is $2000 or greater, the rate is 10 percent.
class2_a = 0.04 # if the sales is less than $1000, the rate is 4 percent.
class2_b = 0.06 # if the sales is $1000 or greater, the rate is 6 percent.
class_3 = 0.045 # the rate is 4.5 percent for all sales amount.
commission = 0  #For initialization
NoneType= ''

def output(number, salesclass, amount, rate):   

    """
    This is a function that outputs the salesperson's commission rate and other
    important information. The commission rate is also rounded to two decimal
    places.
    """
    print("*______________________________________________*")
    print("\nSalesperson Number: " +str(number))
    print("Class: " + str(salesclass))
    print("Sales Amount: $" + str(amount))
    print("Commission: $" + str(round(rate, 2)))
    print("\n*______________________________________________*")

while True:
    while True: # loop created to continue or stop the program.
        end_func = input("If you wish to end the progaram, enter Stop. To continue, enter c: ")
        if end_func == 'c' or end_func == 'C':
            break           
        elif end_func == 'Stop' or end_func == 'stop':
            print("The program has stopped.")
            break
        else:
            print("Input invalid!, Plese try again.\n")
    
    if end_func == 'Stop' or end_func == 'stop':
        break # this will break out of the outermost loop if stop is entered.
    
    print("\nWelcome to JamEx Limited company commision program!")
    
    while True:
        try:
            salesperson_num = int(input("\nPlease enter salesperson\'s number: "))
        except ValueError:
            print("Invalid information! Please enter a valid salesperson number.")
            # Because of the incorrect input, it will return to the begging of the loop.
            continue
        if salesperson_num < 0 or str(''):
          print("No input detected! Please try again.")
        else:
            # The sales data was successfully analyzed! get out of the loop
            break 
      
    while True:
        try:
            sales_amount = int(input("\nPlease enter sales amount: "))
        except ValueError:
            print("Invalid data! Please type a number in the box below.")
            # Because of the incorrect input, it will return to the begging of the loop.
            continue
        if sales_amount < 0 or str(''):
          print("No valid input detected! Please try again.")
        else:
            # The sales data was successfully analyzed! get out of the loop
            break 

    while True:
        try:
            salesman_class = int(input("\nPlease enter the class: "))      
        except ValueError:
            print("Invalid data! Please try once more.")
            # Because of the incorrect input, it will return to the begging of the loop.
            continue
        if salesman_class < 1 or salesman_class > 3:
            print("Just one value is required! Please enter 1, 2, or 3.")  
        else:    
            # The sales data was successfully analyzed! get out of the loop
            break
        
    if salesman_class == 1:
        if sales_amount <= 1000:
            commission = class1_a * sales_amount
            
        elif sales_amount > 1000 and sales_amount < 2000:
            commission = class1_b * sales_amount
            
        elif sales_amount >= 2000:
            commission = class1_c * sales_amount

    if salesman_class == 2:
        if sales_amount < 1000:
            commission = class2_a * sales_amount
            
        elif sales_amount >= 1000:
            commission = class2_b * sales_amount

    if salesman_class == 3:
        commission = class_3 * sales_amount
    
    output(salesperson_num, salesman_class, sales_amount, commission)
    print("Program complete!")
    print("Thank you for your service!")
