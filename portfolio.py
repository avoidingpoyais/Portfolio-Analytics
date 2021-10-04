import quantstats as qs

qs.extend_pandas()

stock = qs.utils.download_returns('GLD', period="10y")

qs.reports.html(stock, title='AP Investing', output='output/gld.html')
stock = qs.utils.download_returns('QQQ', period="10y")

qs.reports.html(stock, "SPY", title="QQQ vs. SPY", output='output/qqq_vs_spy.html')

tickers = {
    'FB': 0.2,
    'AAPL': 0.2,
    'AMZN': 0.2,
    'MSFT': 0.2,
    'GOOG': 0.2
}

quartz = portfolio = qs.utils.make_index(tickers)
qs.reports.html(quartz, "qqq", output="output/quartz_vs_qqq.html")
