from config import * 
from flask import Flask, render_template, request, redirect, url_for
from script import *

"""
! --- Bzzman's New Coin Listing Bot ---
! Features:
* This bot basically gets new coin listings from Binance using Binance API. An alert gets raised everytime that a coin gets listed on Binance.
* When a coin gets listed on Binance, after you get the notification you can go the Flask web page and make purchase with your portion of balance.
* In the website deployed by Heroku; you will find a simple and easily understandable user interface, which allows you to look into latest coins listed on Binance.
* You can enter the quantity of the coin you want to buy using the range object connected to your spot wallet on Binance.

Website: https://bzzmans-new-coin-listing-bot.herokuapp.com/

Eyüp Barlas production.
"""


#! Flask app init
app = Flask(__name__)
app.secret_key = "Bzzmans_Secret"

#! Index page
@app.route("/")
def index():
    #* Latest coins to print out
    latestCoin = getLatestCoin()
    latestCoinBUSD = getLatestCoinBUSD()
    latestCoinUSDT = getLatestCoinUSDT()

    return render_template("index.html", latestCoin=latestCoin, latestCoinBUSD=latestCoinBUSD, latestCoinUSDT=latestCoinUSDT)



#! Getting Quantity -> only BUSD for now
@app.route("/setQuantity", methods=["POST"])
def setQuantity():
    quantityEntry = float(request.form.get("quantityEntry"))
    print(quantityEntry)

    latestBUSD = getLatestCoinBUSD()

    #* Balance percentage algorithm
    balance = client.get_asset_balance(asset="BUSD") 
    portionBalance = float(balance['free']) * (quantityEntry/100)
    print("Money on operation: {}".format(portionBalance))

    #todo-> only busd for now
    marketBuyOrder(symbol=latestBUSD, quantity=portionBalance)
    

    return redirect(url_for("index"))


#! Flask run
if "__main__" == __name__:
    app.run(debug=True)
