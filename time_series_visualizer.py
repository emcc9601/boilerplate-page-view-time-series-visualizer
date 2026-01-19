import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# Ethan's note: Did not change index column as it caused the data cleaning to break when using df.drop()
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data
removeIndexes = []
lowerQuantile = np.quantile(df["value"], 0.025)
upperQuantile = np.quantile(df["value"], 0.975)

for i in range(len(df["value"])):
    if (lowerQuantile >= df["value"][i]) or (upperQuantile <= df["value"][i]):
        removeIndexes.append(i)

df = df.drop(removeIndexes, axis=0)

# For testing purposes, uncomment this and run "python3 time_series_visualizer.py"
# print(df)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 6))
    ax = sns.lineplot(data=df, x="date", y="value")
    ax.set(xlabel="Date", ylabel="Page Views", title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    fig = ax.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df

    df_bar["date"] = pd.to_datetime(df_bar["date"])
    df_bar["year"] = df_bar["date"].dt.year
    df_bar["month"] = df_bar["date"].dt.strftime('%b')

    df_bar = df_bar.groupby(["year", "month"])["value"].mean().reset_index()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax = sns.barplot(data=df_bar, x="year", y="value", hue="month")
    ax.set(xlabel="Years", ylabel="Average Page Views")
    ax.legend().set_title("Months")
    fig = ax.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
