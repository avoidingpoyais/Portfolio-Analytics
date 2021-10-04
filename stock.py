import quantstats as qs

qs.extend_pandas()

stock = qs.utils.download_returns('FB')

#print(dir(stock)


# print(stock)

# sharpe_ratio = qs.stats.sharpe(stock)

# print(sharpe_ratio)

# print(stock.monthly_returns())

# print(stock.max_drawdown())
#print([f for f in dir(qs.stats) if f[0] != '_'])

# qs.plots.earnings()
stock.plot_earnings(savefig='output/fb_earnings.png', start_balance=100000)

stock.plot_monthly_heatmap(savefig='output/fb_heat_map.png')
