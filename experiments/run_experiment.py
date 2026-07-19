from engine.news_generator import generate_news #import generate news function from news_generator file
from engine.price_engine import price_change #import price change function from price_engine file
from engine.trade_engine import execute_trade #import execute trade function from trade_engine file
from strategies.human_strategy import human_decision #import human decision function from human_strategy file
from strategies.bot_strategies import bot_decision #import bot decision function from bot_strategies file
from data.logger import log, start_log #imports logging functions from logger file
import random #imports random module
import time #imports time module
import os #imports the os module to interact with the operating system/terminal size

# The get_terminal_width function checks the current size of the user's terminal window.
# os.get_terminal_size().columns dynamically fetches the number of characters that fit horizontally.
# If it fails (e.g., running in certain IDE runners), it defaults to a standard width of 80.
def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80 # Fallback width if terminal size cannot be detected

# Centers text inside the console dynamically based on the current terminal width.
def center(text):
    width = get_terminal_width()
    return str(text).center(width)

random.seed(42) #makes it so everyone who runs this experiment gets the same experiment conditions

price = 100 #initial price of stock
trend = 0 #initial trend value

human_cash = 1000 #initial account balance for human
human_shares = 0 #initial amount of shares held for human

bot_cash = 1000 #initial account balance for bot
bot_shares = 0 #initial amount of shares held for bot
    
name = input("Enter your name: ")
bot_name = "bot"

start_log(name) #creates a new CSV file for this experiment run

price_history = [] #the list containing all prices from every day

for i in range (1,101): #for loop runs 100 times
    # Dynamic terminal width for separators
    term_width = get_terminal_width()
    
    previous_price = price #stores the previous price
    news_tuple = generate_news() #generate_news returns a tuple like this: (news, sentiment)
    news = news_tuple[0] #stores the news from news_tuple
    sentiment = news_tuple[1] #stores the sentiment from news_tuple
    price_change_tuple = price_change(price,sentiment,trend) #stores the new price and trend from price_change function as a tuple like this: (price, trend)
    trend = price_change_tuple[1] #stores the new trend value by grabbing value from price_change_tuple

    price = round(price_change_tuple[0], 2) #sets price to new price by grabbing price from price_change_tuple. Rounds to 2 decimal places

    pre_trade_portfolio_value = round((human_cash + (human_shares * price)), 2) #claculates portfolio value before trade and rounds to 2 decimal places

    # ==========================
    # DAY HEADER DISPLAY
    # ==========================
    # Displays the current day number centered between separator lines
    print("\n" + "=" * term_width)
    print(center(f"DAY {i}/100"))
    print("=" * term_width)

    # ==========================
    # MARKET NEWS DISPLAY
    # ==========================
    # Displays the generated news event centered
    print("\n" + center("MARKET NEWS"))
    print(center(news))

    # ==========================
    # STOCK PRICE DISPLAY
    # ==========================
    # Displays the current stock price centered and rounded to 2 decimals
    print("\n" + center("STOCK PRICE"))
    print(center(f"${price:.2f}"))

    # ==========================
    # HUMAN PORTFOLIO DISPLAY
    # ==========================
    # Displays the user's current cash, shares, and portfolio value
    print("\n" + "-" * term_width)
    print(center("YOUR PORTFOLIO"))
    print("-" * term_width)

    print(center(f"Cash:            ${human_cash:.2f}"))
    print(center(f"Shares Owned:    {human_shares}"))
    print(center(f"Portfolio Value: ${pre_trade_portfolio_value:.2f}"))
    print("-" * term_width)

    bot_pre_trade_portfolio_value = round((bot_cash + (bot_shares * price)), 2) #claculates portfolio value before trade and rounds to 2 decimal places
   
    choice = human_decision(price, human_cash, human_shares) #returns the decision the human wanted in a tuple
    amount_of_shares = choice[1] #accesses the choice tuple and grabs the amount of shares impacted
    action = choice[0] #accesses the choice tuple and grabs the action(BUY, SELL, HOLD)
    
    bot_choice = bot_decision(price, previous_price, bot_cash, bot_shares, price_history) #returns the decision the bot decides in a tuple
    bot_amount_of_shares = bot_choice[1] #accesses the bot_choice tuple and grabs the amount of shares impacted
    bot_action = bot_choice[0] #accesses the bot_choice tuple and grabs the action(BUY, SELL, HOLD)
    bot_constraint_block = bot_choice[2] #access the bot_choice_typle to get any constraint blocks

    price = round(price, 2) #rounds price again to ensure the execute_trade function uses rounded price
    
    trade = execute_trade(price, human_cash, human_shares, action, amount_of_shares) #executes the trade and stores the updates shares and cash in a tuple
    bot_trade = execute_trade(price, bot_cash, bot_shares, bot_action, bot_amount_of_shares) #executes the trade and stores the updates shares and cash in a tuple

    human_cash = round(trade[1], 2) #stores the new account balance which is grabbed from trade tuple. Rounds to 2 decimal places
    human_shares = trade[0] #stores the new amount of shares the user has which is grabbed from trade tuple

    bot_cash = round(bot_trade[1], 2) #stores the new account balance which is grabbed from trade tuple. Rounds to 2 decimal places
    bot_shares = bot_trade[0] #stores the new amount of shares the bot has which is grabbed from trade tuple

    post_trade_portfolio_value = round((human_cash + (human_shares * price)), 2) #claculates portfolio value after trade and rounds to 2 decimal places
    bot_post_trade_portfolio_value = round((bot_cash + (bot_shares * price)), 2) #claculates portfolio value after trade and rounds to 2 decimal places

    log(name, i, "player", news, sentiment, price, action, amount_of_shares, human_cash, human_shares, post_trade_portfolio_value, "n/a") #logs the human data into logs.csv
    log(bot_name, i, "bot", news, sentiment, price, bot_action, bot_amount_of_shares, bot_cash, bot_shares, bot_post_trade_portfolio_value, bot_constraint_block) #logs the bot data into logs.csv

    # ==========================
    # END OF DAY SUMMARY DISPLAY
    # ==========================
    # Displays updated portfolio information after trades are completed
    print("\n" + "-" * term_width)
    print(center("END OF DAY SUMMARY"))
    print("-" * term_width)

    print(center(f"Cash:            ${human_cash:.2f}"))
    print(center(f"Shares Owned:    {human_shares}"))
    print(center(f"Portfolio Value: ${post_trade_portfolio_value:.2f}"))

    print("-" * term_width)

    time.sleep(4.5) #waits for 4.5 seconds
    price_history.append(price) #adds the day's stock price to the price_history list


# ==========================
# FINAL EXPERIMENT DISPLAY (FIXED OUTSIDE LOOP)
# ==========================
# Displays the final results after all 100 trading days are completed
final_width = get_terminal_width()
print("\n" + "=" * final_width)
print(center("EXPERIMENT COMPLETE"))
print("=" * final_width)

print(center(f"Final Portfolio Value: ${post_trade_portfolio_value:.2f}"))
print("\n" + center("Your trading data has been saved!"))
print(center("To find your CSV file:"))
print(center("1. Open the folder where you extracted this ZIP file"))
print(center("2. Open the folder named 'data'"))
print(center("3. Find the newest CSV file with your name and timestamp"))
print("\n" + center("Please email the most recent .csv file to:"))
print(center("ayaanronaldo08@gmail.com"))
print("\n" + center("Thank you for participating!"))
print("=" * final_width)

while True:
    time.sleep(1)