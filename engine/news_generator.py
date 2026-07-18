import random

PositiveNews = ["Economic indicators show strong growth", "Company announces record profits", "New product launch exceeds expectations"]
NegativeNews = ["Economic indicators show signs of slowdown", "Company reports lower-than-expected earnings", "New product launch fails to meet expectations"]
NeutralNews = ["Company announces new partnership", "Economic indicators remain unchanged", "New product launch receives mixed reviews"]

def generate_news():
    pool = ["neutral", "neutral", "neutral", "positive", "positive", "negative", "negative"]
    roll = random.choice(pool) #chooses sentiment of news
    if roll == "neutral": #following selection statements give news statements based on sentiment chosen
        return random.choice(NeutralNews), roll
    elif roll == "positive":
        return random.choice(PositiveNews), roll
    else: 
        return random.choice(NegativeNews), roll
    
