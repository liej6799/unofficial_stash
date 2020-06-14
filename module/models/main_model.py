class dashboard_model(object):
    operationName = ""
    variables = {}
    query = ""

    def __init__(self):
        self.operationName = 'dashboard'
        self.variables = {}
        # refer to the query from the dashboard api call from website.
        self.query = 'query dashboard {\n  hasUndistributedFunds\n  customer {\n    _id\n    reference\n    progress {\n      state\n      pendingConfirmInvestmentPlan\n      __typename\n    }\n    info {\n      firstName\n      __typename\n    }\n    referralCode\n    preferences {\n      accountCcy\n      ack {\n        depositCurrencies\n        transfer\n        hero\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  goals {\n    _id\n    reviewed\n    currency\n    goalType\n    displayName\n    volIndex\n    startDate\n    fundingSource\n    portfolioPerformance {\n      portfolioId\n      currentNav\n      currency\n      __typename\n    }\n    strategy {\n      id\n      valueAtRisk\n      __typename\n    }\n    depositPlans {\n      depositType\n      pendingAmount\n      totalDeposits\n      amount\n      currency\n      __typename\n    }\n    __typename\n  }\n}\n'
