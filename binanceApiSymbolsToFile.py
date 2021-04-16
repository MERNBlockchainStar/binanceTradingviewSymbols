import requests, json

apiSymbols = requests.get('https://api.binance.com/api/v3/exchangeInfo')
jsonApiSymbols = json.loads(apiSymbols.text)
jsonSymbols = jsonApiSymbols['symbols']

quoteAssets = {"BTC", "USDT"}
binStr = 'BINANCE:'
resList = []
res = ''

def createSpotList():
    global resList
    for symbol in jsonSymbols:
        symbolStatus = symbol['status']
        if symbolStatus == 'TRADING':
            if symbol['quoteAsset'] in quoteAssets and symbol['isSpotTradingAllowed'] == True:
                sym = symbol['symbol']
                resList.append(sym)

def createFutureList():
    global resList
    for symbol in jsonSymbols:
        symbolStatus = symbol['status']
        if symbolStatus == 'TRADING':
            if symbol['quoteAsset'] in quoteAssets and symbol['isMarginTradingAllowed'] == True:
                sym = symbol['symbol']
                resList.append(sym)

# user interaction
print('Binance symbol creation tool')
userSelect = input("Select: spot (s), future (f) or all (a) symbols: ")
print("Selection: " + userSelect)

if userSelect == 's':
    createSpotList()
elif userSelect == 'f':
    createFutureList()
elif userSelect == 'a':
    createSpotList()
    createFutureList()

# filter duplicates from list
resList = list(dict.fromkeys(resList))

# crete string from list
for item in resList:
    if res == '':
        res = res + binStr + item
    else:
        res = res + ',' + binStr + item

# write result var in new file
filename = 'BinanceSymbols.txt'
new_file = open(filename, "w")
new_file.write(res)

print('BinanceSymbols.txt created with ' + str(len(resList)) + ' items.')