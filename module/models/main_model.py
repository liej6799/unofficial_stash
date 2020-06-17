class dashboard_model(object):
    operationName = ""
    variables = {}
    query = ""

    def __init__(self):
        self.operationName = 'dashboard'
        self.variables = {}
        # refer to the query from the dashboard api call from website.
        self.query = 'query dashboard {\n  hasUndistributedFunds\n  customer {\n    _id\n    reference\n    progress {\n      state\n      pendingConfirmInvestmentPlan\n      __typename\n    }\n    info {\n      firstName\n      __typename\n    }\n    referralCode\n    preferences {\n      accountCcy\n      ack {\n        depositCurrencies\n        transfer\n        hero\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  goals {\n    _id\n    reviewed\n    currency\n    goalType\n    displayName\n    volIndex\n    startDate\n    fundingSource\n    portfolioPerformance {\n      portfolioId\n      currentNav\n      currency\n      __typename\n    }\n    strategy {\n      id\n      valueAtRisk\n      __typename\n    }\n    depositPlans {\n      depositType\n      pendingAmount\n      totalDeposits\n      amount\n      currency\n      __typename\n    }\n    __typename\n  }\n}\n'


class asset_performance_model(object):
    operationName = ""
    variables = {}
    query = ""

    def __init__(self, goalId):
        self.operationName = 'assetPerformance'
        self.variables = {
            'goalId': goalId
        }
        # refer to the query from the assetPerformance call from website.
        self.query = 'query assetPerformance($goalId: ID!) {\n  customer {\n    _id\n    progress {\n      state\n      __typename\n    }\n    __typename\n  }\n  goalsCount\n  goal(_id: $goalId) {\n    _id\n    displayName\n    name\n    volIndex\n    startDate\n    fundingSource\n    goalType\n    reviewed\n    currentAllocation {\n      strategyId\n      weights {\n        weight\n        security {\n          name\n          assetClass\n          __typename\n        }\n        __typename\n      }\n      countries {\n        country\n        name\n        region\n        currencies\n        weight\n        __typename\n      }\n      __typename\n    }\n    portfolioPerformance {\n      netDeposits\n      currentNav\n      __typename\n    }\n    portfolioAssetsPerformance {\n      securities {\n        symbol\n        currentWeight\n        assetClass\n        subAssetClass\n        timeWeightedReturns {\n          sinceInception\n          yearToDate\n          oneYear\n          sixMonths\n          threeMonths\n          oneMonth\n          __typename\n        }\n        __typename\n      }\n      cash {\n        symbol\n        units\n        currentWeight\n        assetClass\n        subAssetClass\n        __typename\n      }\n      dividends {\n        symbol\n        currentWeight\n        assetClass\n        subAssetClass\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n'


class etf_detail_model(object):
    operationName = ""
    variables = {}
    query = ""

    def __init__(self, goalId):
        self.operationName = 'etfDetailsWithGoal'
        self.variables = {
            'goalId': goalId
        }
        # refer to the query from the assetPerformance call from website.
        self.query = 'query etfDetailsWithGoal($goalId: ID!) {\n  securities {\n    ...securitiesFields\n    __typename\n  }\n  goal(_id: $goalId) {\n    ...goalFields\n    __typename\n  }\n  latestFxRate(ccyPairs: \"USDMYR\") {\n    ...latestFxRateFields\n    __typename\n  }\n}\n\nfragment securitiesFields on SecurityDetails {\n  symbol\n  ccy\n  name\n  description\n  productUrl\n  dividendFrequency\n  __typename\n}\n\nfragment goalFields on Goal {\n  _id\n  goalType\n  displayName\n  name\n  currency\n  strategyId\n  goalType\n  portfolioAssetsPerformance {\n    securities {\n      symbol\n      units\n      totalValue\n      currency\n      weight\n      currentWeight\n      lastPrice\n      assetClass\n      totalDividendsEarned\n      nextPayoutAmount\n      dividendFrequency\n      timeWeightedReturns {\n        sinceInception\n        yearToDate\n        oneYear\n        sixMonths\n        threeMonths\n        oneMonth\n        __typename\n      }\n      __typename\n    }\n    cash {\n      symbol\n      name\n      totalValue\n      weight\n      currency\n      currentWeight\n      assetClass\n      __typename\n    }\n    dividends {\n      symbol\n      name\n      currency\n      currentWeight\n      totalValue\n      assetClass\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment latestFxRateFields on LatestFXRate {\n  baseCcy\n  quoteCcy\n  rate\n  quoteDate\n  __typename\n}\n'


class securities_model(object):
    symbol = ""
    units = 0.0
    price = 0.0
    value = 0.0

    def __init__(self, symbol, units, price, value):
        self.symbol = symbol
        self.units = units
        self.price = price
        self.value = value

