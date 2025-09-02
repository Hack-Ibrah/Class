# Pandas & Matplotlib Assignment
# This script reads a CSV of monthly sales, prints summary stats, and creates a plot.
# Created by Hack-Ibrah as part of PLP coursework.

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('data.csv')
    print('First 5 rows:')
    print(df.head())
    print('\nSummary statistics:')
    print(df.describe())

    # Plotting sales trend
    plt.figure(figsize=(8,4))
    plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('sales_trend.png')  # saves a PNG that you can submit as proof
    print('\nPlot saved to sales_trend.png')
    plt.show()

if __name__ == '__main__':
    main()
