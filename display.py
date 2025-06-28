import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#def showTime(data):
#    columns = data.columns # Assume the first column to be the time
#    fig, ax = plt.subplots(figsize=(16,6))
#    
#    for col in columns[1:]:
#        ax.plot(data[columns[0]], data[col], label=col)
#    
#    # Assume the time between entries is 1 hour
#    ax.xticks = [i*24 for i in range(round(len(data)/24))]
#    ax.xticklabels=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
#    ax.legend(loc="upper right")
#
#    plt.show()

def showTime(data):
    columns = data.columns  # Assume the first column to be the time
    time_column = columns[0]  # First column is the time
    num_series = len(columns) - 1  # Number of time series (excluding the time column)
    
    # Create subplots: one subplot per time series, organized in a single column
    fig, axes = plt.subplots(num_series, 1, figsize=(16, 6 * num_series), sharex=True)
    
    # If there's only one subplot, wrap axes in a list for consistency
    if num_series == 1:
        axes = [axes]
    
    # Plot each time series in its own subplot
    for i, col in enumerate(columns[1:]):
        axes[i].plot(data[time_column], data[col], label=col)
        axes[i].set_title(f"Time Series: {col}")
        axes[i].legend(loc="upper right")
    
    # Dynamically adjust x-ticks based on the length of the time series
    total_hours = len(data)
    if total_hours <= 24:  # Less than or equal to 1 day
        xticks = range(total_hours)
        xticklabels = [f"{hour}:00" for hour in xticks]
    elif total_hours <= 24 * 7:  # Less than or equal to 1 week
        xticks = range(0, total_hours, 24)  # Daily intervals
        xticklabels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][:len(xticks)]
    elif total_hours <= 24 * 30:  # Less than or equal to 1 month
        xticks = range(0, total_hours, 24 * 7)  # Weekly intervals
        xticklabels = [f"Week {i+1}" for i in range(len(xticks))]
    else:  # Greater than 1 month (up to a year)
        xticks = range(0, total_hours, 24 * 30)  # Monthly intervals
        xticklabels = [f"Month {i+1}" for i in range(len(xticks))]
    
    # Apply x-ticks and labels to the last subplot
    axes[-1].set_xticks(xticks)
    axes[-1].set_xticklabels(xticklabels)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Show the plot
    plt.show()