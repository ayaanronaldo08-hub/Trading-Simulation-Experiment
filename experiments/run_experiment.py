from engine.news_generator import generate_news #import generate news function from news_generator file
from engine.price_engine import price_change #import price change function from price_engine file
from engine.trade_engine import execute_trade #import execute trade function from trade_engine file
from strategies.human_strategy import human_decision #import human decision function from human_strategy file
from strategies.bot_strategies import bot_decision #import bot decision function from bot_startegies file
from data.logger import log, start_log #imports the logging functions from logger file
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
trend = 0 #inital trend value

human_cash = 1000 #initial acc balance for human
human_shares = 0 #initial amount of shares held for human

bot_cash = 1000 #initial acc balance for bot
bot_shares = 0 #intiial amount of shares held for human
    
name = input("Enter your name: ")
bot_name = "bot"

start_log(name) #creates a new CSV file every time the experiment starts

price_history = [] #the list containing all prices from every day
