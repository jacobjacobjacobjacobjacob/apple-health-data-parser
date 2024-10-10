# src/analysis/analysis.py
from src.analysis.load_dataframes import DataFrameLoader
from src.analysis.merge_dataframes import DataFrameMerger
from src.analysis.summaries.monthly_summary import get_monthly_mean_summary, get_monthly_sum_summary
from src.constants.paths import CLEANED_DATA_DIRECTORY

loader = DataFrameLoader(CLEANED_DATA_DIRECTORY)
dataframes = loader.load_all_dataframes()
print(dataframes)

# Merge the dataframes
merger = DataFrameMerger(dataframes)
merged_df = merger.merge_dataframes()

# Generate summaries from the merged DataFrame
monthly_mean_summary = get_monthly_mean_summary(df=merged_df)
monthly_sum_summary = get_monthly_sum_summary(df=merged_df)

# Examples:
print("Monthly Mean Summary:")
print(monthly_mean_summary)
print("Monthly Sum Summary:")
print(monthly_sum_summary)
