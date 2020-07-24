# Alpaca Third Party Services
This is a repo for third party services integration with the alpaca api


The Alpaca SDK will check the environment for a number of variables which can be used rather than hard-coding these into your scripts.

| Environment                      | default                                                                                | Description                                                                                                            |
| -------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ALPHAVANTAGE_API_KEY=<key_id>    |     

## Alpha Vantage

In addition to Polygon is Alpha Vantage, for users without a live account (paper trading) or want to use the unique features of AV data. You can get a free key [here](https://www.alphavantage.co/support/#api-key) and the documentation is [here](https://www.alphavantage.co/documentation/). Premium keys are also available [here](https://www.alphavantage.co/premium/#intro)
This python SDK wraps their API service and seamlessly integrates it with the Alpaca
API. `alpaca_trade_api.REST.alpha_vantage` will be the `REST` object for Alpha Vantage.

The example below gives AAPL daily OHLCV data in a DataFrame format.

```py
import alpaca_trade_api as tradeapi

api = tradeapi.REST()
aapl = api.alpha_vantage.historic_quotes('AAPL', adjusted=True, output_format='pandas')
```

## alpha_vantage/REST
It is initialized through alpaca `REST` object.

### alpha_vantage/REST.get(params=None)
Customizable endpoint, where you can pass all keywords/paramters from the documentation:https://www.alphavantage.co/documentation/#

Returns the specific customized data.

### alpha_vantage/REST.historic_quotes(symbol, adjusted=False, outputsize='full', cadence='daily', output_format=None)
Returns a `csv`, `json`, or `pandas` object of historical OHLCV data.

### alpha_vantage/REST.intraday_quotes(symbol, interval='5min', outputsize='full', output_format=None)
Returns a `csv`, `json`, or `pandas` object of intraday OHLCV data.

### alpha_vantage/REST.current_quote(symbol)
Returns a `json` object with the current OHLCV data of the selected symbol.

### alpha_vantage/REST.last_quote(symbol)
Returns a `json` object with the current OHLCV data of the selected symbol (same as `current_quote`).

### alpha_vantage/REST.search_endpoint(keywords, datatype='json')
Returns a `csv`, `json`, or `pandas` object that contains the best-matching symbols and market information based on keywords of your choice.

### alpha_vantage/REST.company(symbol, datatype='json')
Same as `search_endpoint`.

### alpha_vantage/REST.historic_fx_quotes(from_symbol, to_symbol, outputsize='full', cadence='daily', output_format=None)
Returns a `csv`, `json`, or `pandas` object of historical OHLCV data for the currency pair.

### alpha_vantage/REST.intraday_fx_quotes(from_symbol, to_symbol, interval='5min', outputsize='full', output_format=None)
Returns a `csv`, `json`, or `pandas` object of intraday OHLCV data for the currency pair.

### alpha_vantage/REST.exchange_rate(from_currency, to_currency)
Returns a `json` object with the current OHLCV data of the selected currency pair (digital or physical)

### alpha_vantage/REST.historic_cryptocurrency_quotes(self, symbol, market, cadence='daily', output_format=None)
Returns a `csv`, `json`, or `pandas` object of historical OHLCV data for the cryptocurrency pair.

### alpha_vantage/REST.techindicators(self, techindicator='SMA', output_format='json', **kwargs)
Returns a `csv`, `json`, or `pandas` object with the data from the techindicator of choice.

### alpha_vantage/REST.sector()
Returns a `json` of the currrency sector performances.
