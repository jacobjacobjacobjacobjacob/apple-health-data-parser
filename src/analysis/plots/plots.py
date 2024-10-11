# src/analysis/plots/plots.py
from src.analysis.analysis import load_dataframes, get_merged_dataframe
from src.analysis.plots.plot_utils import (
    create_histogram,
    create_line_plot,
    create_box_plot,
)

# Main function to run the plotting examples
if __name__ == "__main__":
    # Load data
    dataframes = load_dataframes()
    df = get_merged_dataframe(dataframes)

    # Function to print available dataframes
    def print_available_dataframes(dataframes):
        for dataframe_name, df in dataframes.items():
            print(dataframe_name)

    # Print available dataframes
    # print_available_dataframes(dataframes)

    create_histogram(
        df,
        x_axis="Resting Heartrate",
        title="Histogram of Resting Heartrate",
        show_plot=True,
        save_plot_as_png=True,
        file_name="resting_heartrate_histogram.png",
        width=500,  # Plot width
        height=400,  # Plot height
        bargap=0,  # No gap between bars
    )

    # Create rolling Step Count line plot
    create_line_plot(
        df,
        x_axis="date",
        y_axis="Step Count",
        show_plot=True,
        save_plot_as_png=True,
        file_name="rolling_step_count.png",
        rolling_average=True,  # Enable rolling average
        rolling_window_days=14,  # Set rolling window size to 14 days
        y_label="Step Count",
        x_label="Date",
        width=900,  # Plot width
        height=400,  # Plot height
    )

    # Create histogram for Sleep Hours
    create_histogram(
        df,
        x_axis="Sleep Hours",
        title="Histogram of Sleep Hours",
        color="#5F9EA0",  # Custom color for bars
        show_plot=True,
        save_plot_as_png=True,
        nbins=20,  # Number of bins for the histogram
        file_name="sleep_hours_histogram.png",
        width=500,  # Plot width
        height=400,  # Plot height
        bargap=0,  # No gap between bars
        xaxis_title="Sleep Hours",
    )

    # Create box plot for Sleep Hours by day of the week
    create_box_plot(
        df,
        x_axis="day_of_week",
        y_axis="Sleep Hours",
        title="Box Plot of Sleep Hours by Day of Week",
        show_plot=True,
        save_plot_as_png=True,
        file_name="sleep_by_day_of_week.png",
        y_label="Sleep Hours",
        x_label="Day of Week",
        width=600,  # Plot width
        height=400,  # Plot height
    )
