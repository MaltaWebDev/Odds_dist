import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import scipy.stats as stats
import numpy as np

ticker = input('please enter a ticker: ').lower()

path = f"./{ticker}.csv"

df = pd.read_csv(path)

# Create Returns column and format as % to two decimal places
df['Returns'] = ((df['Open'] - df['Close']) / df['Open'])

# Create histogram of Returns column
bins = [round(-0.1 + 0.005 * i, 4) for i in range(42)]
plt.hist(df['Returns'], bins=bins, density=True)
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.title(f'{ticker.upper()} Distribution of Returns')

# add normal distribution with same mean and standard deviation as data
mu, sigma = df['Returns'].mean(), df['Returns'].std()
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma)) 

# format y-axis as percentages
fmt = mtick.PercentFormatter(xmax=1, decimals=0)
plt.gca().xaxis.set_major_formatter(fmt)

# save plot as PNG file
plt.savefig('histogram.png', dpi=300)

plt.show()

# calculate probability and cumulative columns
count = df['Returns'].count()
