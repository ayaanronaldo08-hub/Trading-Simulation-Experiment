def human_decision(price, cash, shares): #function to prompt user for their decision
    action = input("Do you wish to BUY, SELL, or HOLD: ") #asks for one of the three decisions
    action = action.strip() #gets rid of any unwanted spaces
    action = action.upper() #turns the input into capital so it is always the same

    while action != "BUY" and action != "SELL" and action != "HOLD": #check if user gives valid decision
        #the while loop condition basically says it will run if the input from the user doesnt match any of the allowable deicisons
        #if the given input is ANY of the allowed decisions the condition will evaluate to false and the loop does not run
        #Ex(Loop WILL RUN): action = "hi"
        #Ex(Loop WILL NOT RUN): action = "BUY"
        action = input("Do you wish to BUY, SELL, or HOLD: ") #asks for one of the three decisions
        action = action.upper() #turns the input into capital so it is always the same

    if (action == "BUY"): 
        quantity = input("How many shares do you wish to BUY(ENTER AN INTEGER BIGGER THAN OR EQUAL TO 0): ") #asks for the number of shares that will be used to either BUY or SELL
        while True: #creates infinite loop that runs until 'return' function escapes it
            try: #makes sure the quantitiy variable is an integer
                quantity = int(quantity)#turns the string we got from input into an integer
            except ValueError: #asks again if quantity can't be turned into an integer
                quantity = input("How many shares do you wish to BUY(ENTER AN INTEGER BIGGER THAN OR EQUAL TO 0): ") #asks for the number of shares that will be used to either BUY or SELL
            else: #runs if quantity is a valid integer
                if quantity < 0: #checks if quantity is negative
                    quantity = input("Please enter an integer greater than or equal to 0:") #asks for a number greater than or equal to 0
                    continue #restarts loop
                if quantity == 0: #checks if user doesn't want to buy and exits loop
                    return action, quantity
                if cash < price*quantity: #checks if user can afford it
                    quantity = input("You cannot afford this many shares, enter an amount you can afford with the cash you have: ") #asks for a quantity that the user can afford
                    continue #restarts loop
                else: #if quantity is greater than or equal to 0 and the user can afford it
                    return action, quantity #returns the action(BUY) and the quantity
                
    elif (action == "SELL"):
        quantity = input("How many shares do you wish to SELL(ENTER AN INTEGER BIGGER THAN OR EQUAL TO 0): ") #asks for the number of shares user wants to sell
        while True: #creates infinite loop that runs until 'return' function escapes it
            try: #makes sure the quantitiy variable is an integer
                quantity = int(quantity)#turns the string we got from input into an integer
            except ValueError: #asks again if quantity can't be turned into an integer
                quantity = input("How many shares do you wish to SELL(ENTER AN INTEGER BIGGER THAN OR EQUAL TO 0): ") #asks for the number of shares user wants to sell
            else: #runs if quantity is a valid integer
                if quantity < 0: #checks if quantity is negative
                    quantity = input("Please enter an integer greater than or equal to 0:") #asks for a number greater than or equal to 0
                    continue #restarts loop
                if quantity == 0: #checks if user doesn't want to sell and exits loop
                    return action, quantity
                if quantity > shares: #checks if user can sell shares
                    quantity = input("You do not have enough shares to sell, enter an amount you can sell based on how many shares you hold: ") #asks for a quantity that the user is able to sell. Ex: can't sell 4 shares if you only own 3
                    continue #restarts loop
                else: #if quantity is greater than or equal to 0 and the user can afford it
                    return action, quantity #returns the action(SELL) and the quantity
                
    else: #following code runs if user wishes to hold
        quantity = 0 #quantity is 0 because user isn't buying or selling
        return action, quantity #returns the action(hold) and quantity(0)
