# do a test for if they enter an empty string
# make sure they add a user before doing anything else

class Property():
    def __init__(self, property_name= None):
        self.property_name = property_name
        self.total_income = 0
        self.total_expenses = 0
        self.total_investments = 0
        self.total_roi = 0
        self.cashFlow = 0
        self.user_portfolio = []

    def assign_property_name(self):
        response = input('Please enter the name of your property. ')
        self.property_name = response
        print(f'You have added {self.property_name.title()} to your portfolio. ')
        self.user_portfolio.append("Property Name: " + self.property_name.title())

    def income_info(self):
        running = True
        while running == True:
            response = input("Enter an income amount for this property or enter 'Q' to quit. ")
            if response.lower() != 'q':
                self.total_income += float(response)
                print(f"${self.total_income} has been added as your total income for this property. ")

            else:
                print(f"${self.total_income} has been added as your total income for this property. ")
                running = False
                break
        self.user_portfolio.append(f"Total property income: ${self.total_income}")

    def expenses_info(self):
        done = False
        while not done:
            response = input("Enter an expense amount for this property or enter 'Q' to quit. ")
            if response.lower() != 'q':
                self.total_expenses += float(response)
                print(f"${self.total_expenses} has been added as your total expense amount for this property. ")
            else:
                print(f"${self.total_expenses} has been added as your total expense amount for this property. ")
                done = True
                break
        self.user_portfolio.append(f"Total expenses for this property: ${self.total_expenses}")
    def cash_flow(self):
        self.cashFlow = float(self.total_income) - float(self.total_expenses)
    def get_investment(self):
        done = False
        while not done:
            investment = input("Enter investment amount for this property or enter 'Q' to quit. ")
            if investment.lower() != "q":
                self.total_investments += float(investment)
                print(f"${self.total_investments} has been added as your total investment for this property. ")
            else:
                print(f"${self.total_investments} has been added as your total investment for this property. ")
                done = True
                break
        self.user_portfolio.append(f"Total investment for this property: ${self.total_investments}")    
    def calculate_roi(self):
        annual_cash_flow = float(self.cashFlow * 12)
        roi = annual_cash_flow/float(self.total_investments)
        self.total_roi = roi * 100
        print(f"Your ROI for this property is {self.total_roi}%")
        self.user_portfolio.append(f"ROI for this property:{self.total_roi}%")
    


class User(Property):
    def __init__(self, user_name = None):
        super().__init__()
        self.user_name = user_name
        self.users= {}
    def define_user(self):
        self.user_name = input("Enter your user name ").title()
        self.users[self.user_name] = []
    def menu_options(self):
        done = False
        while not done:
            menu = ("""
            [1] Add user
            [2] Add new property
            [3] View portfolio
            [4] Modify property
            [5] Delete Property
            [6] Switch User
            [7] Exit
            """)
            print(menu)
            choices = input(f"What would you like to do? ")
            if choices == "1":
                self.define_user()
            if choices == "2":
                myProperty = Property() 
                myProperty.assign_property_name()
                myProperty.income_info()
                myProperty.expenses_info()
                myProperty.cash_flow()
                myProperty.get_investment()
                myProperty.cash_flow()
                myProperty.calculate_roi()
                self.users[self.user_name].append(myProperty)
            if choices == "3":
                if len(self.users[self.user_name]) == 0:
                    print("You have no properties in your portfolio. ")
                else:
                    for i in range(0, len(self.users[self.user_name])):
                        print("Property Name: " + self.users[self.user_name][i].property_name.title())
                        print("Total Investment: $" + str(self.users[self.user_name][i].total_investments))
                        print("Total Income: $"+ str(self.users[self.user_name][i].total_income))
                        print("Total Expenses: $"+ str(self.users[self.user_name][i].total_expenses))
                        print(f"ROI for this property: {self.users[self.user_name][i].total_roi}%")
            if choices == "4":
                done = False
                while not done:
                    for i in range(0, len(self.users[self.user_name])):
                        print("[" + str(i) + "] : " + self.users[self.user_name][i].property_name.title())
                    choice = input(f"What property would you like to change? ")
                    modify = input("What would you like to change? Enter 'property name', 'income', 'expenses', 'investments' or 'quit'. ").lower()
                    if modify == "property name":
                        new_name = input("What would you like to change the name to? ")
                        self.users[self.user_name][int(choice)].property_name = new_name.title()
                    if modify == "income":
                        new_income = input("Enter new income amount. ")
                        self.users[self.user_name][int(choice)].total_income = new_income
                        self.users[self.user_name][int(choice)].cash_flow()
                        self.users[self.user_name][int(choice)].calculate_roi()
                    if modify == "expenses":
                        new_expenses = input("Enter new expense amount. ")
                        self.users[self.user_name][int(choice)].total_expenses = new_expenses
                        self.users[self.user_name][int(choice)].cash_flow()
                        self.users[self.user_name][int(choice)].calculate_roi()
                    if modify == "investments":
                        new_investments = input("Enter new investment amount. ")
                        self.users[self.user_name][int(choice)].total_investments = new_investments
                        self.users[self.user_name][int(choice)].cash_flow()
                        self.users[self.user_name][int(choice)].calculate_roi()
                    if modify == "quit":
                        done = True
                        self.menu_options()
            if choices == "5":
                for i in range(0, len(self.users[self.user_name])):
                    print("[" + str(i) + "] : " + self.users[self.user_name][i].property_name.title())
                delete = input("Enter property number that you would like to delete. ")
                del(self.users[self.user_name][int(delete)])
            if choices == "6":
                self.user_name = input("Enter username that you would like the view. ").title()
                self.menu_options
            if choices == "7":
                print("Thank you for using ROI calculator. ")
                done = True
                break




if __name__== "__main__":      
    my_user = User()
    my_user.menu_options()



































        