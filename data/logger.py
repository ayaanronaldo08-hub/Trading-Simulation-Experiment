import csv
import os
from datetime import datetime

# Create writable data folder next to executable/script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

# Stores the filename after the first call
LOG_FILE = None


def log(name, day, player_type, news, sentiment, price,
        action, quantity, cash, shares,
        portfolio_value, block):

    global LOG_FILE

    # Create a new CSV only once per experiment
    if LOG_FILE is None:

        # Removes characters Windows doesn't allow in filenames
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

    # Write one row
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
