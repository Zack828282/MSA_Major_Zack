# Asking the user for their two inputs
# Defining obtain_user_daily_hours
def obtain_user_daily_hours():
    while (True):
        try:
            User_daily_hours = float(input("How many hours do you work every day? \n"))
            # Making sure input isn't above 24 or below 0
            if User_daily_hours > 24:
                print("Please enter a possible value \n")
                continue
            if User_daily_hours < 0:
                print("Please enter a possible value \n")
                continue
            break
        # Making sure a number is entered
        except:
            print("Please enter a numerical value \n")
        continue
            # Allowing other fucntions to pull User_daily_hours
    return User_daily_hours
# Defining obtain_user_hourly_wage
def obtain_user_hourly_wage():
    while (True):
        try:
            User_hourly_wage = float(input("What is your hourly wage? \n"))
            # Making sure input is positive
            if User_hourly_wage < 0:
                print("Please enter a possible value \n")
                continue
            break
        # Making sure a number is entered
        except:
            print("Please enter a numerical value \n")
            continue
    return User_hourly_wage
# Defining a function to print results
def Final_printer():
    User_daily_hours = obtain_user_daily_hours()
    User_hourly_wage = obtain_user_hourly_wage()
    Yearly_income_pretax = User_daily_hours * User_hourly_wage * 350
    Tax_takings = Yearly_income_pretax * 0.12
    Gross_annual_income = Yearly_income_pretax -Tax_takings
    

    print("Pay Advice\n-------------")

    print(f"Hours worked a day: {User_daily_hours:.2f} \n")
          
    #print(f"Hours worked all year: {Hours_all_year:.2f} \n")

    print(f"Hourly wage: {User_hourly_wage:.2f} \n")

    print(f"Yearly income before tax: {Yearly_income_pretax:.2f} \n")

    print(f"Taxes: {Tax_takings:.2f} \n")

    print(f"Gross annual income: {Gross_annual_income:.2f} \n")
# Printing
Final_printer()