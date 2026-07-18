def execute_trade(price, cash, shares, action, quantity): #the function to execute trade and update user portfolio 
    #function parameter explanation(below)
        #price: The current stock price, cash: The amount of cash user has, 
        #shares: The amount of shares the user holds, action: BUY, SELL, or HOLD, 
        #amount_of_shares: The amount of shares that will be affected
    if action == "BUY": #following statements will run if user wishes to buy
        shares += quantity #updates shares by how many the user wanted to buy
        cash -= price*quantity #updates cash by how much the user spent
        return shares, cash #returns the updated shares and cash
    elif action == "SELL": #following code will run if user wishes to SELL
        shares -= quantity #updates shares by how many the user wanted to sell
        cash += price * quantity #updates cash by how much cash the user earned by selling
        return shares, cash #returns the updated shares and cash
    else: #runs if user chose to hold
        return shares, cash  #returns standards shares and cash because nothing is being sold or bought