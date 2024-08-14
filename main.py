# Class ATM Machine
class Atm:
  def __init__(self):
    self.__pin = None
    self.__balance = 0
    self.__menu() # calls the menu when creating object

  def __menu(self):
    
    while True:
      # Menu Options
      print()
      print("----------------------------------------------------------------------")
      print("Menu: ")
      print("1. Generate a PIN")
      print("2. Change your PIN")
      print("3. Check your balance")
      print("4. Withdraw money")
      print("5. Deposit money")
      print("6. Exit")
    
      option = input("Please enter your choice: ")
      print()

      if option == "1":
        self.__generate_pin()
      elif option == "2":
        self.__change_pin()
      elif option == "3":
        self.__check_balance()
      elif option == "4":
        self.__withdraw()
      elif option == "5":
        self.__deposit()
      elif option == "6":
        print("Thank you for using our ATM!")
        break
      else:
        print("Invalid option, please choose one from the menu.")

  # Returns the PIN
  def __get_pin(self):
    pin = input("Enter a 4 digit PIN: ")
    return pin
  
  # Verifies if the PIN is the same, returns T/F
  def __verify_pin(self, entered_pin):
    verify_pin = input("Enter your current PIN to verify: ")
    if(entered_pin == verify_pin):
      print("\nYour PIN has been verfied")
      return True
    else:
      print("Incorrect PIN enetered. Please try again.")
      return False

  # Generates a 4 digit PIN and verifies it
  def __generate_pin(self):
    if self.__pin is not None: # checking if self.__pin already has a value
      print("Your PIN has already been set. You will be redirected to the menu.")
      self.__menu()
    else:
      pin = self.__get_pin()
      if(self.__verify_pin(pin)):
        print("Congrats, you have generated a new PIN.")
        self.__pin = pin # sets pin to variable
      else:
        print("\nThere is an error. Your PIN dosen't match.")

  # Changes the PIN, updates the __pin variable
  def __change_pin(self):
    old_pin = input("Enter your old pin to verify: ")
    # checking if pin entered is correct
    if old_pin == self.__pin:
      new_pin = input("Enter a new 4 digit PIN: ")
      new_pin_2 = input("Enter it again: ")
      if(new_pin == new_pin_2):
        print("Your PIN has been changed.")
        self.__pin = new_pin # updating the pin
      else:
        print("Your PINS don't match. Please try again.")
    else:
      print("Your old PIN is incorrect. Please try again.")

  # Checks the balance
  def __check_balance(self):
    check_balance_pin = input("Please input your PIN to check your balance: ")
    if check_balance_pin == self.__pin:
      print("Your balance is: $", self.__balance)
    else:
      print("Your PIN is incorrect. Please try again.")

  # Withdraws money
  def __withdraw(self):
    withdraw_pin = input("Please input your PIN to withdraw money: ")
    # verifying the pin is correct before withdrawing
    if withdraw_pin == self.__pin:
      withdrawl_money = int(input("Input the amount you want to withdraw in hundreds: "))
      
      # checking if the amount is a multiple of 100 and if there's a sufficient balance
      if withdrawl_money < self.__balance and withdrawl_money%100 == 0:
        self.__balance -= withdrawl_money
        print("You have successfully withdrawn $", withdrawl_money)
      else:
        print("Insufficient balance or invalid amount. Please try again.")
    else:
      print("Your PIN is incorrect. Please try again.")

  # Deposits money
  def __deposit(self):
    deposit_pin = input("Please input your PIN to deposit money: ")
    # verifying the pin is correct before depositing
    if deposit_pin == self.__pin:
      deposit_money = int(input("Input the amount you want to deposit in hundreds: "))

      # checking if the amount is a multiple of 100 and if it's positive
      if deposit_money%100 == 0 and deposit_money > 0:
        self.__balance += deposit_money
        print("You have successfully deposited $", deposit_money)
      else:
        print("Invalid amount. Please try again.")
    else:
      print("Your PIN is incorrect. Please try again.")


# Main
print("Welcome to the ATM Machine!")
name = input("Please enter your name: ")
print("\nHello", name,"! What would you like to do today?")

new_ATM = Atm() # creating ATM object