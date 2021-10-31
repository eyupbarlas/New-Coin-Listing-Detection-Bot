import requests, pprint, datetime
from config import *
from binance.client import Client
from binance.enums import *
import pymongo

#! For colored console outputs
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#! Database init
mongo_client = pymongo.MongoClient("your connection")
db = mongo_client.Bzzmans_NCL_Bot
allCoinsCollection = db.allDetectedCoins 
busdCoinsCollection = db.allDetectedBUSDCoins
usdtCoinsCollection = db.allDetectedUSDTCoins


#! Binance Client init
client = Client(REAL_API_KEY, REAL_SECRET_KEY)


#! Telegram Notification
def telegram_bot_sendtext(bot_message):
    bot_token = BOT_TOKEN
    bot_chatID = BOT_CHATID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)

#! Sending notifications after detecting new coin
def sendNotifications(newCoin):
    print(color.DARKCYAN+"Sending new coin notifications via Telegram...")
    telegram_bot_sendtext("***New coin detected:*** \n+`Symbol: {}`".format(newCoin))
    telegram_bot_sendtext("Check the listing time from Binance webpage below: \nhttps://www.binance.com/en/support/announcement/c-48")

#! Market Buy Order
def marketBuyOrder(symbol, quantity):
    try:
        print(color.GREEN+"**Sending Market Buy Order**")
        order = client.order_market_buy(
            symbol=symbol,
            quantity=quantity
        )
        pprint.pprint(order)
        telegram_bot_sendtext("***Market Buy Order Successful!***")


    except Exception as e:
        print("Exception occured: {}".format(e))
        telegram_bot_sendtext("Market Buy Order failed!\n+Exception: `{}`".format(e))

        return False
    
    return True

#! Market Sell Order
def marketSellOrder(symbol, quantity):
    try:
        print(color.GREEN+"**Sending Market Sell Order**")
        order = client.order_market_sell(
            symbol=symbol,
            quantity=quantity
        )
        pprint.pprint(order)
        telegram_bot_sendtext("***Market Sell Order Successful!***")


    except Exception as e:
        print("Exception occured: {}".format(e))
        telegram_bot_sendtext("Market Sell Order Failed!\n+Exception: `{}`".format(e))
        return False
    
    return True

#! Checks for BUSD
def check_BUSD(coinSymbol): 
    busd = "BUSD"
    if busd in coinSymbol: 
        return coinSymbol  
    else:
        return False

#! Checks for USDT
def check_USDT(coinSymbol):
    usdt = "USDT"
    if usdt in coinSymbol:
        return coinSymbol
    else:
        return False

#! Return Latest Coin
def getLatestCoin():
    allCoins = client.get_all_tickers()
    return allCoins[-1].get("symbol")

#! Return Latest Coin(BUSD)
def getLatestCoinBUSD():
    allCoins = client.get_all_tickers()
    onlyBUSD = [""]

    #* Classifying coins(BUSD)
    for coin in allCoins:
        coinSymbol = coin.get("symbol") 
        result = check_BUSD(coinSymbol=coinSymbol) 

        if result:
            onlyBUSD.append(result)

    return onlyBUSD[-1]

#! Return Latest Coin(USDT)
def getLatestCoinUSDT():
    allCoins = client.get_all_tickers()
    onlyUSDT = [""]

    #* Classifying coins(USDT)
    for coin in allCoins:
        coinSymbol = coin.get("symbol") 
        result = check_USDT(coinSymbol=coinSymbol) 

        if result:
            onlyUSDT.append(result)

    return onlyUSDT[-1]

#! Checks if the latest coin is on the DB (All coins)
def latestCoinCheck():
    try:
        latestCoin = getLatestCoin()
        dbCheck = list(busdCoinsCollection.find().sort("date", pymongo.DESCENDING))
        if latestCoin != dbCheck[0]['symbol']:
            print(color.GREEN+"New coin detected! -> {}".format(latestCoin))
            sendNotifications(latestCoin)  
            allCoinsCollection.insert_one({
                "symbol" : latestCoin,
                "date" : datetime.datetime.now()
            })

        else:
            print(color.PURPLE+"No new coins listed.")

    except Exception:
        print(color.BOLD+color.RED+"Error returned in latestCoinCheck().")

#! Checks the latest coin if it is on DB (BUSD)
def latestCoinCheckBUSD():
    try:
        latestBUSDCoin = getLatestCoinBUSD()
        dbBUSDCheck = list(busdCoinsCollection.find().sort("date", pymongo.DESCENDING))
        if latestBUSDCoin != dbBUSDCheck[0]['symbol']:
            print(color.GREEN+"New coin detected! -> {}".format(latestBUSDCoin))
            sendNotifications(latestBUSDCoin)  
            busdCoinsCollection.insert_one({
                "symbol" : latestBUSDCoin,
                "date" : datetime.datetime.now()
            })

        else:
            print(color.PURPLE+"No new BUSD coins listed.")

    except Exception:
        print(color.BOLD+color.RED+"Error returned in latestCoinCheckBUSD().")

#! Checks the latest coin if it is on DB (USDT)
def latestCoinCheckUSDT():
    try:
        latestUSDTCoin = getLatestCoinUSDT()
        dbUSDTCheck = list(usdtCoinsCollection.find().sort("date", pymongo.DESCENDING))
        if latestUSDTCoin != dbUSDTCheck[0]['symbol']:
            print(color.GREEN+"New coin detected! -> {}".format(latestUSDTCoin))
            sendNotifications(latestUSDTCoin)  
            usdtCoinsCollection.insert_one({
                "symbol" : latestUSDTCoin,
                "date" : datetime.datetime.now()
            })

        else:
            print(color.PURPLE+"No new USDT coins listed.")

    except Exception:
        print(color.BOLD+color.RED+"Error returned in latestCoinCheckUSDT().")


#! Main function for Heroku Scheduler to work
if __name__ == "__main__":
    latestCoinCheckBUSD()

    #? Other functions are closed because of production purposes. 
    # latestCoinCheck() 
    # latestCoinCheckUSDT()
