# src/analysis/plots/plots.py
from src.analysis.analysis import load_dataframes, get_merged_dataframe
from src.analysis.plots.plot_utils import (
    create_histogram,
    create_line_plot,
    create_box_plot,
)

# Constants
PLOT_WIDTH = 500
PLOT_HEIGHT = 400
SAVE_PLOT_AS_PNG = False
SHOW_PLOT = True

def print_available_dataframes(dataframes):
    for dataframe_name in dataframes.items():
        print(dataframe_name)

def create_plots(df):
    try:
        create_histogram(
            df,
            x_axis="Resting Heartrate",
            title="Histogram of Resting Heartrate",
            show_plot=SHOW_PLOT,
            save_plot_as_png=SAVE_PLOT_AS_PNG,
            file_name="resting_heartrate_histogram.png",
            width=PLOT_WIDTH,
            height=PLOT_HEIGHT,
            bargap=0,
        )

        create_line_plot(
            df,
            x_axis="date",
            y_axis="Step Count",
            show_plot=SHOW_PLOT,
            save_plot_as_png=SAVE_PLOT_AS_PNG,
            file_name="rolling_step_count.png",
            rolling_average=True,
            rolling_window_days=14,
            y_label="Step Count",
            x_label="Date",
            width=900,
            height=PLOT_HEIGHT,
        )

        create_histogram(
            df,
            x_axis="Sleep Hours",
            title="Histogram of Sleep Hours",
            color="#5F9EA0",
            show_plot=SHOW_PLOT,
            save_plot_as_png=SAVE_PLOT_AS_PNG,
            nbins=20,
            file_name="sleep_hours_histogram.png",
            width=PLOT_WIDTH,
            height=PLOT_HEIGHT,
            bargap=0,
            xaxis_title="Sleep Hours",
        )

        create_box_plot(
            df,
            x_axis="day_of_week",
            y_axis="Sleep Hours",
            title="Box Plot of Sleep Hours by Day of Week",
            show_plot=SHOW_PLOT,
            save_plot_as_png=SAVE_PLOT_AS_PNG,
            file_name="sleep_by_day_of_week.png",
            y_label="Sleep Hours",
            x_label="Day of Week",
            width=600,
            height=PLOT_HEIGHT,
        )
    except Exception as e:
        print(f"An error occurred while creating plots: {e}")

if __name__ == "__main__":
    try:
        # Load data
        dataframes = load_dataframes()
        df = get_merged_dataframe(dataframes)

        # Print available dataframes
        #print_available_dataframes(dataframes)

        # Create plots
        create_plots(df)
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
