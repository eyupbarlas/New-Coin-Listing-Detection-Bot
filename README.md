# Bzzmans New Coin Listing Detection Bot

## Architecture
![Bzzman's NCL Bot Architecture](https://user-images.githubusercontent.com/72407947/138091419-74ddf933-acd3-4267-9ba5-7d74d888e6f0.jpg)
## About Project
  ***Work in progress.*** This bot basically gets new coin listings from Binance using Binance API. An alert gets raised every time that a coin gets listed on Binance. After the alert, you can use the web page to purchase coins with the portion percentage. Crypto trading is highly volatile. This project doesn't possess any trading advise. Trade carefully.
## Features
* 

## How To Use
### Required Libs
* [Python-Binance](https://python-binance.readthedocs.io/en/latest/ "python-binance")
```
pip install python-binance
```
* [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/ "Python Flask")
```
pip install Flask
```
### Deploying Python Flask App to Heroku
> [Useful documentation by Heroku](https://devcenter.heroku.com/articles/getting-started-with-python "python app deployment")

> [My explaination](https://github.com/eyupbarlas/Crypto-Trading-Bot-with-Tradingview-Binance-Heroku-and-Telegram/issues/1)
#### Useful terminal commands after deployment:
* After making a change on production: `git add .` + `git commit -am "your message"`
* Pushing the app to the cloud: `git push heroku master`
* Checking for logs: `heroku logs --tail`

### Setting Up Telegram Bot
To build a bot for Telegram, you need to talk to [BotFather](https://telegram.me/botfather "BotFather") and follow the simple steps. He will give you a token to start a chat with your bot. 
