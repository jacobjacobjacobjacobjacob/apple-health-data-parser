# src/analysis/analysis.py

# from src.analysis.plots.plots import create_histogram
from src.analysis.load_dataframes import DataFrameLoader
from src.analysis.merge_dataframes import DataFrameMerger
from src.analysis.summaries.monthly_summary import (
    get_monthly_mean_summary,
    get_monthly_sum_summary,
)
from src.constants.paths import CLEANED_DATA_DIRECTORY


def load_dataframes():
    loader = DataFrameLoader(CLEANED_DATA_DIRECTORY)
    dataframes = loader.load_all_dataframes()
    return dataframes


def get_merged_dataframe(dataframes):
    # Merge the dataframes
    merger = DataFrameMerger(dataframes)
    merged_df = merger.merge_dataframes()

    return merged_df


if __name__ == "__main__":
    dataframes = load_dataframes()
    merged_df = get_merged_dataframe(dataframes)

    monthly_mean_summary = get_monthly_mean_summary(df=merged_df)
    monthly_sum_summary = get_monthly_sum_summary(df=merged_df)

    # Examples:
    print("Monthly Mean Summary:")
    print(monthly_mean_summary)
    print("Monthly Sum Summary")
    print(monthly_sum_summary)
