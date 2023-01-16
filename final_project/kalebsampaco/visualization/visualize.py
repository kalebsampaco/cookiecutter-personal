import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def covid_time_series(df: pd.DataFrame):
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");
    
def top_countries(df, countries, n):
    top_countries_df = (
    df
    .select_columns(["country_region", "value"])
    .groupby(["country_region"])
    .aggregate("sum")
    .sort_values("value", ascending=False)
    .reset_index()
    .head(20)
    .transform_column(
        column_name="country_region",
        function=lambda x: "red" if x in countries else "lightblue",
        dest_column_name="color"
        )
    )
    return top_countries_df.head(n)

def visualize_top_countries(df):
    sns.barplot(
        data=df,
        x="value",
        y="country_region",
        palette=df.color
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");