# # Download Script
# import json
# from sec_edgar_downloader import Downloader

# dl = Downloader()

# f = open("./tickers.json")

# data = json.load(f)

# for i in data:
#     dl.get("10-K", data[i]["ticker"], amount=1)

# # Process Stocks into Dict Script
# import json
# from random import random

# f = open("./tickers.json")

# data = json.load(f)

# stocks = {}

# for i in data:
#     stocks[data[i]["ticker"]] = {
#         "diversity": random() * random() * 200,
#         "human rights and supply chain": random() * random() * 200,
#         "community impact": random() * random() * 200,
#         "environmental impact": random() * random() * 200,
#         "ecological impact": random() * random() * 200
#     }

# # Pymongo Connection and Population
# import pymongo
# from pymongo import MongoClient
# from pymongo.errors import ServerSelectionTimeoutError
# import os
# from dotenv import load_dotenv

# load_dotenv()

# uri = os.getenv('MONGODB_URI')

# client = MongoClient(uri)

# try:
#     info = client.server_info() # Forces a call.
# except ServerSelectionTimeoutError:
#     print("server is down.")

# db = client["scores"]
# col = db["tickers"]

# for x in stocks:
#     col.insert_one({"name":x, "scores": stocks[x]})
#     # print(stocks[x])