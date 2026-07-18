def bot_decision(price, previous_price, cash, shares, price_history): #the function that handles all bot decisions
    #function parameter explanation(BELOW):
    #price: current price of stock, previous_price: the price of stock from the previous day,
    #cash: initial acc balance for bot, shares: the amount of shares the bot has
    #price_history: the price history list

    percent_change = ((price-previous_price)/previous_price) #the percent change of stock price

    avg = 0 #the moving average
    sum = 0 #the sum of all prices in the price_history list
    investment = 0 #the investment the bot will put in the market

    if len(price_history) >= 5: #the moving average will only be caluclated once atleast 5 prices from 5 days have been recorded in the list
        for i in range(len(price_history)-1, len(price_history)-6, -1): #runs the loop from the last element in the list to the 5th to last element decreasing i by 1 every time
            sum += price_history[i] #calculates the sum of all prices from past 5 days
        avg = sum/5 #divides the sum of the last 5 prices by 5 to get 5 day moving average

    #the follow statements determine the momentum of the market
    if percent_change > 0: #if stock price is rising
        momentum = 1
    elif percent_change < 0: #if stock price is falling
        momentum = -1
    else:
        momentum = 0 #if stock price is the same

    #the following statements determine the strength of the momentum
    if 0 <= abs(percent_change) <= 0.005: #if the price has changed 0% to 0.5%
        strength = "none"
    elif 0.005 < abs(percent_change) <= 0.02: #if the price has changed 0.5% to 2%
        strength = "weak"
    elif 0.02 < abs(percent_change) <= 0.04: #if the price has changed 2% to 4%
        strength = "moderate"
    elif 0.04 < abs(percent_change): #if the price has changed more than 4%
        strength = "strong"

    if len(price_history) >= 5: #this code will only run if the length of the price_history list is more than 5
        #the following statements compare the current price to the moving average
        if price > avg: #if the current price is higher than the moving average
            trend = +1
        elif price < avg: #if the current price is lower than the moving average
            trend = -1
        else: #if the current price is equal to the moving average
            trend = 0
    else:
        trend = 0 #if there is not enough data to calculate moving average trend is null
    
    score = momentum + trend #combines momentum and moving-average trend into a single decision score

    # momentum: rising = +1, flat = 0, falling = -1
    # trend: bullish = +1, neutral = 0, bearish = -1

    # possible scores:
    # +2 = strong bullish signal
    # +1 = bullish signal
    #  0 = mixed or neutral signals
    # -1 = bearish signal
    # -2 = strong bearish signal

    if score > 0: #decides the action of the bot based on the score 
        action = "BUY"
    elif score < 0:
        action = "SELL"
    
    if score == 0: #if score is equal to 0 the bot hold
        action = "HOLD"
        quantity = 0
        return action, quantity, "mixed signal" #returns action, quantity, and reason
    
    if strength == "none": #if the momentum has no strength the bot holds
        action = "HOLD"
        quantity = 0
        return action, quantity, "no strength" #returns action, quantity, and reason
    
    if action == "BUY": #following code runs if the bot has decided to buy
        if score == 2: #following code runs if score is 2
            if strength == "weak": #if the strength is weak
                investment = cash * 0.25 #investment is 25% of bot's cash
            elif strength == "moderate": #if the strength is moderate
                investment = cash * 0.5 #investment is 50% of bot's cash
            elif strength == "strong": #if the strength is strong
                investment = cash * 0.75 #investment is 75% of cash

            quantity = int(investment//price) #gives the quantity of shares. Uses // to divide investment by price to always give a whole number. int is used to turn it into an integer value

            if quantity == 0 and cash >= price: #checks if quantity is returned as 0 and bot has enough cash to buy 1 share
                quantity = 1 #quantity is set to 1
            elif quantity == 0 and cash < price: #checks is quantity is returned as 0 and bot does not have enough cash to buy 1 share
                action = "HOLD" #changes the bot action to HOLD
                quantity = 0 #quantity is set to 0 because its a HOLD
                return action, quantity, "insufficient funds" #returns action, quantity, and reason
            return action, quantity, "succesful buy" #returns action, quantity, and reason
        
        elif score == 1: #following code runs if score is 1
            if strength == "weak": #if the strength is weak
                investment = cash * 0.1 #investment is 10% of bot's cash
            elif strength == "moderate": #if the strength is moderate
                investment = cash * 0.25 #investment is 25% of bot's cash
            elif strength == "strong": #if the strength is strong
                investment = cash * 0.5 #investment is 50% of bot's cash

            quantity = int(investment//price) #gives the quantity of shares. Uses // to divide investment by price to always give a whole number. int is used to turn it into an integer value

            if quantity == 0 and cash >= price: #checks if quantity is returned as 0 and bot has enough cash to buy 1 share
                quantity = 1 #quantity is set to 1
            elif quantity == 0 and cash < price: #checks is quantity is returned as 0 and bot does not have enough cash to buy 1 share
                action = "HOLD" #changes the bot action to HOLD
                quantity = 0 #quantity is set to 0 because its a HOLD
                return action, quantity, "insufficient funds" #returns action, quantity, and reason
            return action, quantity, "succesful buy" #returns action, quantity, and reason
    
    if action == "SELL": #following code runs if the bot has decided to sell
        if score == -1: #following code runs if score is -1
            if strength == "weak": #if the strength is weak
                investment = shares * 0.1 #the investment is 10% of the bot's shares
            elif strength == "moderate": #if the strength is moderate
                investment = shares * 0.25 #the investment is 25% of the bot's shares
            elif strength == "strong": #if the strength is strong
                investment = shares * 0.5 #the investment is 50% of the bot's shares
            
            quantity = int(investment//1) #gives the quantity of shares. Uses // to divide investment by 1 to always give a whole number. int is used to turn it into an integer value

            if quantity == 0 and shares > 0: #checks if quantity is returned as 0 and bot has enough shares to sell
                quantity = 1 #sets quantity to 1
            elif quantity == 0 and shares == 0: #checks if quantity is returned as 0 and bot does not have enough shares to sell
                quantity = 0 #quantity is set to 0 because its a HOLD 
                action = "HOLD" #changes bot action to hold
                return action, quantity, "insufficient shares" #returns action, quantity, and reason
            
            return action, quantity, "succesful sell" #returns action, quantity, and reason
        
        elif score == -2: #following code runs if score is -2
            if strength == "weak": #if the strength is weak
                investment = shares * 0.25 #the investment is 25% of the bot's shares
            elif strength == "moderate": #if the strength is moderate
                investment = shares * 0.5 #the investment is 50% of the bot's shares
            elif strength == "strong": #if the strength is strong
                investment = shares * 0.75 #the investment is 75% of the bot's shares
            
            quantity = int(investment//1) #gives the quantity of shares. Uses // to divide investment by 1 to always give a whole number. int is used to turn it into an integer value

            if quantity == 0 and shares > 0: #checks if quantity is returned as 0 and bot has enough shares to sell
                quantity = 1 #sets quantity to 1
            elif quantity == 0 and shares == 0: #checks if quantity is returned as 0 and bot does not have enough shares to sell
                quantity = 0 #quantity is set to 0 because its a HOLD 
                action = "HOLD" #changes bot action to hold
                return action, quantity, "insufficient shares" #returns action, quantity, and reason
            
            return action, quantity, "succesful sell" #returns action, quantity, and reason
                




        

    




   



    

