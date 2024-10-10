# src/analysis/analysis.py
import pandas as pd
from load_dataframes import DataFrameLoader
from merge_dataframes import DataFrameMerger
from summaries.monthly_summary import get_monthly_mean_summary, get_monthly_sum_summary

# Load the dataframes
loader = DataFrameLoader("/Users/daniel/Desktop/python/apple_health/data/cleaned")
dataframes = loader.load_all_dataframes()

# Merge the dataframes
merger = DataFrameMerger(dataframes)
merged_df = merger.merge_dataframes()

# Generate summaries from the merged DataFrame
monthly_mean_summary = get_monthly_mean_summary(df=merged_df)
monthly_sum_summary = get_monthly_sum_summary(df=merged_df)
# Print or log the summaries
print("Monthly Mean Summary:")
# print(monthly_mean_summary)
print("Monthly Sum Summary:")
print(monthly_sum_summary)
