# Bzzmans New Coin Listing Detection Bot

## Architecture
![Bzzman's NCL Bot Architecture](https://user-images.githubusercontent.com/72407947/138091419-74ddf933-acd3-4267-9ba5-7d74d888e6f0.jpg)
## About Project
  ***Work in progress.*** This bot basically gets new coin listings from Binance using Binance API. An alert gets raised every time that a coin gets listed on Binance. After the alert, you can use the web page to purchase coins with the portion percentage. You need a Binance account to start trading. Then when you connect the API keys, you can purchase coins. Crypto trading is highly volatile. This project doesn't possess any trading advise. Trade carefully.
## Features
* Getting market data every 10 minutes to detect if any new coin gets listed on Binance.
* After detection, user gets notified via Telegram.
* After notification, user can enter the Flask web application to purchase coin that coin quickly.
* Only BUSD based coins are enabled for purchase for now. ***Other coins are on progress***.
* You can contact with me to enabling other coins. Contact info below this page.

## How To Use
### Required Libs
* [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/ "Python Flask")
```
pip install Flask
```
* [PyMongo](https://pymongo.readthedocs.io/en/stable/ "Python Pymongo")
```
pip install pymongo
```
* [dnspython](https://pypi.org/project/dnspython/2.1.0/ "dnspython")
```
pip install dnspython
```
* [Passlib](https://passlib.readthedocs.io/en/stable/ "passlib")
```
pip install passlib
```

### Deploying Python Flask App to Heroku
> [Useful documentation by Heroku](https://devcenter.heroku.com/articles/getting-started-with-python "python app deployment")

> [My explaination on another project](https://github.com/eyupbarlas/Crypto-Trading-Bot-with-Tradingview-Binance-Heroku-and-Telegram/issues/1)
#### Useful terminal commands after deployment:
* After making a change on production: `git add .` + `git commit -am "your message"`
* Pushing the app to the cloud: `git push heroku master`
* Checking for logs: `heroku logs --tail`

### Setting Up Telegram Bot
To build a bot for Telegram, you need to talk to [BotFather](https://telegram.me/botfather "BotFather") and follow the simple steps. He will give you a token to start a chat with your bot. 

### Setting up MongoDB Atlas
> [Useful documentation from MongoDB](https://www.mongodb.com/developer/how-to/use-atlas-on-heroku/ "Atlas on Heroku")
<br>

> **Personal Information**
> 
>> Eyüp Barlas  eyupbarlas2134@gmail.com
>> Waasiq Masood  waasiq.masood@gmail.com
>> For more projects from Eyüp Barlas, [click here](https://github.com/eyupbarlas "my repos").
>> For more projects from Waasiq Masood, [click here](https://github.com/waasiqmasood "my repos").
