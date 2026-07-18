import random #imports the random module

def price_change(price, sentiment, trend): #the price_change function takes in current price, sentiment of news, and the market trend
    #trend is an integer

    #following code checks if the new is posititve or negative
    if sentiment == "positive": 
        trend += 1 #increases trend by 1 if news is positive
    elif sentiment == "negative":
        trend -= 1 #decreases trend by 1 if news is negative
    else: #if sentiment is neutral it tries and brings the trend value back to 0
         if trend > 0: 
              trend -= 1
         elif trend < 0:
              trend += 1

    #following code keeps the trend value between -5 and 5 so it doesn't keep decreasing or increasing forever
    if trend > 5:
            trend = 5
    elif trend < -5:
            trend = -5

    rand_num_direction = random.randint(1,100) #gives a random number from 1 to 100. Will be used to determine direction of market

    #following code determines if price will go up or down
    #depending on the value of trend, the probabilities of wether the price goes up or down changes
    if trend == 5: 
        if rand_num_direction <= 90: #90% chance
            direction = "Up" 
        else: #10% chance
             direction = "Down"
    elif trend >= 3: #if trend is 3 or 4
        if rand_num_direction <= 70: #70% chance
              direction = "Up"
        else: #30% chance
             direction = "Down"
    elif trend >=1 : #if trend is 1 or 2
        if rand_num_direction <= 55: #55% chance
              direction = "Up"
        else: #45% chance
             direction = "Down"
    elif trend == 0:
        if rand_num_direction <= 50: #50% chance
            direction = "Up"
        else: #50% chance
            direction = "Down"
    elif trend == -5:
        if rand_num_direction <= 90: #90% chance
            direction = "Down"
        else: #10% chance
            direction = "Up"
    elif trend <= -3: #if trend is -4 or -3
        if rand_num_direction <= 70: #70% chance
            direction = "Down"
        else: #30% chance
            direction = "Up"
    elif trend <= -1: #if trend is -2 or -1
        if rand_num_direction <= 55: #55% chance
            direction = "Down"
        else: #45% chance
            direction = "Up"

    rand_num_magnitude = random.randint(1,100) #gives a random number from 1 to 100. Will be used to determine the magnitude of the change in price

    #if market is going to move up
    if direction == "Up":
        if rand_num_magnitude <= 35: #35% chance
              price = price + (price * 0.005) #increase by 0.5%
        elif rand_num_magnitude <= 60: #25% chance
              price = price + (price * 0.01) #increase by 1%
        elif rand_num_magnitude <= 78: #18% chance
              price = price + (price * 0.02) #increase by 2%
        elif rand_num_magnitude <= 90: #12% chance
              price = price + (price * 0.03) #increase by 3%
        elif rand_num_magnitude <= 97: #7 percent chance
              price = price + (price * 0.04) #increase by 4%
        else: #3% chance
              price = price + (price * 0.05) #increase by 5%
    #if market is going to move down
    else: 
        if rand_num_magnitude <= 35: #35% chance
              price = price - (price * 0.005) #decrease by 0.5%
        elif rand_num_magnitude <= 60: #25% chance
              price = price - (price * 0.01) #decrease by 1%
        elif rand_num_magnitude <= 78: #18% chance
              price = price - (price * 0.02) #decrease by 2%
        elif rand_num_magnitude <= 90: #12% chance
              price = price - (price * 0.03) #decrease by 3%
        elif rand_num_magnitude <= 97: #7% chance
              price = price - (price * 0.04) #decrease by 4%
        else: #3% chance
              price = price - (price * 0.05) #decrease by 5%

    return price, trend #returns the updated price and trend value

#price = 100
#trend = 0

#for i in range(500):
    news = generate_news()
    sentiment = news[1]
    price, trend = price_change(price, sentiment, trend)

    print(price)
    print(trend)
  
    






        