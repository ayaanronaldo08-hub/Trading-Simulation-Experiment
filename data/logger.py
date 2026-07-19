import csv
import os
import sys
from datetime import datetime

# Gets the folder where the executable is being run from.
# If running as a Python script, uses the script folder.
# If running as an .exe, uses the executable folder.
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Creates data folder next to the executable/script
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

# Stores the current CSV filename
LOG_FILE = None


def start_log(name):
    """
    Creates a new CSV file every time the experiment starts.
    The file is saved in a data folder next to the executable.
    """

    global LOG_FILE

    safe_name = "".join(
        c for c in name if c.isalnum() or c in (" ", "_", "-")
    ).strip()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    LOG_FILE = os.path.join(
        DATA_DIR,
        f"{safe_name}_{timestamp}.csv"
    )

    with open(LOG_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "name",
            "day",
            "player_type",
            "news",
            "sentiment",
            "price",
            "action",
            "quantity",
            "cash",
            "shares",
            "portfolio_value",
            "block"
        ])


def log(name, day, player_type, news, sentiment, price,
        action, quantity, cash, shares,
        portfolio_value, block):
    """
    Adds one trading record to the current experiment CSV.
    """

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            name,
            day,
            player_type,
            news,
            sentiment,
            round(price, 2),
            action,
            quantity,
            round(cash, 2),
            shares,
            round(portfolio_value, 2),
            block
        ])
