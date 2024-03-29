## --------------------------------------------------------------------------------------##
##
## Script name: plot_hydrograph.py
##
## Purpose of the script: Plot hydrograph with GOF stats (NSE, Rsq, PBIAS)
##
## Input data: Dataframe has 4 columns, Date, SimulatedQ, ObservedQ, Precip
## 
## Author: Chinmay Deval
##
## Created On: 2020-04-01
##
## Copyright (c) Chinmay Deval, 2020
## Email: chinmay.deval91@gmail.com
##
## --------------------------------------------------------------------------------------##
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from matplotlib.ticker import MaxNLocator

# Read data from CSV
data = pd.read_csv('dummy_data.csv')

# Function to calculate PBIAS
def pbias(observed, simulated):
    return 100 * (simulated - observed).sum() / observed.sum()

# Function to calculate NSE
def nse(observed, simulated):
    return 1 - ((observed - simulated)**2).sum() / ((observed - observed.mean())**2).sum()

# Calculate statistics
bias = pbias(data['ObservedQ'], data['SimulatedQ'])
r_squared = r2_score(data['ObservedQ'], data['SimulatedQ'])
nse_value = nse(data['ObservedQ'], data['SimulatedQ'])

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 8), dpi=300)  # Adjust figsize and dpi as needed

ax1.set_xlabel('Date')
ax1.set_ylabel('Streamflow (mm)')
ax1.plot(data['Date'], data['ObservedQ'], color='black', label='Observed Streamflow')  
ax1.plot(data['Date'], data['SimulatedQ'], color='red', linestyle='--', label='Simulated Streamflow')
ax1.tick_params(axis='y')  

ax2 = ax1.twinx()
ax2.set_ylabel('Precipitation (mm)')
ax2.plot(data['Date'], data['Precip'], color='tab:blue', label='Precipitation')
ax2.tick_params(axis='y')  # Set label color for precipitation

# Rotate x-axis ticks by 45 degrees
ax1.tick_params(axis='x', rotation=45)

# Move legend outside the plot area
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
fig.legend(lines + lines2, labels + labels2, loc='upper left', bbox_to_anchor=(0.25, 1.0), ncol=3)

# Invert y-axis for precipitation
ax2.invert_yaxis()

# Limit number of x ticks
ax1.xaxis.set_major_locator(MaxNLocator(nbins=25))

# Set y-axis to start at 0
ax1.set_ylim(0, None)

# Limit number of y ticks
#ax1.yaxis.set_major_locator(MaxNLocator(nbins=15))
#ax2.yaxis.set_major_locator(MaxNLocator(nbins=15))

# Title
plt.title('')

# Display goodness of fit statistics outside the plot area
stats_x = 0.5
stats_y = 1.05  # Adjust this value to change the vertical position
plt.text(stats_x, stats_y, f'PBIAS: {bias:.2f}%, R2: {r_squared:.2f}, NSE: {nse_value:.2f}',
         horizontalalignment='center',
         verticalalignment='top',  
         transform=ax1.transAxes)

# Save plot directly to file with legend
plt.savefig('hydrograph.png', bbox_inches='tight')